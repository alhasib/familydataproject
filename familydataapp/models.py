from django.db import models
from django.contrib.auth.models import *
# Create your models here.
class Profession(models.Model):
    name = models.CharField(max_length = 250, blank = True, null = True)

    def __str__(self):
        return self.name
    

class MemberChoices:
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    
    CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Others')
    )

class Division(models.Model):
    name = models.CharField(max_length = 250)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length = 250)
    division = models.ForeignKey(Division, on_delete = models.SET_NULL, blank = True, null = True)

    def __str__(self):
        return self.name

class BloodGroup(models.Model):
    
    name_of_group = models.CharField(max_length = 250)

    def __str__(self):
        return self.name_of_group


class CrimePlace(models.Model):
    location = models.CharField(max_length = 250)
    near_identity_one = models.CharField(max_length = 250, blank = True, null = True)
    near_identity_two = models.CharField(max_length = 250, blank = True, null = True)
    near_identity_three = models.CharField(max_length = 250, blank = True, null = True)
    near_identity_four = models.CharField(max_length = 250, blank = True, null = True)

    def __str__(self):
        return self.location


class CrimeType(models.Model):
    name = models.CharField(max_length = 250)

    def __str__(self):
        return self.name

class CrimeTeam(models.Model):
    crime_type = models.ForeignKey(CrimeType, 
    on_delete = models.SET_NULL,
    blank = True,
    null = True,)
    crime_location = models.ManyToManyField(CrimePlace, related_name = 'team_in_here')
    member = models.ManyToManyField('Member')

    def __str__(self):
        return str(self.crime_type)

class Member(models.Model):
    # crime_point = 
    user = models.OneToOneField(User, 
                                    on_delete = models.SET_NULL,
                                    blank = True,
                                    null = True,
                                    related_name="member")
    is_criminal = models.BooleanField(default = False,
                                      blank = True,
                                      null = True)
    
    photo = models.ImageField(blank = True, null = True)
    name = models.CharField(
                            max_length=250, 
                            blank=True,
                            null=True)
    gender = models.CharField(max_length=1,
                              choices=MemberChoices.CHOICES,
                              blank=True,
                              null=True,
                              default=MemberChoices.MALE)

    father = models.ForeignKey(
        "self", on_delete=models.SET_NULL, 
        blank=True, null = True,
        limit_choices_to={'gender': 'M'},
        related_name='children_of_father')

    mother = models.ForeignKey('self',
                               blank=True,
                               null=True,
                               on_delete=models.SET_NULL,
                               default = None,
                               limit_choices_to={'gender': 'F'},
                               related_name='children_of_mother')

    housband = models.ForeignKey(
        "self", 
        on_delete=models.SET_NULL, 
        blank=True, null = True, 
        limit_choices_to={'gender': 'M'},
        related_name='wives')

    address = models.CharField(
        max_length = 250, 
        blank = True, 
        null = True)
    national_id_number = models.IntegerField(
        blank = True, 
        null = True)

    date_of_birth = models.DateField(
        blank=True, 
        null = True)
    date_of_death = models.DateField(blank = True, null = True, default = None)
    marital_status = models.CharField(max_length=1,
                              choices=(('M', 'Married'), ('S', 'Unmarried')),
                              blank=True,
                              null=True,
                              default=None)
    want_to_donate_blood = models.BooleanField(blank = True, null = True, default = True)

    blood_group = models.ForeignKey(
                            'BloodGroup',
                            on_delete = models.SET_NULL,
                            blank=True,
                            null=True,
                            default=None,
                            )
    last_date_of_blood_donation = models.DateField(
        blank = True,
        null = True,
    )
    mobile_number = models.CharField(max_length = 250, blank = True, null = True)

    district = models.ForeignKey(District, on_delete = models.SET_NULL, blank = True, null
     = True)
    


    @property
    def member_age(self):
        if self.date_of_birth:

            date = self.date_of_birth.strftime('%Y-%m-%d')
            date = date.split('-')
            start_date = int(date[2]) 
            start_month = int(date[1]) 
            start_year = int(date[0])

            end_date = 0
            end_month = 0
            end_year = 0

            if self.date_of_death:
                death_date = self.date_of_death.strftime('%Y-%m-%d')
                death_date = death_date.split('-')

                end_date = int(death_date[2])
                end_month = int(death_date[1])
                end_year = int(death_date[0])
            else:
                from datetime import datetime
                death_date = datetime.today().strftime('%Y-%m-%d')
                death_date = death_date.split('-')

                end_date = int(death_date[2])
                end_month = int(death_date[1])
                end_year = int(death_date[0])

            year = 0 

            month = 0 

            date = 0 


            if int(end_date) >= int(start_date):
                date = int(end_date) - int(start_date)
                
            elif int(end_date) < int(start_date):
                date = (int(end_date) + 30) - int(start_date)
                start_month += 1 


            if int(end_month) >= int(start_month):
                month = int(end_month) - int(start_month)
                
            elif int(end_month) < int(start_month):
                month = (int(end_month) + 12) - int(start_month) 
                start_year += 1 
                
            year = int(end_year) - int(start_year)

            context = str(year) + " years " + str(month) + str('month ') + str(date) + ' days'
            return context
        else:
            return None

    def __str__(self):
        return self.name
    

class ImportantNumber(models.Model):
    officer_name = models.CharField(max_length = 250)
    mobile_number = models.CharField(max_length = 12)
    # office_name = models.CharField(max_length = 250)
    designation = models.CharField(max_length = 250)

    def __str__(self):
        return self.officer_name


class PrayerPlace(models.Model):
    place_name = models.CharField(max_length = 250)
    place_type = models.CharField(choices=(('Mandir', 'Mandir'), ('Masjid', 'Masjid')),
    max_length = 250,
    )
    chairman = models.CharField(
        max_length = 250,
        blank = True,
        null = True
    )
    vice_chairman = models.CharField(
        max_length = 250,
        blank = True,
        null = True,
    )
    responsible_person_one = models.CharField(
        max_length = 250,
        blank = True,
        null = True,
    )
    responsible_person_two = models.CharField(
        max_length = 250,
        blank = True,
        null = True,
    )
    responsible_person_three = models.CharField(
        max_length = 250,
        blank = True,
        null = True,
    )
    responsible_person_four = models.CharField(
        max_length = 250,
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.place_name

class Institution(models.Model):
    institute_type = models.CharField(
    max_length = 250,
    choices=(('School', 'School'),
     ('College', 'College'),
     ('Madrasha', 'Madrasha'),
     ('University', 'University'),
     ('Kindergarten', 'Kindergarten'),
     ))

    name = models.CharField(max_length = 250, blank = True,
    null = True)
    head_of_institution = models.CharField(max_length = 250, blank = True,
    null = True)
    head_contact_number = models.CharField(max_length = 250, blank = True,
    null = True)
    institution_contact_number = models.CharField(max_length = 250, blank = True,
    null = True)
    location = models.CharField(max_length = 250, blank = True,
    null = True)

    def __str__(self):
        return self.name 
