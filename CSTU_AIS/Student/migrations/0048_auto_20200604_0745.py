# Generated by Django 3.0.2 on 2020-06-04 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0047_enrollment_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='check_for_cs101',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='check_for_cs223',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='check_for_cs300',
            field=models.CharField(max_length=20, null=True),
        ),
    ]