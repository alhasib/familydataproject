# Generated by Django 3.2.4 on 2021-06-21 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familydataapp', '0003_member_housband'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='national_id_number',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]
