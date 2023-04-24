from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django.http import *


def insert_student(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():

            si=SFDO.cleaned_data['sid']
            sn=SFDO.cleaned_data['sname']
            em=SFDO.cleaned_data['email']
            ph=SFDO.cleaned_data['phone']
            pe=SFDO.cleaned_data['percentage']
            re=SFDO.cleaned_data['remarks']
            #si=request.POST['sid']
            SO=Student.objects.get_or_create(sid=si,sname=sn,email=em,phone=ph,percentage=pe,remarks=re)[0]
            SO.save()

            return HttpResponse(' Data Inserted Successfully ')
    return render(request,'insert_student.html',d)




def insert_course(request):
    CFO=CourseForm()
    d={ 'CFO' : CFO }
    if request.method=='POST':
        CFDO=CourseForm(request.POST)
        if CFDO.is_valid():
            si=CFDO.cleaned_data['sid']
            ci=CFDO.cleaned_data['cid']
            co=CFDO.cleaned_data['Course']
            clg=CFDO.cleaned_data['college']
            CO=Course.objects.get_or_create(sid=si,cid=ci,Course=co,college=clg)[0]
            CO.save()
            return HttpResponse('Course data Inserted Successfully ')
    return render(request,'insert_course.html',d)