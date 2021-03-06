# Generated by Django 2.2.7 on 2019-11-21 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Time', models.DateTimeField()),
                ('Description', models.CharField(max_length=50)),
                ('Status', models.CharField(choices=[('New', 'New'), ('In_progress', 'In_progress'), ('DONE', 'Done'), ('VALID', 'Valid')], default='New', max_length=200)),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name', to=settings.AUTH_USER_MODEL)),
                ('assigned', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned', to=settings.AUTH_USER_MODEL)),
                ('completed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='completed', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
