# Generated by Django 3.2.5 on 2021-08-14 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polling_app', '0005_polls_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='polls',
            name='type',
        ),
        migrations.AddField(
            model_name='polls',
            name='answer',
            field=models.CharField(default=None, max_length=1000),
        ),
    ]
