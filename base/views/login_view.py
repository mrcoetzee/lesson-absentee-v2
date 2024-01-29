from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def index(request):
    
    if request.method == 'POST':

        if request.POST.get('btnLogin'):
            #Get teacher code input
            teacherCode = request.POST.get('teacher_code')
            teacherPass = request.POST.get('teacher_pass')

            #Check if teacher code exists            
            teacher = authenticate(request,username=teacherCode,password=teacherPass)
            
            if teacher is None:
                messages.warning(request, "Teacher code or password is incorrect")
            elif teacher is not None:
                login(request, teacher)
                return redirect('home')
            
            
        '''      
        #Create new teacher code   
        if request.POST.get('btnRegister') and newTeacherCode is not None and newTeacherPass is not None:

            newTeacherCode = request.POST.get('register_code').upper()
            newTeacherPass = request.POST.get('newteacher_pass')
            
            try:
                new_user = User.objects.create_user(username=newTeacherCode, password=newTeacherPass)
            except IntegrityError:
                messages.error(request, "User already exists, logged in with that code"))
            except Exception as e:
                messages.error(request, f"an error occured: {e}")

                
            user = authenticate(request, username=newTeacherCode, password=newTeacherPass)
            if user is not None:
                try:    
                    login(request, user)
                    return redirect('home')
                except Exception as e:
                    messages.error(request,f"an error occured: {e}")
            elif user is None:
                messages.error(request, "Teacher code or password is incorrect")
        '''
            
    return render(request,'base/login.html')
    

##############################################################################

def logout_user(request):
    logout(request)
    return redirect('index')

'''
def index(request):

    if request.method == 'POST':
        #Get teacher code input
        teacherCode = request.POST.get('teacher_code')

        new_user = User.objects.create_user(username=teacherCode)

    return render(request,'base/login.html')
    '''