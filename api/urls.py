from django.urls import path
from .views import CustomUserView, CustomUserViewDetails, StudentView, StudentViewDetails, CourseView,CourseViewDetails, SessionTimeView, SessionTimeViewDetails

urlpatterns = [
    path('', CustomUserView.as_view()),
    path('', CustomUserViewDetails.as_view()),

    path('student/', StudentView.as_view()),
    path('student/<int:pk>', StudentViewDetails.as_view()),


    path('course/', CourseView.as_view()),
    path('course/<int:pk>', CourseViewDetails.as_view()),

    path('session/', SessionTimeView.as_view()),
    path('session/<int:pk>', SessionTimeViewDetails.as_view()),
]