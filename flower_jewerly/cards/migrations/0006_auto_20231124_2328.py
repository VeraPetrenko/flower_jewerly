# Generated by Django 3.2.3 on 2023-11-24 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0005_alter_сhain_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='name',
            field=models.CharField(default=1, max_length=200, verbose_name='Название компонента'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='JewerlyComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, help_text='Дата создания', verbose_name='Дата создания')),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jew_component', to='cards.component', verbose_name='Название компонента')),
                ('jewerly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jew_component', to='cards.jewerly', verbose_name='Название компонента')),
            ],
            options={
                'ordering': ('pub_date',),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='jewerly',
            name='сomponents',
            field=models.ManyToManyField(through='cards.JewerlyComponent', to='cards.Component', verbose_name='Компоненты украшения'),
        ),
    ]
