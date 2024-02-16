from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('logout_user/', views.logout_user, name="logout_user"),

    path('home/',views.home, name="home"),

    path('manage_absentees/', views.manage_absentees, name="manage_absentees"),
    path('submit_absentees/<str:classpk>/<str:lessonnum>/<str:date_absentee>/', views.submit_absentees, name="submit_absentees"),

    path('manage_stats/', views.manage_stats, name="manage_stats"),

    path('manage_classes/', views.manage_classes, name="manage_classes"),
    path('add_class/', views.add_class, name="add_class"),


    path('ajax/autocomplete/', views.autocomplete, name='autocomplete'),
    path('ajax/delete_item/', views.deleteitem, name='deleteitem'),
    path('ajax/download_csv_all/', views.download_csv_all, name='download_csv_all'),
    path('ajax/download_csv_today/', views.download_csv_today, name='download_csv_today'),
    path('ajax/morning_absentees_today/', views.morning_absentees_today, name='morning_absentees_today'),
    path('ajax/morning_absentees_any/', views.morning_absentees_any, name='morning_absentees_any'),
    path('ajax/lesson_absentees_any/', views.lesson_absentees_any, name='lesson_absentees_any')
    
    

  
    #path('Logout/', views.logoutUser, name='Logout'),
    #path('manageclasses/', views.manageclasses, name="manageclasses"),
   #path('addclass/', views.addClass, name="addclass"),
    #path('absentees/<str:pk>/', views.absentees, name="absentees")
]
