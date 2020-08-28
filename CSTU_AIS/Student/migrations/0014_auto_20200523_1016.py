# Generated by Django 3.0.2 on 2020-05-23 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0013_student_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrance_info',
            name='student_id',
        ),
        migrations.AddField(
            model_name='entrance_info',
            name='gat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='entrance_info',
            name='gpax',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='entrance_info',
            name='onet_eng',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='entrance_info',
            name='onet_math',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='entrance_info',
            name='onet_sci',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='entrance_info',
            name='onet_soc',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='entrance_info',
            name='onet_th',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='entrance_info',
            name='pat1',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='entrance_info',
            name='pat2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='entrance_info',
            name='TCAS',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='entrance_info',
            name='entrance_score',
            field=models.FloatField(null=True),
        ),
        migrations.DeleteModel(
            name='Entrance_Score',
        ),
    ]
