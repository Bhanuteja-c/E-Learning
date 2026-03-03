from .models import Progress

def calculate_progress(student, course):
    total_videos = course.video_set.count()

    completed_videos = Progress.objects.filter(
        student=student,
        video__course=course,
        completed=True
    ).count()

    if total_videos == 0:
        return 0

    return (completed_videos / total_videos) * 100