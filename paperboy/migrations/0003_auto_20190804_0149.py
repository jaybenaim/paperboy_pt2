# Generated by Django 2.2.4 on 2019-08-04 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperboy', '0002_remove_paperboy_earnings'),
    ]

    operations = [
        migrations.AddField(
            model_name='paperboy',
            name='end_house_number',
            field=models.IntegerField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paperboy',
            name='start_house_number',
            field=models.IntegerField(default=False),
            preserve_default=False,
        ),
    ]
