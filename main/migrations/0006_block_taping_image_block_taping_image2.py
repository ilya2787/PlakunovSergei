# Generated by Django 4.1.7 on 2023-06-15 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_block_obuchine'),
    ]

    operations = [
        migrations.AddField(
            model_name='block_taping',
            name='image',
            field=models.ImageField(default=123, upload_to='image/taping', verbose_name='Изображение к услуги'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='block_taping',
            name='image2',
            field=models.ImageField(default=32, upload_to='image/taping', verbose_name='Изображение к услуги'),
            preserve_default=False,
        ),
    ]
