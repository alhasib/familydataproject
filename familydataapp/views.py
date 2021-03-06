from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required



@login_required(login_url='/')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/')
def search(request):
    if request.method == 'GET':
        print("hasib")
        search_value = request.GET.get('search')
        print(search_value)
        print(search_value.isnumeric())
        if search_value.isnumeric():
            try:
                search_data = Member.objects.filter(national_id_number__contains = search_value)
                context = {'search_data':search_data}
                return render(request, 'search_data.html', context)
            except:
                context = {'search_data':''}
                return render(request, 'search_data.html', context)
        # print(search_item)
        else:
            try:
                search_data = Member.objects.filter(name__contains = search_value)
                context = {'search_data':search_data}
                return render(request, 'search_data.html', context)
            except:
                context = {'search_data':''}
                return render(request, 'search_data.html', context)
    # return render(req)
    return render(request, 'search_data.html')

@login_required(login_url='/')
def profile_details(request, id):
    member = Member.objects.get(id = id)
    if member.father:
        father = Member.objects.get(id = member.father.id)
    else:
        father = None
    if member.mother:
        mother = Member.objects.get(id = member.mother.id)
    else:
        mother = None
    if father and mother:
        sibling = Member.objects.filter(father = father, mother = mother)
    elif father:
        sibling = Member.objects.filter(father = father)
    elif mother:
        sibling = Member.objects.filter(mother = mother)
    else:
        sibling = None
    
    chilrens = member.children_of_father.all()
    print(chilrens)
    wife = member.wives.all()
    print(father)
    print(mother)
    print(wife)
    print(sibling)
    context = {
        'member':member, 
        'father':father,
        'mother':mother,
        'sibling':sibling,
        'wife':wife,
        'chilrens':chilrens
      }
    return render(request, 'profile_details.html', context)


def dashboard(request):

    return render(request, 'dashboard.html')

@login_required(login_url='/')
def blood_doner(request):
    members = Member.objects.filter(
        want_to_donate_blood = True)
    
    b_group = request.GET.get('blood_group')
    if b_group:
        members = members.filter(
            blood_group__name_of_group = b_group)
        
    dist_name = request.GET.get('area')
    if dist_name:
        members = members.filter(
            district__name = dist_name)
    
    blood_groups = BloodGroup.objects.all()
    districts = District.objects.all()
    
    context = {
        'blood_groups':blood_groups,
        'districts':districts,
        'members':members,
        }
    
    return render(request, 'blood_doner.html', context)

    # if request.method == 'POST':
        
    #     print("hasib")
    #     b_group = request.POST['blood_group']
    #     dist_name = request.POST['area']
    #     context.update({'b_group':b_group, 'dist_name':dist_name})
    #     print(b_group)
    #     print(dist_name)

    #     try:
    #         b_group = blood_groups.get(name_of_group = b_group)
    #     except:
    #         b_group = None

    #     print(b_group)
        
    #     try:
    #         dist_name = districts.get(name__contains = dist_name)
    #     except:
    #         dist_name = None
    #     print(b_group)
    #     print(dist_name)

    #     if dist_name and b_group:
    #         try:
    #             members = Member.objects.filter(
    #                 blood_group__name_of_group = b_group, 
    #                 district__name = dist_name,
    #                 want_to_donate_blood = True)

    #             context['members'] = members
    #             return render(request, 'blood_doner.html', context)
    #         except:
    #             context['message'] = "No Data Found"
    #             return render(request, 'blood_doner.html', context)

    #     elif dist_name:
    #         print("dd")
    #         try:
    #             members = Member.objects.filter(
    #                 district__name = dist_name,
    #                 want_to_donate_blood = True)
    #             context['members'] = members
    #             return render(request, 'blood_doner.html', context)

    #         except:
    #             context['message'] = "No Data Found"
    #             return render(request, 'blood_doner.html', context)
                
    
    #     elif b_group:
    #         print(1)
    #         try:
    #             members = Member.objects.filter(
    #                 blood_group__name_of_group = b_group,
    #                 want_to_donate_blood = True)
            
    #             context['members'] = members
    #             return render(request, 'blood_doner.html', context)
        
    #         except:
    #             context['message'] = "No Data Found"
    #             return render(request, 'blood_doner.html', context)
    #     else:
    #         context['message'] = "No Data Found"
    #         return render(request, 'blood_doner.html', context)

    # members = Member.objects.filter(want_to_donate_blood = True)
    # context.update({'members':members})
    # return render(request, 'blood_doner.html', context)

import datetime
@login_required(login_url='/')
def marriagable_list(request):
    compare_date = datetime.datetime.now() - datetime.timedelta(days=25*365)
    member = Member.objects.filter(date_of_birth__lte = compare_date, marital_status = "S")
    print(member)
    # for member in member:
    #     print(member.gender)
    context = {'member':member}
    return render(request, 'marriagable_list.html', context)


@login_required(login_url='/')
def important_number(request):
    numbers = ImportantNumber.objects.all()
    context = {'numbers':numbers}
    return render(request, 'important_number.html', context)


@login_required(login_url='/')
def prayer_place(request, place):
    p_place = PrayerPlace.objects.filter(place_type = place)
    context = {'p_place':p_place, 'place':place}
    return render(request, 'prayer_place.html', context)


@login_required(login_url='/')
def institution(request,name):
    all_institution = Institution.objects.filter(institute_type = name)
    context = {'all_institution':all_institution, 'name':name}
    return render(request, 'institution.html', context)

from familydataapp.forms import*
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            return redirect('/home')
        else:
            msg = "Invalid Username Or passowrd"
            context = {'msg':msg}
            return render(request, 'login.html', context)
    # form = UserLoginForm()
    # context = {'form':form}
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/')
def crime_point(request):
    all_places = CrimePlace.objects.all()
    context = {'all_places':all_places}
    return render(request, 'crime_point.html', context)

@login_required(login_url='/')
def crime_team(request, id):
    place = CrimePlace.objects.get(id = id)
    teams = CrimeTeam.objects.filter(crime_location = place)
    # for i in teams:
    #     print(i.member.all())
    context = {'teams':teams}
    return render(request, 'crime_team.html', context)

@login_required(login_url='/')
def criminals(request):
    all_criminals = Member.objects.filter(is_criminal = True)
    context = {'all_criminals':all_criminals}
    return render(request, 'criminals.html', context)