import csv, datetime

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models import Q


from base.models import LearnerClass

@login_required(login_url='index')
def manage_stats(request):

    currentuser=request.user

    context= {'current_user':currentuser}
    return render(request, 'base/manage_stats.html', context)

def download_csv_all(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="all_data.csv"'

    # Create a CSV writer and write the header
    writer = csv.writer(response)
    writer.writerow(['Lesson No','Learner', 'Teacher','Subject', 'Grade', 'Description', 'Date/Time'])  # Replace with your model fields

    # Query the data from the model and write to the CSV file
    
    queryset = LearnerClass.objects.all().order_by('-created')  # Replace with your actual model
    for obj in queryset:
        lesson_no = obj.lesson_no
        created = obj.created.strftime('%Y-%m-%d')
        learner = obj.learner if obj.learner else 'no_learner' 
        teacher = obj.classunit.getusername() if obj.classunit else 'no_teacher'
        subject = obj.classunit.subject if obj.classunit else 'no_subject'
        grade = obj.learner.grade if obj.learner else 'no_grade'
        description = obj.classunit.description if obj.classunit else ''


        writer.writerow([lesson_no, learner, teacher, subject, grade, description, created])
        
    return response

def download_csv_today(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="all_data.csv"'

    # Create a CSV writer and write the header
    writer = csv.writer(response)
    writer.writerow(['Lesson No','Learner', 'Teacher','Subject', 'Grade', 'Description', 'Date/Time'])  # Replace with your model fields

    # Query the data from the model and write to the CSV file
    queryset = LearnerClass.objects.filter(created__date=datetime.date.today()).exclude(lesson_no='Register Class').order_by('-created')  # Replace with your actual model
    for obj in queryset:
        lesson_no = obj.lesson_no
        created = obj.created.strftime('%Y-%m-%d')
        learner = obj.learner if obj.learner else 'no_learner' 
        teacher = obj.classunit.getusername() if obj.classunit else 'no_teacher'
        subject = obj.classunit.subject if obj.classunit else 'no_subject'
        grade = obj.learner.grade if obj.learner else 'no_grade'
        description = obj.classunit.description if obj.classunit else ''


        writer.writerow([lesson_no, learner, teacher, subject, grade, description, created])
        
    return response

#Today's morning absentees
def morning_absentees_today(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="morning_absentees_today.csv"'

    # Create a CSV writer and write the header
    writer = csv.writer(response)
    writer.writerow(['Lesson No', 'Learner', 'Teacher','Subject', 'Grade', 'Description', 'Date/Time'])  # Replace with your model fields

    # Query the data from the model and write to the CSV file
    queryset = LearnerClass.objects.filter(created__date=datetime.date.today(),lesson_no='Register Class').order_by('-created')  # Replace with your actual model
    for obj in queryset:
        lesson_no = obj.lesson_no
        created = obj.created.strftime('%Y-%m-%d')
        learner = obj.learner if obj.learner else 'no_learner' 
        teacher = obj.classunit.getusername() if obj.classunit else 'no_teacher'
        subject = obj.classunit.subject if obj.classunit else 'Register Class'
        grade = obj.learner.grade if obj.learner else 'no_grade'
        description = obj.classunit.description if obj.classunit else 'no_description'


        writer.writerow([lesson_no, learner, teacher, subject, grade, description, created])
        
    return response

#Any morning absentees
def morning_absentees_any(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="morning_absentees_any.csv"'

    datepicker = request.GET.get('absenteeDate') 
    print(datepicker)
    #datepicker = datetime.datetime.strptime(datepicker, '%Y-%m-%d')
 


    # Create a CSV writer and write the header
    writer = csv.writer(response)
    writer.writerow(['Lesson No', 'Learner', 'Teacher','Subject', 'Grade', 'Description', 'Date/Time'])  # Replace with your model fields

    # Query the data from the model and write to the CSV file
    queryset = LearnerClass.objects.filter(created__date=datepicker,lesson_no='Register Class').order_by('-created')  # Replace with your actual model
    for obj in queryset:
        lesson_no = obj.lesson_no
        created = obj.created.strftime('%Y-%m-%d')
        learner = obj.learner if obj.learner else 'no_learner' 
        teacher = obj.classunit.getusername() if obj.classunit else 'no_teacher'
        subject = obj.classunit.subject if obj.classunit else 'Register Class'
        grade = obj.learner.grade if obj.learner else 'no_grade'
        description = obj.classunit.description if obj.classunit else 'no_description'


        writer.writerow([lesson_no, learner, teacher, subject, grade, description, created])
        
    return response

#Any lesson absentees
def lesson_absentees_any(request):
    datepicker = request.GET.get('absenteeDate')
                                 
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="morning_absentees_{datepicker}.csv"'

     

    # Create a CSV writer and write the header
    writer = csv.writer(response)
    writer.writerow(['Lesson No','Learner', 'Teacher','Subject', 'Grade', 'Description', 'Date/Time'])  # Replace with your model fields

    # Query the data from the model and write to the CSV file
    queryset = LearnerClass.objects.filter(created__date=datepicker).exclude(lesson_no='Register Class').order_by('-created')  # Replace with your actual model
    for obj in queryset:
        lesson_no = obj.lesson_no
        created = obj.created.strftime('%Y-%m-%d')
        learner = obj.learner if obj.learner else 'no_learner' 
        teacher = obj.classunit.getusername() if obj.classunit else 'no_teacher'
        subject = obj.classunit.subject if obj.classunit else 'no_subject'
        grade = obj.learner.grade if obj.learner else 'no_grade'
        description = obj.classunit.description if obj.classunit else ''


        writer.writerow([lesson_no, learner, teacher, subject, grade, description, created])
        
    return response
