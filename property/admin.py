from django.contrib import admin

from .models import Flat, Сomplaint, Owner


class OwnerInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ['owner']

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_nuber', 'pure_phone_number']
    search_fields = ['full_name', 'phone_nuber']
    raw_id_fields = ['flats']

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    inlines = (OwnerInline,)
    search_fields = ['town', 'address', 'owner', 'owner_pure_phone']
    readonly_fields = ['created_at']
    list_display = ['address', 'price','new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked']


@admin.register(Сomplaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['user', 'flat', 'text']
    raw_id_fields = ['user', 'flat']

