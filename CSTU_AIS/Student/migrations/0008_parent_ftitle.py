# Generated by Django 3.0.2 on 2020-05-11 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0007_auto_20200511_0611'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='ftitle',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ftitle', to='Student.Title'),
        ),
    ]