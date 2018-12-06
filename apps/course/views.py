from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Teacher, Course

# Create your views here.
def index(request):
    context = {
        'classes':Course.objects.all()
    }
    return render(request, 'course/index.html', context)

def delete(request, id):
    course = Course.objects.get(id=id)
    context={'id':id,
             'name': course.name,
             'desc': course.description,
             }
    return render(request, 'course/delete.html', context)

def process(request):
    errors = Course.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
    else:
        print(type(request.POST['teacher']))
        cap_teacher = request.POST['teacher'].capitalize()
        # request.POST['teacher'] = cap_teach
        new_teacher = Teacher.objects.save_teacher(request.POST, cap_teacher)
        new_course = Course.objects.save_course(request.POST, cap_teacher)

    return redirect('/course/index/')

def deleted(request, id):
    course_class = Course.objects.get(id=id)
    course_class.delete()
    return redirect('/course/index/')
