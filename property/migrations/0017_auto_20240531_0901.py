# Generated by Django 2.2.24 on 2024-05-31 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20240531_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='has_balcony',
            field=models.BooleanField(db_index=True, null=True, verbose_name='Наличие балкона'),
        ),
    ]
