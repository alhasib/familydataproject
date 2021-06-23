from django.db import models

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

class Member(models.Model):
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
        on_delete=models.CASCADE, 
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
                              choices=(('M', 'Married'), ('s', 'Unmarried')),
                              blank=True,
                              null=True,
                              default=None)

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
    