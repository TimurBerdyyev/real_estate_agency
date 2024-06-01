from django.db import migrations, models
import phonenumbers

def normalize_phone_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats_to_update = []

    for flat in Flat.objects.iterator():
        if flat.owners_phonenumber:
            try:
                parsed_phone = phonenumbers.parse(flat.owners_phonenumber, 'RU')
                if phonenumbers.is_valid_number(parsed_phone):
                    flat.owner_pure_phone = phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.E164)
                else:
                    flat.owner_pure_phone = None
            except phonenumbers.NumberParseException:
                flat.owner_pure_phone = None
            flats_to_update.append(flat)

    Flat.objects.bulk_update(flats_to_update, ['owner_pure_phone'])

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_number)
    ]
