from django.shortcuts import render
from django.http import HttpResponse
import requests as req
import application.testing.main

def code_submit(request):
    return render(request, "submit_code.html")

def form(request):
    return render(request,"testing.html")


def executor(request):
    teacher = request.FILES['teachercode']
    student = request.FILES['student']
    testcase = request.FILES['testcase']
    basedir = "/home/aniket/PycharmProjects/Automatic-Code-Evaluation"
    with open(basedir + "/" + str(teacher.name), 'wb+') as dest:
        for ch in teacher.chunks():
            dest.write(ch)
    with open(basedir + "/" + str(testcase.name), 'wb+') as dest:
        for ch in testcase.chunks():
            dest.write(ch)
    with open(basedir + "/" + str(student.name), 'wb+') as dest:
        for ch in student.chunks():
            dest.write(ch)
    return HttpResponse("Done")







def contact(request):
    return render(request, 'contact.html')


