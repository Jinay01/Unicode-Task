# Generated by Django 3.0.8 on 2020-07-23 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attempt1', '0011_auto_20200723_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiinput',
            name='counter',
            field=models.FloatField(default=0),
        ),
    ]