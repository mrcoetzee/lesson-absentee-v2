from django.contrib import admin
from .models import Subject, Grade, ClassUnit, LearnerClass, Learner

# Register your models here.

class LearnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'grade', 'reg_class')  # Customize the fields to be displayed in the list view
    search_fields = ('name', 'reg_class', 'grade__grade')  # Enable searching for these fields

class LearnerClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'learner', 'classunit','created', 'lesson_no')  # Customize the fields to be displayed in the list view
    search_fields = ('created', 'lesson_no', 'classunit__subject__subject', 'classunit__grade__grade', 'learner__name')  # Enable searching for these fields

class ClassUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'grade', 'description', 'user', 'created' )  # Customize the fields to be displayed in the list view
    search_fields = ('subject__subject', 'grade__grade', 'description', 'user__username', 'created' )  # Enable searching for these fields

#admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(ClassUnit, ClassUnitAdmin)
admin.site.register(LearnerClass, LearnerClassAdmin)
admin.site.register(Learner, LearnerAdmin)





