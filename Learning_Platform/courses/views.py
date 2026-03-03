from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Course
from .serializers import CourseSerializer

class CreateCourseView(generics.CreateAPIView):
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        if self.request.user.role != 'instructor':
            raise PermissionDenied("Only instructors can create courses")
        serializer.save(instructor=self.request.user)