# Generated by Django 3.0.2 on 2020-05-28 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0038_auto_20200528_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(default='', max_length=500, null=True),
        ),
    ]
