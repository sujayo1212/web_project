from django.contrib import admin
from lecture.models import Lecture, Category

admin.site.register(Lecture)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('class_name', )}


admin.site.register(Category, CategoryAdmin)