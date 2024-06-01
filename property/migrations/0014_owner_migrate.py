from django.db import migrations
from ..models import Flat, Owner

def migrate_flat_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    
    flats_to_update = []

    for flat in Flat.objects.iterator():
        owner, created = Owner.objects.get_or_create(
            full_name=flat.owner,
            phone_nuber=flat.owners_phonenumber,  
            pure_phone_number=flat.owner_pure_phone
        )
        flat.owners.add(owner)
        flats_to_update.append(flat)
        
        if len(flats_to_update) >= 200:
            for f in flats_to_update:
                f.save()
            flats_to_update = []
            
    if flats_to_update:
        for f in flats_to_update:
            f.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20240529_1258'),
    ]

    operations = [
        migrations.RunPython(migrate_flat_owners)
    ]
