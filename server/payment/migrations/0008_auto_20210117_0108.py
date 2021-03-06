# Generated by Django 3.1.5 on 2021-01-16 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0007_bill_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='doctor',
        ),
        migrations.AlterField(
            model_name='bill',
            name='amount_paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bill',
            name='current_balance_before',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bill',
            name='new_balance_after',
            field=models.IntegerField(default=0),
        ),
    ]
