# Generated by Django 3.2.4 on 2021-06-26 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('familydataapp', '0015_auto_20210625_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='familydataapp.district'),
        ),
    ]
