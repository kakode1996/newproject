# Generated by Django 2.2.6 on 2019-10-14 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='dog',
            name='name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
