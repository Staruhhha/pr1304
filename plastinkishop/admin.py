from django.contrib import admin
from plastinkishop.models import *


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'agent_FIO', 'agent_telephone')
    list_display_links = ('name',)
    search_fields = ('name', 'agent_firstname')
    ordering = ('name',)

    @admin.display(description='ФИО представителя')
    def agent_FIO(self, obj):
        if obj.agent_patronymic:
            return f"{obj.agent_firstname} {obj.agent_name[0]}. {obj.agent_patronymic[0]}."
        return f"{obj.agent_firstname} {obj.agent_name[0]}."

@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_supply', 'supplier_name')
    list_display_links = ('id', 'date_supply')
    search_fields = ('date', 'supplier_name')
    ordering = ('id',)

    @admin.display(description='Поставщик')
    def supplier_name(self, obj):
        return obj.supplier.name


@admin.register(Pos_supply)
class Pos_supplyAdmin(admin.ModelAdmin):
        list_display = ('id', 'vinyl_record', 'supply', 'count')
        list_display_links = ('id',)
        search_fields = ('vinyl_record__name', 'supply__supplier__name')
        list_editable = ('count',)



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk','customer_FIO', 'delivery_address', 'delivery_type', 'datetime_create')
    list_display_links = ('pk', 'customer_FIO',)
    search_fields = ('delivery_address',)
    ordering = ('-datetime_create',)

    @admin.display(description='ФИО покупателя')
    def customer_FIO(self, obj):
        if obj.customer_patronymic:
            return f"{obj.customer_firstname} {obj.customer_name[0]}. {obj.customer_patronymic[0]}."
        return f"{obj.customer_firstname} {obj.customer_name[0]}."


@admin.register(Pos_order)
class Pos_orderAdmin(admin.ModelAdmin):
    list_display = ('order', 'vinyl_record', 'discount', 'count')
    list_display_links = None
    list_editable = ('vinyl_record', 'discount', 'count')
    search_fields = ('vinyl_record__name', 'order__id')
    ordering = ('-order__id',)


@admin.register(Parametr)
class ParametrAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('name',)
    list_editable = ('name',)
    ordering = ('name',)


@admin.register(Pos_parametr)
class Pos_parametrAdmin(admin.ModelAdmin):
    list_display = ('vinyl_record', 'parametr', 'value')
    list_display_links = None
    search_fields = ('vinyl_record__name', 'parametr__name')
    list_editable = ('vinyl_record', 'parametr', 'value')
    ordering = ('-vinyl_record__name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = None
    list_editable = ('name', 'description')
    search_fields = ('name',)
    ordering = ('-name',)


@admin.register(Performer)
class PerformerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name',)
    search_fields = ('name',)
    ordering = ('name',)



@admin.register(Vinyl_record)
class Vinyl_recordAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name','price', 'genre', 'is_exist')
    search_fields = ('name',)
    list_filter = ('genre', 'is_exist')
    list_display_links = ('name',)
    list_editable = ('price', 'is_exist')
    ordering = ('-pk',)


