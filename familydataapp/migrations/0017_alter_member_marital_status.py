# Generated by Django 3.2.4 on 2021-06-27 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familydataapp', '0016_member_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('M', 'Married'), ('s', 'Unmarried')], default=False, max_length=1, null=True),
        ),
    ]
