# Generated by Django 5.0.4 on 2024-07-08 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inlingua_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='nameOfCounselor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=100)),
                ('Created_by', models.CharField(max_length=100)),
                ('Created_date', models.DateTimeField()),
                ('Updated_by', models.CharField(blank=True, max_length=100, null=True)),
                ('Updated_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
