# Generated by Django 3.2.7 on 2021-10-01 22:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Heart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measured_datetime', models.DateTimeField(default=datetime.datetime(2021, 10, 1, 22, 50, 28, 317012, tzinfo=utc))),
                ('sys', models.IntegerField(default=0)),
                ('dia', models.IntegerField(default=0)),
                ('heart_rate', models.IntegerField(default=0)),
                ('note', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['measured_datetime'],
            },
        ),
    ]