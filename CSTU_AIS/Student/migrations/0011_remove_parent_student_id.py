# Generated by Django 3.0.2 on 2020-05-11 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0010_auto_20200511_0649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='student_id',
        ),
    ]
