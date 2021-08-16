from django.urls import path
from familydataapp.views import *
from .views import *

urlpatterns = [
    path('my-admin/', admin_home, name="admin-home"),
    path('add-institute/', add_institute, name = 'add_institute'),
    path('add-crime-team/', add_crime_team, name = 'add_crime_team'),

    path('add-crime-type/', add_crime_type, name = 'add_crime_type'),


    path('add-crime-place/', add_crime_place,name='add_crime_place'),

    path('add-number/', add_number, name = 'add_number'),
    path('add-prayer-place/', add_prayer_place, name = 'add_prayer_place'),
    path('add-member/', add_member, name = 'add_member'),
    
]