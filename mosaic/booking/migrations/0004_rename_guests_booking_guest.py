# Generated by Django 4.1.3 on 2022-11-18 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_remove_booking_guest_booking_guests'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='guests',
            new_name='guest',
        ),
    ]