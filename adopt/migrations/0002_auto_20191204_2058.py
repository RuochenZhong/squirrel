# Generated by Django 3.0 on 2019-12-04 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='Other_activities',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='show',
            name='Shift',
            field=models.CharField(choices=[('AM', 'am'), ('PM', 'pm')], max_length=2),
        ),
    ]
