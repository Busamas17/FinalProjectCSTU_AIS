# Generated by Django 3.0.2 on 2020-05-28 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0017_auto_20200528_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_sector_tgf',
            name='tqf_sector_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='usage_type',
            name='usage_type',
            field=models.CharField(max_length=100),
        ),
    ]
