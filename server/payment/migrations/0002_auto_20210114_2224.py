# Generated by Django 3.1.5 on 2021-01-14 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='date',
            new_name='date_paid',
        ),
    ]
