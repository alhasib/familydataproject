from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Member)
admin.site.register(Profession)
admin.site.register(BloodGroup)
admin.site.register(Division)
admin.site.register(District)
admin.site.register(ImportantNumber)
admin.site.register(PrayerPlace)
admin.site.register(Institution)
admin.site.register(CrimePlace)
admin.site.register(CrimeType)
admin.site.register(CrimeTeam)
