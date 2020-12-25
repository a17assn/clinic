# Generated by Django 3.1.2 on 2020-11-29 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdultTeethChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UR_1', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UR_2', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UR_3', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UR_4', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UR_5', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UR_6', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UR_7', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UR_8', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UL_9', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UL_10', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UL_11', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UL_12', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UL_13', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UL_14', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UL_15', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UL_16', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LL_17', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LL_18', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LL_19', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LL_20', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LL_21', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LL_22', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LL_23', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LL_24', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LR_25', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LR_26', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LR_27', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LR_28', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LR_29', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LR_30', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LR_31', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LR_32', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChildTeethChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UR_A', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UR_B', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UR_C', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UR_D', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UR_E', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UL_F', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UL_G', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UL_H', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UL_I', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('UL_J', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LL_K', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LL_L', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LL_M', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LL_N', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LL_O', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LR_P', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LR_Q', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LR_R', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LR_S', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
                ('LR_T', models.CharField(blank=True, choices=[('None', 'None'), ('Decayed', 'Decayed'), ('Missing', 'Missing'), ('Filled', 'Filled')], default='None', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('token', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('dental_position', models.CharField(blank=True, max_length=50, null=True)),
                ('dental_test', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now=True, null=True)),
                ('adultTeethChart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treatment.adultteethchart')),
                ('ahildTeethChart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treatment.childteethchart')),
            ],
        ),
    ]
