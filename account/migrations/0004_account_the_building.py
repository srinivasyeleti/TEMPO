# Generated by Django 2.2.2 on 2021-04-10 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_auto_20210410_1020'),
        ('account', '0003_auto_20210410_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='the_building',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='personal.Building'),
        ),
    ]