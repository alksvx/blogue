# Generated by Django 4.2 on 2023-07-04 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('Красота', 'Красота'), ('Мода', 'Мода'), ('Отношения', 'Отношения'), ('Знаменитости', 'Знаменитости')], default='Мода', max_length=15, verbose_name='Категория'),
        ),
    ]
