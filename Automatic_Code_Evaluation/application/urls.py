from django.contrib import admin
from django.urls import path
from application.evaluate import evaluator
from application import views

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact),
    path('evaluate',evaluator.executor),
    path('evaluate_code',views.evaluate_code),
]
