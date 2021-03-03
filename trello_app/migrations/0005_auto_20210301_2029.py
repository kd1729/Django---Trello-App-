# Generated by Django 3.1.6 on 2021-03-01 14:59

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trello_app', '0004_auto_20210301_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 14, 59, 45, 365278, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 14, 59, 45, 401314, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='board',
            field=models.ForeignKey(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='green', on_delete=django.db.models.deletion.CASCADE, to='trello_app.board'),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 14, 59, 45, 400318, tzinfo=utc)),
        ),
    ]