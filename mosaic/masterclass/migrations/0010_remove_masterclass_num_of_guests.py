# Generated by Django 4.1.3 on 2022-11-18 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masterclass', '0009_alter_masterclass_course_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masterclass',
            name='num_of_guests',
        ),
    ]
