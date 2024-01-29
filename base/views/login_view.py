from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password


def index(request):
    
    if request.method == 'POST':
        #Get teacher code input
        teacherCode = request.POST.get('teacher_code')
        teacherPass = request.POST.get('teacher_pass')
        #registerCode = request.POST.get('register_code').upper()

        if request.POST.get('btnLogin'):
            #Check if teacher code exists
            
            try:
                teacher = User.objects.get(username=teacherCode,password=teacherPass)
            except User.DoesNotExist:
                messages.warning(request, "Teacher code or password is incorrect")
                teacher = None

            
            if teacher is not None:
                login(request, teacher)
                return redirect('home')
            
            
        newTeacherCode = request.POST.get('register_code').upper()
        newTeacherPass = request.POST.get('newteacher_pass')      
        #Create new teacher code   
        if request.POST.get('btnRegister') and newTeacherCode is not None and newTeacherPass is not None:
            
            try:
                new_user = User.objects.create_user(username=newTeacherCode, password=newTeacherPass)
            except Exception as e:
                messages.error(request, "User already exists, logged in with that code")

            try:    
                user = authenticate(request, username=newTeacherCode, password=newTeacherPass)
                
                login(request, user)
                return redirect('home')
            except Exception as e:
                messages.error(request,e)

            
                
             

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