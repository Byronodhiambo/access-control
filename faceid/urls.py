from django.urls import path
from .views import *

urlpatterns = [
    path('', users.as_view(), name='users'),
    path('images', ImageProcessing.as_view(), name='images'),
    path('enroll', EnrolUser.as_view(), name='enroll'),
    
]
