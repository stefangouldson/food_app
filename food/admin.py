from django.contrib import admin
from .models import Item

# Register your models here.
admin.site.site_header = "Custom Header"
admin.site.site_title = 'Custom Title'
admin.site.index_title = 'Manage some shit'

class ItemAdmin(admin.ModelAdmin):

    def change_price_to_free(self, request, queryset):
        queryset.update(item_price = 0, )
    change_price_to_free.short_description = 'Make Free'

    list_display = ('item_name', 'item_desc', 'item_price')
    search_fields = ('item_name',)
    actions = ('change_price_to_free',)
    fields = ('item_name', 'item_desc')
    list_editable = ('item_price',)
    list_filter = ['item_price']

admin.site.register(Item, ItemAdmin)