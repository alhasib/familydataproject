# Generated by Django 3.2.4 on 2021-06-23 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familydataapp', '0009_alter_member_date_of_death'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='date_of_death',
            field=models.DateField(blank=True, default='Present', null=True),
        ),
    ]
