# Generated by Django 2.2.24 on 2024-05-29 07:46

from django.db import migrations


def new_bilding(apps, shema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__gte=2015).update(new_building=True)
    Flat.objects.filter(construction_year__lt=2015).update(new_building=False)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_auto_20240529_1036'),
    ]

    operations = [
        migrations.RunPython(new_bilding)
    ]
