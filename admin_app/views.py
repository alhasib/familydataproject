from django.shortcuts import render
from admin_app.forms import *
# Create your views here.
def admin_home(request):
    return render(request, 'admin/admin_home.html')


def add_member(request):
    if request.method == 'POST':
        pass 
    else:
        forms = MemberForm()
        context = {'forms':forms}
        return render(request, 'admin/add_member.html', context) 
    return render(request, 'admin/add_member.html')