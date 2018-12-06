from django.db import models


# Create your models here.
class CourseManager(models.Manager):
    def validate(self, form):
        errors = []
        if len(form['course_name'])<2:
            errors.append('Courses name must be longer than 1 Characters')
        if len(form['teacher'])<2:
            errors.append('Teachers name must be longer than 1 Characters')
        if len(form['description'])<6:
            errors.append('Course description must be longer than 5 Characters')
        return errors

    def save_course(self, form, cap_teacher):
        new_teacher = Teacher.objects.get(t_name=cap_teacher)
        new_course = self.create(
            name = form['course_name'],
            teacher = new_teacher,
            description = form['description'],
        )
        return new_course

    def save_teacher(self, form, cap_teacher):
        if len(Teacher.objects.filter(t_name=cap_teacher)) == 0:
            print('Adding teacher')
            new_teacher = self.create(
                t_name = form['teacher'].capitalize()
            )
            return new_teacher
        print('did not add teacher')
        return Teacher.objects.get(t_name=cap_teacher).id


class Teacher(models.Model):
    t_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

    def __str__(self):
        string = f'{self.t_name}'
        return string


class Course(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, related_name='courses')
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

    def __str__(self):
        string = f'{self.name}: taught by: {self.teacher} {self.description}'
        return string

