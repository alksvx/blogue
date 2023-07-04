# Generated by Django 4.2 on 2023-07-04 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('Красота', 'Мода')], default='Мода', max_length=10),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='default.jpeg', upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Название'),
        ),
    ]