# Generated by Django 2.2.6 on 2020-01-24 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UKI', '0005_auto_20200124_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='Flight_Date',
            field=models.CharField(max_length=15),
        ),
    ]