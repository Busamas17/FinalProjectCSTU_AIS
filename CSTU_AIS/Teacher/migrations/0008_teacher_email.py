# Generated by Django 3.0.2 on 2020-05-25 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0007_auto_20200525_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
