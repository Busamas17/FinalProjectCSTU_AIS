# Generated by Django 3.0.2 on 2020-05-30 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0019_auto_20200530_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='course_condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=100)),
            ],
        ),
    ]
