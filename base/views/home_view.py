import datetime
from django.db.models import Case, When, Value, IntegerField
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect

from base.models import ClassUnit, LearnerClass


@login_required(login_url='index')
@csrf_protect
def home(request):
    #Get current user and classes
    current_user = request.user

    try:
        classes = ClassUnit.objects.filter(user=current_user).order_by(
            Case(
            When(subject=28, then=Value(0)), #subject 28 = 'Register Class'
            When(subject=5, then=Value(9999)),default='subject',
            output_field=IntegerField(),
        )
        )
    except:
        classes = ClassUnit.objects.filter(user=current_user).order_by('subject')

    done_absentees = LearnerClass.objects.filter(classunit__user=current_user, created__date=datetime.date.today())
    date_today = datetime.date.today().strftime("%d/%b")
    

    #dictionary of subjects and learners per subject.
    home_list = []

    for a_class in classes:
        subject = a_class.subject
        grade = a_class.grade
        desc = a_class.description

        absentee_list = []
        absentees = LearnerClass.objects.filter(classunit=a_class, created__date=datetime.date.today())
        if absentees:
            for absentee in absentees:
                absentee_list.append(absentee.learner)
        else:
            absentee_list.append('-')

        home_list.append({'subject':subject, 'grade':grade, 'desc':desc, 'absentee_list':absentee_list})
        

    

    ##############################################################
    # Redirect to manage_absentees
    if request.method == 'POST' and request.POST.get('btnAbsentees'):
        return redirect('manage_absentees')
    
    ##############################################################
    #Redirect to manage_classes
    if request.method == 'POST' and request.POST.get('btnClasses'):
        return redirect('manage_classes')
    
    ##############################################################
    #Redirect to manage_stats
    if request.method == 'POST' and request.POST.get('btnStats'):
        return redirect('manage_stats')
    
    ##############################################################


    #Define the output context
    context = {'classes' : classes, 'current_user' : current_user, 'done_absentees' : done_absentees,\
               'date_today' : date_today, 'home_list': home_list}

    return render(request,'base/home.html', context)
    