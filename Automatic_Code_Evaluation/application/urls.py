# from django.contrib import admin
from django.urls import path
from .evaluate import evaluator as ev1
from .evaluate2 import evaluator as ev2
# from application import views -- This is changed for below
from . import views

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact),
    path('evaluate/', ev1.executor),
    path('evaluate_code/', views.evaluate_code),
    path('evaluate_code_2/', views.evaluate_code2),
    path('evaluate2/', ev2.executor)
]
