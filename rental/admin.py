from django.contrib import admin

# Register your models here.
from .models import Brand, Category, Uav, UavInstance

# admin.site.register(Uav)
# admin.site.register(Brand)
admin.site.register(Category)
# admin.site.register(UavInstance)

class BrandAdmin(admin.ModelAdmin):
    fields = ['brand_name']

admin.site.register(Brand, BrandAdmin)

class UavsInstanceInline(admin.TabularInline):
    model = UavInstance

@admin.register(Uav)
class UavAdmin(admin.ModelAdmin):
     list_display = ('model', 'brand', 'display_category')

     inlines = [UavsInstanceInline]

@admin.register(UavInstance)
class UavInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'return_date')

    fieldsets = (
        (None, {
            'fields': ('Uav', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'return_date')
        }),
    )
