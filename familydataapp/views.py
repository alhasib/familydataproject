from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request, 'home.html')

def search(request):
    if request.method == 'GET':
        search_value = request.GET.get('search')
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

def blood_doner(request):
    
    # members = Member.objects.filter(blood_group = b_group)

    context = {'members':'members'}
    return render(request, 'blood_doner.html', context)