# Generated by Django 3.0.2 on 2020-05-23 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0008_auto_20200523_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='major_or_track',
            name='m_or_t',
        ),
    ]
