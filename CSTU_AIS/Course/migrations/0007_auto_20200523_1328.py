# Generated by Django 3.0.2 on 2020-05-23 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0006_auto_20200511_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculum',
            name='curri',
            field=models.IntegerField(max_length=20),
        ),
    ]
