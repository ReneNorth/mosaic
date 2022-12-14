# Generated by Django 4.1.3 on 2022-11-17 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterclass', '0003_masterclasstype_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterclass',
            name='time_begin',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='masterclass',
            name='time_end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='masterclasstype',
            name='length',
            field=models.PositiveSmallIntegerField(verbose_name='How many hours required to finish the masterclass'),
        ),
    ]
