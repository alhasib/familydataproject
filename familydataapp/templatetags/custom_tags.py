from django import template
register = template.Library()
from familydataapp.models import *
@register.filter  

def custom_filter(arg):
    # team = CrimeTeam.objects.get(name = arg)
    member = arg.member.all()
    print(member)
    return member