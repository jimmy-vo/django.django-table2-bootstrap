# Generated by Django 2.2.5 on 2019-10-01 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0003_person_height'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='commonwealth',
        ),
        migrations.RemoveField(
            model_name='country',
            name='continent',
        ),
        migrations.RemoveField(
            model_name='country',
            name='flag',
        ),
        migrations.RemoveField(
            model_name='country',
            name='population',
        ),
        migrations.RemoveField(
            model_name='country',
            name='tz',
        ),
        migrations.RemoveField(
            model_name='country',
            name='visits',
        ),
        migrations.DeleteModel(
            name='Continent',
        ),
    ]