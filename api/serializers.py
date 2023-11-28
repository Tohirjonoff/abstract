from rest_framework import serializers
from app.models import CustomUser, Student, Session_Time, Course

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'user_type', 'username', 'profile_pic','first_name', 'last_name')
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('admin', 'course_id', 'address', 'gender', 'session_id', 'created_at', 'updated_at')
class SessionTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session_Time
        fields = ('sesstion_start', 'sesstion_end')
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'created_ad', 'updated_ad')
