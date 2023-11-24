from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
CHARFIELDS_MAX_LEN = 200


class CreatedModel(models.Model):
    """Абстрактная модель для добавления даты
    создания объекта."""
    pub_date = models.DateTimeField(
        'Дата создания',
        help_text='Дата создания',
        auto_now_add=True,
    )

    class Meta:
        abstract = True
        ordering = ('pub_date',)


class Component(CreatedModel):
    name = models.CharField(
        verbose_name='Название компонента',
        max_length=CHARFIELDS_MAX_LEN,
    )

    def __str__(self):
        return f'{self.name}'


class JewerlyComponent(CreatedModel):
    component = models.ForeignKey(
        'Component',
        on_delete=models.CASCADE,
        verbose_name='Название компонента',
        related_name='jew_component',
    )
    jewerly = models.ForeignKey(
        'Jewerly',
        on_delete=models.CASCADE,
        verbose_name='Название компонента',
        related_name='jew_component',
    )


class JewForm(CreatedModel):
    name = models.CharField(
        verbose_name='Название формы',
        max_length=CHARFIELDS_MAX_LEN,
    )
    slug = models.CharField(
        verbose_name='Слаг формы',
        max_length=CHARFIELDS_MAX_LEN,
    )

    def __str__(self):
        return f'Форма: {self.name}'


class Сhain(CreatedModel):
    length = models.CharField(
        verbose_name='Длина цепочки',
        max_length=CHARFIELDS_MAX_LEN,
        default='45',
    )
    color = models.CharField(
        verbose_name='Цвет цепочки',
        max_length=CHARFIELDS_MAX_LEN,
        default='Серебряная',
    )

    def __str__(self):
        if self.length == 'регулируемая':
            return f'{self.color} цепочка регулируемой длины'
        return f'{self.color} цепочка {self.length} мм'


class Jewerly(CreatedModel):
    name = models.CharField(
        verbose_name='Название украшения',
        max_length=CHARFIELDS_MAX_LEN,
    )
    description = models.TextField(
        verbose_name='Описание украшения',
    )
    length = models.PositiveSmallIntegerField(
        verbose_name='Длина украшения',
    )
    width = models.PositiveSmallIntegerField(
        verbose_name='Ширина украшения',
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена украшения',
    )
    chain = models.ForeignKey(
        'Сhain',
        on_delete=models.SET_DEFAULT,
        verbose_name='Длина цепочки',
        related_name='chain',
        default='Серебряная 45 мм',
    )
    available = models.BooleanField(default=True)
    # image = models.ImageField(
    #     upload_to='cards/media/',
    #     null=True,
    #     default=None,
    # )
    сomponents = models.ManyToManyField(
        'Component',
        through='JewerlyComponent',
        verbose_name="Компоненты украшения",
    )


    def __str__(self):
        return f'{self.name}'


