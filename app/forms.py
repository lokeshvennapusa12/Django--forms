from django import forms
from app.models import *

class StudentForm(forms.Form):
    sid=forms.IntegerField()
    sname=forms.CharField(max_length=100)
    email=forms.EmailField()
    phone=forms.IntegerField()
    percentage=forms.IntegerField()
    remarks=forms.CharField(max_length=4)

class CourseForm(forms.Form):
    sid=forms.IntegerField()
    cid=forms.IntegerField()
    Course=forms.CharField(max_length=100)
    college=forms.CharField(max_length=100)

