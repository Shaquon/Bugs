# Generated by Django 2.2.7 on 2019-12-02 07:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Bugs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='Time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
