import csv, datetime

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.template.loader import render_to_string

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
    writer.writerow(['Learner', 'Teacher','Subject', 'Grade', 'Description', 'Date/Time'])  # Replace with your model fields

    # Query the data from the model and write to the CSV file
    queryset = LearnerClass.objects.all().order_by('-created')  # Replace with your actual model
    for obj in queryset:
        created = obj.created
        learner = obj.learner if obj.learner else 'no_learner' 
        teacher = obj.classunit.getusername() if obj.classunit else 'no_teacher'
        subject = obj.classunit.subject if obj.classunit else 'no_subject'
        grade = obj.learner.grade if obj.learner else 'no_grade'
        description = obj.classunit.description if obj.classunit else ''


        writer.writerow([learner, teacher, subject, grade, description, created])
        
    return response

def download_csv_today(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="all_data.csv"'

    # Create a CSV writer and write the header
    writer = csv.writer(response)
    writer.writerow(['Learner', 'Teacher','Subject', 'Grade', 'Description', 'Date/Time'])  # Replace with your model fields

    # Query the data from the model and write to the CSV file
    queryset = LearnerClass.objects.filter(created__date=datetime.date.today()).order_by('-created')  # Replace with your actual model
    for obj in queryset:
        created = obj.created
        learner = obj.learner if obj.learner else 'no_learner' 
        teacher = obj.classunit.getusername() if obj.classunit else 'no_teacher'
        subject = obj.classunit.subject if obj.classunit else 'no_subject'
        grade = obj.learner.grade if obj.learner else 'no_grade'
        description = obj.classunit.description if obj.classunit else ''


        writer.writerow([learner, teacher, subject, grade, description, created])
        
    return response
