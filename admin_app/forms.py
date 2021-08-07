from familydataapp.models import *
from django.forms import ModelForm
from django import forms
class MemberForm(ModelForm):
    blood_group = forms.ModelChoiceField(widget = forms.Select(attrs={'class':'form-control form_field',}), queryset=BloodGroup.objects.all(), required=False)
    
    district = forms.ModelChoiceField(widget = forms.Select(attrs={'class':'form-control form_field',}), queryset=District.objects.all(), required=False)
    
    want_to_donate_blood = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-control checkbox',}))
    is_criminal = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-control checkbox',}), required=False)
    
    father = forms.ModelChoiceField(widget = forms.Select(attrs={'class':'form-control form_field',}), queryset=Member.objects.filter(gender = 'M'), required=False)
    
    housband = forms.ModelChoiceField(widget = forms.Select(attrs={'class':'form-control form_field',}), queryset=Member.objects.filter(gender = 'M'), required=False)
    
    mother = forms.ModelChoiceField(widget = forms.Select(attrs={'class':'form-control form_field',}), queryset=Member.objects.filter(gender = 'F'), required=False)

    
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
            
            'national_id_number':forms.NumberInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Nation Id..."}),
            
            'mobile_number':forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Mobile Number..."}),
            
            'address':forms.TextInput(attrs={'class':'mb-2 form-control form_field', 'placeholder':"Enter Address..."}),
            
            'date_of_birth':forms.DateInput(attrs={'type': 'date', 'class':'form-control form_field datepicker', 'placeholder':"Enter Date Of Birth..."}),
                                            
            'date_of_death':forms.DateInput(attrs={'type': 'date', 'class':'form-control form_field datepicker'}),
            
            'last_date_of_blood_donation':forms.DateInput(attrs={'type': 'date', 'class':'form-control form_field datepicker'}),
            'marital_status':forms.Select(attrs={'class': 'form-control form_field'}),
            
            'gender':forms.Select(attrs={'class': 'form-control form_field'}),

        }
        
        

class ImportantNumberForm(ModelForm):
    
    class Meta:
        model = ImportantNumber
        fields = ['officer_name', 'mobile_number', 'designation',]
        
        widgets = {
                        'officer_name':forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Officer Name..."}),
                        
                        'mobile_number':forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Mobile Number..."}),
                        
                        'designation':forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Designation..."}),

        }


    
class PrayerplaceForm(ModelForm):
    class Meta:
        model = PrayerPlace
        fields = ['place_name','place_type', 'chairman', 'vice_chairman', 'responsible_person_one', 'responsible_person_two','responsible_person_three', 'responsible_person_four']
        
        widgets = {
            'place_type':forms.Select(attrs={'class': 'form-control form_field'}),
            'place_name': forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Place Name..."}),
            
            'chairman': forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Chairnam Name..."}),
            
            'vice_chairman': forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Vice Chairman Name..."}),
            
            'responsible_person_one': forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Responsible Person One Name..."}),
            
            'responsible_person_two': forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Responsible Person Two Name..."}),
            
            'responsible_person_three': forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Responsible Person three Name..."}),
            
            'responsible_person_four': forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Responsible One Four..."}),
        }
        
        
        
class InstitutionForm(ModelForm):
    
    class Meta:
        model = Institution
        fields = ['institute_type', 'name', 'head_of_institution','head_contact_number','institution_contact_number','location']
        
        widgets = {
                        'institute_type':forms.Select(attrs={'class': 'form-control form_field'}),
                        
                        'head_of_institution':forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Head Of Institution..."}),
                        
                        'head_contact_number':forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Head Contact Number..."}),

                        'name':forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Institute name..."}),
                        
                        'institution_contact_number':forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Institute Number..."}),
                        
                        'location':forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Location..."}),

        }


class CrimeTeamForm(ModelForm):
    
    class Meta:
        model = CrimeTeam 
        fields = ['crime_type','crime_location','member']
        
        widgets = {
                'crime_type':forms.Select(attrs={'class': 'form-control form_field'}),
                
                'member':forms.SelectMultiple(attrs = {
                    'class':"form-control form_field"
                }),
              
                'crime_location':forms.SelectMultiple(attrs={'class':'form-control form_field', 'placeholder':"Enter Location..."}),

                }



class CrimePlaceForm(ModelForm):
    
    class Meta:
        model = CrimePlace
        fields = ['location', 'near_identity_one', 'near_identity_two','near_identity_three','near_identity_four',]
        
        widgets = {
                        
                    'near_identity_four':forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Near Identity One..."}),
                    
                    'near_identity_one':forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Near Identity One..."}),

                    'near_identity_two':forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Near Identity One..."}),
                    
                    'near_identity_three':forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Near Identity One..."}),

                        
                    'location':forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Location..."}),

        }

class CrimeTypeForm(ModelForm):

    class Meta:
        model = CrimeType
        fields = ['name']
        
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control form_field', 'placeholder':"Enter Crime Type..."}),

        }

