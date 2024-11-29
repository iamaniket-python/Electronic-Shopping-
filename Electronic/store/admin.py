from django.contrib import admin
from .models import *
# Register your models here.

class OrderitemTabularInline(admin.TabularInline):
    model = Orderitem

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderitemTabularInline,
        ]
    

class ImagesTabularInline(admin.TabularInline):
    model=Images

class TagTabularInline(admin.TabularInline):
    model=Tag

class ProductAdmin(admin.ModelAdmin):
    inlines=[TagTabularInline,ImagesTabularInline]

@admin.register(Categories)
class CategoriesModelAdmin(admin.ModelAdmin):
    list_display=['name']


@admin.register(Brand)
class BrandModelAdmin(admin.ModelAdmin):
    list_display=['name']

@admin.register(Color)
class ColorModelAdmin(admin.ModelAdmin):
    list_display=['name']

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display=['name','email','subject','message','date']

admin.site.register(Filter_price)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images)
admin.site.register(Tag)
admin.site.register(Order)
admin.site.register(Orderitem)