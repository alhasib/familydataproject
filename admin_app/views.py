from django.shortcuts import render
from admin_app.forms import *
# Create your views here.
def admin_home(request):
    return render(request, 'admin/admin_home.html')


def add_member(request):
    if request.method == 'POST':
        print('jnfoi')
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Member Added Successfully!"
            forms = MemberForm()
            context = {'forms':forms, 'msg':msg}
            return render(request, 'admin/add_member.html', context)
         
    else:
        forms = MemberForm()
        context = {'forms':forms}
        return render(request, 'admin/add_member.html', context) 
    return render(request, 'admin/add_member.html')


def add_number(request):
    if request.method == 'POST':
        print('jnfoi')
        form = ImportantNumberForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Number Added Successfully!"
            forms = ImportantNumberForm()
            context = {'forms':forms, 'msg':msg}
            return render(request, 'admin/add_important_number.html', context)
         
    else:
        forms = ImportantNumberForm()
        context = {'forms':forms}
        return render(request, 'admin/add_important_number.html', context)
    return render(request, 'admin/add_important_number.html')


def add_prayer_place(request):
    if request.method == 'POST':
        
        form = PrayerplaceForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Prayer Place Added Successfully!"
            forms = PrayerplaceForm()
            context = {'forms':forms, 'msg':msg}
            return render(request, 'admin/add_prayer_place.html', context)
         
    else:
        forms = PrayerplaceForm()
        context = {'forms':forms}
        return render(request, 'admin/add_prayer_place.html', context)
    return render(request, 'admin/add_prayer_place')



def add_institute(request):
    if request.method == 'POST':
        form = InstitutionForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Prayer Place Added Successfully!"
            forms = InstitutionForm()
            context = {'forms':forms, 'msg':msg}
            return render(request, 'admin/add_institute.html', context)
         
    else:
        forms = InstitutionForm()
        context = {'forms':forms}
        return render(request, 'admin/add_institute.html', context)
    return render(request, 'admin/add_institute.html')


def add_crime_team(request):
    if request.method == 'POST':
        print('This is post view')
        form = CrimeTeamForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Crime Team Added Successfully!"
            forms = CrimeTeamForm()
            context = {'forms':forms, 'msg':msg}
            return render(request, 'admin/add_crime_team.html', context)
         
    else:
        forms = CrimeTeamForm()
        context = {'forms':forms}
        return render(request, 'admin/add_crime_team.html', context)
    return render(request, 'admin/add_crime_team.html')


def add_crime_type(request):
    if request.method == 'POST':
        form = CrimeTypeForm(request.POST)
        if form.is_valid():
            form = form.save()
            msg = "Crime Team Added Successfully!"
            context = {'form':form, 'msg':msg}
            return render(request, 'admin/add_crime_type.html', context)
    else:
        form = CrimeTypeForm()
        context = {'form':form}
        return render(request, 'admin/add_crime_type.html', context)
    
def add_crime_place(request):
    if request.method == 'POST':
        form = CrimePlaceForm(request.POST)
        if form.is_valid():
            form = form.save()
            msg = "Crime place Added Successfully!"
            form = CrimePlaceForm()
            context = {'form':form, 'msg':msg}
            return render(request, 'admin/add_crime_place.html', context)
    else:
        form = CrimePlaceForm()
        context = {'form':form}
        return render(request, 'admin/add_crime_place.html', context)