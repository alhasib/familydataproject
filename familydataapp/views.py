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
    father = Member.objects.get(id = member.father.id)
    mother = Member.objects.get(id = member.mother.id)
    sibling = Member.objects.filter(father = father, mother = mother)
    print(father)
    print(mother) 
    print(sibling)
    context = {'member':member, 'father':father, 'mother':mother, 'sibling':sibling}
    return render(request, 'profile_details.html', context)