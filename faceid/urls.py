from django.urls import path
from .views import *

urlpatterns = [
    path('', users.as_view(), name='users')
    
]
