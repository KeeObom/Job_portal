from django.urls import path 
# now import the views.py file into this code
from .views import cv_upload

app_name = "jobs"

urlpatterns = [
    path('cv-upload/', cv_upload, name='cv_upload'),
]
