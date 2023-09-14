# Generated by Django 4.1.7 on 2023-06-15 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_block_taping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block_obuchine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Наименование')),
                ('time', models.CharField(max_length=200, verbose_name='Продолжительность')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Стоймость')),
            ],
            options={
                'verbose_name': 'Обучение',
                'verbose_name_plural': 'Услуга обучения',
            },
        ),
    ]
