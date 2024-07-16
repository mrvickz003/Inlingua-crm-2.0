# Generated by Django 5.0.6 on 2024-07-16 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inlingua_app', '0006_remove_trainerqualifications_trainerhead'),
    ]

    operations = [
        migrations.CreateModel(
            name='trainer_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer_name_mod', models.CharField(max_length=100)),
                ('trainer_dob_mod', models.DateField()),
                ('trainer_education_mod', models.CharField(max_length=100)),
                ('trainer_mail_mod', models.EmailField(max_length=254)),
                ('trainer_phone_mod', models.CharField(max_length=15)),
                ('trainer_languages_mod', models.CharField(max_length=100)),
                ('trainer_address_mod', models.TextField()),
                ('trainer_photo_mod', models.ImageField(upload_to='trainer_photos/')),
                ('trainer_bank_details_mod', models.CharField(max_length=100)),
                ('trainer_aadhar_mod', models.CharField(max_length=12)),
                ('trainer_role_mod', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='levels',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='user',
        ),
        migrations.AlterField(
            model_name='trainerqualifications',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inlingua_app.trainer_table'),
        ),
        migrations.DeleteModel(
            name='TrainingBatch',
        ),
        migrations.DeleteModel(
            name='Trainer',
        ),
    ]
