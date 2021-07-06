from familydataapp.models import *
from django.forms import ModelForm
from django import forms
class MemberForm(ModelForm):
    blood_group = forms.ModelChoiceField(widget = forms.Select(attrs={'class':'ml-3 col-md-2 form-group custom-select form_field',}), queryset=BloodGroup.objects.all())
    district = forms.ModelChoiceField(widget = forms.Select(attrs={'class':'col-md-4 my-3 form-group custom-select form_field',}), queryset=District.objects.all())
    want_to_donate_blood = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-control checkbox',}))
    is_criminal = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-control checkbox',}))
    class Meta:
        model = Member
        fields = ['name','gender', 'marital_status',
                  'blood_group', 'father', 'mother', 'housband',
                  'national_id_number','mobile_number', 'date_of_birth',
                  'date_of_death', 
                  'last_date_of_blood_donation',
                  'district',
                  'address','is_criminal', 'want_to_donate_blood', 
                  ]
        
        widgets = {
            'name':forms.TextInput(attrs={'class':'mb-2 form-control form_field', 'placeholder':"Enter Name..."}),
            'father':forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Father's Name..."}),
            'mother':forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Mother's Name..."}),
            'housband':forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Housband's Name..."}),
            'national_id_number':forms.NumberInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Nation Id..."}),
            'mobile_number':forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Mobile Number..."}),
            'address':forms.TextInput(attrs={'class':'mb-2 form-control form_field', 'placeholder':"Enter Address..."}),
            'date_of_birth':forms.DateInput(attrs={'type': 'date', 'class':'col-md-4 mr-3 my-3 form-group custom-select datepicker form_field', 'placeholder':"Enter Date Of Birth..."}),
            'date_of_death':forms.DateInput(attrs={'type': 'date', 'class':'col-md-4 my-3 form-group custom-select datepicker form_field'}),
            'last_date_of_blood_donation':forms.DateInput(attrs={'type': 'date', 'class':'col-md-4 mr-3 my-3 form-group custom-select datepicker form_field'}),
            'marital_status':forms.Select(attrs={'class': 'mr-2 col-md-3 form-group custom-select form_field'}),
            'gender':forms.Select(attrs={'class': 'mr-2 col-md-3 form-group custom-select form_field'}),

        }

    
