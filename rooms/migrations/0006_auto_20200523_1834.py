# Generated by Django 2.2.5 on 2020-05-23 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20200523_1803'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='houserule',
            new_name='houserules',
        ),
    ]
