# Generated by Django 2.2.5 on 2020-05-27 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200527_0936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email_confirmed',
            new_name='email_verify',
        ),
        migrations.AddField(
            model_name='user',
            name='email_secrete',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
    ]
