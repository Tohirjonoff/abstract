from django.shortcuts import redirect,render
from app.models import Course

def BASE(request):

    return render(request,'base.html')

def HOME(request):
    course = Course.objects.all()
    context = {
        'course': course
    }
    return  render(request, 'Main/home.html', context=context)

def ABOUT(request):
    return  render(request, 'Main/about.html')

# def VIEWCOURSE(request):
#     course = Course.objects.all()
#     context = {
#         'course': course
#     }
#     return  render(request, 'admin/view_course.html', context=context)

