# Generated by Django 3.2.6 on 2021-10-23 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('better', '0002_auto_20211021_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]
