# Generated by Django 3.0.2 on 2020-06-04 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0049_delete_check_for_lastest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='applicant_code',
            new_name='applicant_type_id',
        ),
    ]
