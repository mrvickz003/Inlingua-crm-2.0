# Generated by Django 5.0.4 on 2024-07-09 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inlingua_app', '0002_studenttable_balance_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studenttable',
            old_name='Account_Paide',
            new_name='Amount_Paide',
        ),
    ]
