# Generated by Django 3.0.2 on 2020-05-23 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0009_remove_major_or_track_m_or_t'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_usage',
            name='course_tqf',
        ),
    ]
