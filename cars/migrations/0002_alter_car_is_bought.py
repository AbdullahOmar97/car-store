# Generated by Django 5.0.7 on 2024-07-22 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='is_bought',
            field=models.BooleanField(),
        ),
    ]
