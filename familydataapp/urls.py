
from django.urls import path
from .views import *


urlpatterns = [
    path('home', home),
    path('dashboard', dashboard, name = 'dashboard'),
    path('blood-doner/', blood_doner, name = 'blood-doner'),
    path('search', search, name = 'search'),
    path('profile_details/<int:id>', profile_details, name = 'profile_details')
]
