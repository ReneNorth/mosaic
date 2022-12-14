# Generated by Django 4.1.3 on 2022-11-17 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('masterclass', '0002_masterclass_num_of_guests'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attending', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attending', to='masterclass.masterclass')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
