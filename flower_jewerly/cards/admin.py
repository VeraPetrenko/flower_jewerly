from django.contrib import admin

from cards.models import Component, Сhain, Jewerly, JewForm, JewerlyComponent


class JewerlyComponentInLine(admin.TabularInline):
    model = JewerlyComponent
    extra = 1


@admin.register(Jewerly)
class JewerlytAdmin(admin.ModelAdmin):
    inlines = (JewerlyComponentInLine,)
    list_display = (
        'id',
        'name',
        'length',
        'width',
        'price',
        'chain',
        'available',
    )
    empty_value_display = "-пусто-"
    list_editable = (
        'name',
        'length',
        'width',
        'price',
        'chain',
        'available',
    )
    # pass


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    # list_display = ('__all__')
    pass


@admin.register(Сhain)
class СhainAdmin(admin.ModelAdmin):
    # list_display = ('__all__')
    pass


@admin.register(JewForm)
class JewFormAdmin(admin.ModelAdmin):
    # list_display = ('__all__')
    pass
