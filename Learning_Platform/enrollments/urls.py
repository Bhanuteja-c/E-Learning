from django.urls import path
from .views import EnrollView, ProgressView, MarkCompleteView

urlpatterns = [
    path('enroll/<int:course_id>/', EnrollView.as_view(), name='enroll'),
    path('progress/<int:course_id>/', ProgressView.as_view(), name='progress'),
    path('complete/<int:video_id>/', MarkCompleteView.as_view(), name='mark-complete'),
]