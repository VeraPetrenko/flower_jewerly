# Generated by Django 3.2.3 on 2023-11-24 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_remove_сhain_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='jewerly',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='jewerly',
            name='chain',
            field=models.ForeignKey(default='Серебряная 45 мм', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='chain', to='cards.сhain', verbose_name='Длина цепочки'),
        ),
        migrations.AlterField(
            model_name='сhain',
            name='color',
            field=models.CharField(default='Серебряная', max_length=200, verbose_name='Цвет цепочки'),
        ),
        migrations.AlterField(
            model_name='сhain',
            name='length',
            field=models.PositiveSmallIntegerField(default=45, verbose_name='Длина цепочки'),
        ),
    ]
