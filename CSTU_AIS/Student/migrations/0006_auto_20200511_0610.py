# Generated by Django 3.0.2 on 2020-05-11 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0005_auto_20200511_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='titles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stitile', to='Student.Title'),
        ),
    ]
