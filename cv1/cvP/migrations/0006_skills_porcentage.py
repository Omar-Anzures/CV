# Generated by Django 3.0.5 on 2020-04-16 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvP', '0005_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='porcentage',
            field=models.PositiveSmallIntegerField(default=60),
        ),
    ]