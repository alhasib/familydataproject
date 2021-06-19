from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    gender = models.CharField(max_length=1,
                              choices=(('M', 'Male'), ('F', 'Female')),
                              blank=True,
                              null=True,
                              default=None)
    father = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null = True,
                               limit_choices_to={'gender': 'M'},
                               related_name='children_of_father')
    mother = models.ForeignKey('self',
                               blank=True,
                               null=True,
                               on_delete=models.CASCADE,
                               limit_choices_to={'gender': 'F'},
                               related_name='children_of_mother')
    housband = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null = True,
                               limit_choices_to={'gender': 'M'},
                               related_name='partner_of_women')
    
    def __str__(self):
        return self.name
    