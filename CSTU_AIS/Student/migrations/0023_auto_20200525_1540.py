# Generated by Django 3.0.2 on 2020-05-25 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0022_auto_20200525_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parent',
            old_name='P_phone',
            new_name='p_phone',
        ),
    ]
