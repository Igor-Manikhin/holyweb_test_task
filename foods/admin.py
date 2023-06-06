from django.contrib import admin

from foods import models


class FoodAdmin(admin.ModelAdmin):
    model = models.Food
    list_display = ("name_ru", "category",)


class FoodCategoryAdmin(admin.ModelAdmin):
    model = models.FoodCategory
    list_display = ("name_ru",)


admin.site.register(models.Food, FoodAdmin)
admin.site.register(models.FoodCategory, FoodCategoryAdmin)
