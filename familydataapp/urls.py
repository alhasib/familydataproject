
from django.urls import path
from .views import *


urlpatterns = [
    path('home', home),
    path('dashboard', dashboard, name = 'dashboard'),
    path('login', user_login, name = 'user_login'),
    path('logout', user_logout, name = 'user_logout'),
    path('Institution/<name>', institution, name = 'institution'),
    path('prayer-place/<place>', prayer_place, name = 'prayer-place'),
    path('important-number', important_number, name = 'important_number'),
    path('marriagable-list', marriagable_list, name = 'marriagable-list'),
    path('blood-doner/', blood_doner, name = 'blood-doner'),
    path('search', search, name = 'search'),
    path('profile_details/<int:id>', profile_details, name = 'profile_details')
]
