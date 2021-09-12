from django.contrib import admin
from .models import *
# Register your models here.


class RecipeModelAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'updated', 'timestamp']
    list_display_links = ['title']
    list_filter = ['updated', 'timestamp']

    class Meta:
        model = Recipe


admin.site.register(Recipe, RecipeModelAdmin)
admin.site.register(Ingredient)
admin.site.register(Technique)
admin.site.register(Category)
admin.site.register(PrepTime)
admin.site.register(CookTime)
admin.site.register(Difficulty)
