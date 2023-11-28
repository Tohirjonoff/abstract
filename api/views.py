from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from app.models import CustomUser, Student, Course, Session_Time
from .serializers import CustomUserSerializer,StudentSerializer, CourseSerializer, SessionTimeSerializer

class CustomUserView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserViewDetails(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
class StudentView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentViewDetails(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class SessionTimeView(ListCreateAPIView):
    queryset = Session_Time.objects.all()
    serializer_class = SessionTimeSerializer

class SessionTimeViewDetails(RetrieveUpdateDestroyAPIView):
    queryset = Session_Time.objects.all()
    serializer_class = SessionTimeSerializer

class CourseView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseViewDetails(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer