# Generated by Django 3.2.4 on 2021-06-22 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familydataapp', '0006_member_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
