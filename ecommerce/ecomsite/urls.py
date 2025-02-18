from django.urls import path
from .views import student_form
 
urlpatterns = [
    path('', student_form, name='student-form'),
]