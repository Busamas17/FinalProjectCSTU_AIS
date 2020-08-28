# Generated by Django 3.0.2 on 2020-06-04 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0050_auto_20200604_0907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='check_for_cs101',
        ),
        migrations.RemoveField(
            model_name='student',
            name='check_for_cs223',
        ),
        migrations.RemoveField(
            model_name='student',
            name='check_for_cs300',
        ),
        migrations.CreateModel(
            name='Check_for_lastest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_for_cs101', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='check101', to='Student.Enrollment')),
                ('check_for_cs223', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='check223', to='Student.Enrollment')),
                ('check_for_cs300', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='check300', to='Student.Enrollment')),
                ('student_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Student.Student')),
            ],
        ),
    ]
