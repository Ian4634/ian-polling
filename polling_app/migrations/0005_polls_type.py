# Generated by Django 3.2.5 on 2021-08-14 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polling_app', '0004_auto_20210809_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='polls',
            name='type',
            field=models.CharField(default='question', max_length=200),
        ),
    ]