# Generated by Django 4.1.2 on 2022-10-18 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0004_place3'),
    ]

    operations = [
        migrations.CreateModel(
            name='place4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
