# Generated by Django 3.1.5 on 2021-01-09 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.IntegerField()),
                ('current_balance_before', models.IntegerField()),
                ('new_balance_after', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
