import datetime

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
import csv
from django.http import HttpResponse
# Create your models here.

'''
class Teacher(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=100, null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)


    def is_authenticated(self):
        return True  # Always returns True for user objects

    def __str__(self):
        return self.code
'''
class Subject(models.Model):
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.subject
    def get_name(self):
        return self.subject


class Grade(models.Model):
    grade = models.SmallIntegerField()

    def __str__(self):
        return str(self.grade)

class ClassUnit(models.Model):
    description = models.TextField(null=True, blank=True, default='Key 7 or class 9E')
    created = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    #teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        teacher_str= self.user.username if self.user else 'no teacher'
        return f"{self.subject.subject} {self.grade} {teacher_str}"
        #return self.subject.subject + ' ' + self.user.username + ' ' + str(self.grade)
    
    def getusername(self):
        teacher_str= self.user.username if self.user else 'no teacher'
        return f"{teacher_str}"




class Learner(models.Model):
    name = models.CharField(max_length=150)
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True)
    reg_class = models.CharField(max_length=3, null=True)

    def __str__(self):
        return self.name


class LearnerClass(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    classunit = models.ForeignKey(ClassUnit, on_delete=models.SET_NULL, null=True)
    learner = models.ForeignKey(Learner, on_delete=models.SET_NULL, null=True)
    lesson_no=models.CharField(max_length=1, null=True)


    def __str__(self):
        return f"{self.classunit} {self.learner.name} | \
              {self.created.strftime('%d-%m-%Y')}"
    



    


