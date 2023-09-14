# Generated by Django 4.1.7 on 2023-06-16 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_block_massag_poleot_alter_block_massag_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block_massag',
            name='PoleOt',
            field=models.CharField(max_length=2, null=True, verbose_name='Приставка к сумме'),
        ),
        migrations.AlterField(
            model_name='block_massag',
            name='time',
            field=models.CharField(max_length=10, null=True, verbose_name='Продолжительность в минутах'),
        ),
    ]