# Generated by Django 3.0 on 2019-12-04 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopt', '0003_auto_20191204_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='Date',
            field=models.CharField(max_length=10),
        ),
    ]