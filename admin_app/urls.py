from django.urls import path
from familydataapp.views import *
from .views import *

urlpatterns = [
    path('my-admin/', admin_home),
    path('add-member/', add_member, name = 'add_member'),
    
]