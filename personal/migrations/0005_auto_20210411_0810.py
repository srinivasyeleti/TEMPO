# Generated by Django 2.2.2 on 2021-04-11 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_auto_20210410_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='current_temp',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='max_temp',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='min_temp',
            field=models.FloatField(null=True),
        ),
    ]
