# Generated by Django 3.0.2 on 2020-05-26 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0029_auto_20200526_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='grade',
            field=models.CharField(max_length=20),
        ),
    ]
