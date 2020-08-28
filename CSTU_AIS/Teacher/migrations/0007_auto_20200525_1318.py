# Generated by Django 3.0.2 on 2020-05-25 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0006_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Title',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='management_position',
            new_name='education_position',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='title',
        ),
        migrations.AddField(
            model_name='teacher',
            name='campus',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
