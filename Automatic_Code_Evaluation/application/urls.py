from django.contrib import admin
from django.urls import path
from application.evaluate import evaluator
from application import views #Added by me

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('evaluator', evaluator.executor),
    path('contact/', evaluator.contact),
    path('evaluate',evaluator.executor),
    path('submit_code/', views.submit_code),
    path('upload', views.submit_code),
    path('testing/',evaluator.form)
]

# File Handling
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
