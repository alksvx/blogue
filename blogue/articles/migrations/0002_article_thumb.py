# Generated by Django 4.2 on 2023-04-24 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='default.jpeg', upload_to=''),
        ),
    ]
