# Generated by Django 3.0.2 on 2020-05-31 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0022_auto_20200530_1132'),
        ('Student', '0044_auto_20200531_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.Course'),
        ),
    ]
