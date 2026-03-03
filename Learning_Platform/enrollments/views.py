from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Enrollment
from courses.models import Course
from .models import Progress
from courses.models import Video

class EnrollView(APIView):

    def post(self, request, course_id):
        if request.user.role != 'student':
            return Response({"error": "Only students can enroll"})

        course = Course.objects.get(id=course_id)

        enrollment, created = Enrollment.objects.get_or_create(
            student=request.user,
            course=course
        )

        if not created:
            return Response({"message": "Already enrolled"})

        return Response({"message": "Enrolled successfully"})
    
class ProgressView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, course_id):

        if request.user.role != 'student':
            return Response({"error": "Only students can view progress"}, status=403)

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=404)

        total_videos = course.videos.count()

        completed_videos = Progress.objects.filter(
            student=request.user,
            video__course=course,
            completed=True
        ).count()

        if total_videos == 0:
            progress_percentage = 0
        else:
            progress_percentage = (completed_videos / total_videos) * 100

        return Response({
            "course": course.title,
            "progress": progress_percentage
        })
        
class MarkCompleteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, video_id):

        if request.user.role != "student":
            return Response({"error": "Only students can complete videos"}, status=403)

        try:
            video = Video.objects.get(id=video_id)
        except Video.DoesNotExist:
            return Response({"error": "Video not found"}, status=404)

        progress, created = Progress.objects.get_or_create(
            student=request.user,
            video=video
        )

        progress.completed = True
        progress.save()

        return Response({"message": "Video marked as completed"})
