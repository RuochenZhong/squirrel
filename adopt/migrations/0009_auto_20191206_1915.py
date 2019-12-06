# Generated by Django 3.0 on 2019-12-06 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopt', '0008_auto_20191206_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='Age',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='Location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='Other_activities',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='Primary_fur_color',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='Shift',
            field=models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], max_length=2),
        ),
        migrations.AlterField(
            model_name='show',
            name='Specific_location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]