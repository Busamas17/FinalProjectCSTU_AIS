# Generated by Django 3.0.2 on 2020-05-30 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0018_auto_20200528_0649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='major_or_track',
            old_name='major_and_track',
            new_name='major_or_track',
        ),
    ]
