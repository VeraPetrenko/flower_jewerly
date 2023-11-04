from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class CreatedModel(models.Model):
    '''Абстрактная модель для добавления даты
    создания объекта.'''
    pub_date = models.DateTimeField(
        'Дата создания',
        help_text='Дата создания',
        auto_now_add=True,
    )

    class Meta:
        abstract = True
        ordering = ('pub_date',)


class Jewerly(CreatedModel):
    ...


class JewForm(CreatedModel):
    ...


class Component(CreatedModel):
    ...


class Сhain(CreatedModel):
    ...
