# Generated by Django 4.1.3 on 2022-11-18 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masterclass', '0010_remove_masterclass_num_of_guests'),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='attending',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='masterclass.masterclass'),
        ),
    ]
