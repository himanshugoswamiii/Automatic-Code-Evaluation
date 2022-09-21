from django.shortcuts import render
from pathlib import Path
import os
from django.http import HttpResponse
import requests as req
import application.testing.main

BASE_DIR = Path(__file__).resolve().parent.parent.parent # Modify no of parents according to this file's location

def code_submit(request):
    return render(request, "submit_code.html")

def form(request):
    return render(request,"testing.html")


# To upload the file
def executor(request):
    teacher = request.FILES['teachercode']
    student = request.FILES['student']
    testcase = request.FILES['testcase']
    basedir = os.path.join(BASE_DIR,'media/')
    #basedir = "/home/himanshu/Desktop/Automatic-Code-Evaluation/Automatic_Code_Evaluation/media"
    # with open(basedir + "/" + str(teacher.name), 'wb+') as dest:
    with open(basedir + str(teacher.name), 'wb+') as dest:
        for ch in teacher.chunks():
            dest.write(ch)
    # with open(basedir + "/" + str(testcase.name), 'wb+') as dest:
    with open(basedir + str(testcase.name), 'wb+') as dest:
        for ch in testcase.chunks():
            dest.write(ch)
    # with open(basedir + "/" + str(student.name), 'wb+') as dest:
    with open(basedir + str(student.name), 'wb+') as dest:
        for ch in student.chunks():
            dest.write(ch)
    return HttpResponse("Done")

def contact(request):
    return render(request, 'contact.html')


