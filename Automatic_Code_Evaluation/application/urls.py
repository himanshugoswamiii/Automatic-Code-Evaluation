from django.contrib import admin
from django.urls import path
from application.evaluate import evaluator
from application import views #Added by me

urlpatterns = [
    path('', views.index),
    path('evaluator', evaluator.executor),
    path('contact/', evaluator.contact),
    path('evaluate',evaluator.executor),
    path("submitcode/", views.submit_code,name='upload'),
    path("submitcode/upload", views.submit_code,name='upload'),
    path('testing/',evaluator.form)
]
