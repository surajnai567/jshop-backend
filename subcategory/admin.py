from django.contrib import admin
from.models import SubCategory
# Register your models here.


@admin.register(SubCategory)
class AdminSub(admin.ModelAdmin):
    list_editable = ['discount', 'price']
    list_display = ['name', 'price', 'discount']
