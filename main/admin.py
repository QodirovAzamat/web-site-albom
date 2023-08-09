from django.contrib import admin
from .models import Category , Royxat


@admin.register(Category)
class CatigoryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    fields = ["title", "slug" , "description"]
    readonly_fields = ["created" , "updated"]
    prepopulated_fields = {"slug":("title", )}
    search_fields = ["title", "slug" , "description"]
    list_filter = ["created" , "updated"]

@admin.register(Royxat)
class RoyxatAdmin(admin.ModelAdmin):
    list_display = ["title", "slug","shirt_size","category"]
    fields = ["title", "slug" , "description","shirt_size","category"]
    

    

