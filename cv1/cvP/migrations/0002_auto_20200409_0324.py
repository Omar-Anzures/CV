# Generated by Django 3.0.5 on 2020-04-09 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='end_year',
            field=models.DateField(blank=True),
        ),
    ]
