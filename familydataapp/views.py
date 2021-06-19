from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def search(request):
    if request.method == 'GET':
        search_item = request.GET.get('search')
        print(search_item)

    # return render(req)