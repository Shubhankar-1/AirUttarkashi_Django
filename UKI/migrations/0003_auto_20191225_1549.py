# Generated by Django 2.2.6 on 2019-12-25 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UKI', '0002_auto_20191206_1651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='No_of_ticket',
            new_name='Last_Name',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='Name',
            field=models.CharField(max_length=15),
        ),
    ]
