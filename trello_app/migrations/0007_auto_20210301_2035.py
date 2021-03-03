# Generated by Django 3.1.6 on 2021-03-01 15:05

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trello_app', '0006_auto_20210301_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 15, 5, 32, 60548, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 15, 5, 32, 96416, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='list',
            field=models.ForeignKey(choices=[('list 1', 'LIST1'), ('list 2', 'LIST 2'), ('list 3', 'LIST 3'), ('lsit 4', 'LIST 4')], on_delete=django.db.models.deletion.CASCADE, to='trello_app.tasklist'),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 15, 5, 32, 96416, tzinfo=utc)),
        ),
    ]