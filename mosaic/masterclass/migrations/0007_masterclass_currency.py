# Generated by Django 4.1.3 on 2022-11-18 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterclass', '0006_alter_masterclass_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterclass',
            name='currency',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]