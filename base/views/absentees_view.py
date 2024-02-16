from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
import datetime

from base.models import ClassUnit, Learner, LearnerClass


@login_required(login_url='index')
def manage_absentees(request):
    #Current User
    current_user = request.user

    #Get classes for current user
    classes = ClassUnit.objects.filter(user=current_user).order_by('subject')

    #initialize double lesson to false
    double_lesson = False
    
    #Process inputs
    if request.method == 'POST':

        date_absentee = request.POST.get('absentee_date_old')
        
        if date_absentee == '':            
            date_absentee = (datetime.date.today()) 
            print(date_absentee) 
  
        #Get selected class
        try:
            selected_class = request.POST.get('classid')
            selected_class = ClassUnit.objects.get(id=selected_class)
        except:
            selected_class = None
            #No class selected, return to screen
            messages.error(request, 'Please select a class')
            context = {'current_user' : current_user, 'classes' : classes}
            return render (request, 'base/manage_absentees.html', context)

        #Get lesson number
        if selected_class.subject.subject == 'Register Class':
            lessonnum = 'Register Class'
            double_lesson = '0'
        elif selected_class.subject.subject =='LO':
            lessonnum = 'LO'
            double_lesson = '0'
        else:
            lessonnum = request.POST.get('lessonNumber')
            double_lesson = request.POST.get('double_check')

        #double lesson only valid if numbered lesson       
        if double_lesson == '1':
            if lessonnum in ['1', '2', '3', '4', '5', '6', '7', '8']:
                lessonnum = f"{lessonnum} + {int(lessonnum)+1}"
            else:
                lessonnum= f"{lessonnum}"
        else:
            lessonnum= f"{lessonnum}"
        
        #btnSubmitAbsentees
            #
        if request.POST.get('btnSubmitAbsentees') and selected_class is not None and lessonnum is not None:
            classpk = selected_class.id
            return redirect('submit_absentees', classpk=classpk, lessonnum=lessonnum, date_absentee=date_absentee) #old_date add to param
        elif not selected_class:
            messages.error(request, 'Please select a class')


    #Context
    context = {'current_user' : current_user, 'classes' : classes}

    return render (request, 'base/manage_absentees.html', context)

##############################################################################