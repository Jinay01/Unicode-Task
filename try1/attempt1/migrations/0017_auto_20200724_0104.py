# Generated by Django 3.0.8 on 2020-07-23 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attempt1', '0016_delete_usercheck'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiinput',
            name='repo_count',
            field=models.IntegerField(default=0),
        ),
    ]
