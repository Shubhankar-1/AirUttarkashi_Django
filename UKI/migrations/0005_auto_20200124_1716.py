# Generated by Django 2.2.6 on 2020-01-24 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UKI', '0004_auto_20191225_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=15)),
                ('Last_Name', models.CharField(max_length=15)),
                ('From', models.CharField(max_length=10)),
                ('To', models.CharField(max_length=10)),
                ('Mob', models.IntegerField()),
                ('Flight_Date', models.DateField()),
                ('Class', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='info',
        ),
    ]
