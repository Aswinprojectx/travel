# Generated by Django 4.1.2 on 2022-10-21 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0005_place4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place4',
            name='img',
            field=models.ImageField(upload_to='pics1'),
        ),
    ]
