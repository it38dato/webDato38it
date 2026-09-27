from django.contrib import admin
from .models import *
admin.site.register(Category)
#admin.site.register(Category,CategoryAdmin)
admin.site.register(Place)
admin.site.register(Portfolio)
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title",)
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    ordering = ("order", "name")
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "value", "order")
    ordering = ("order", "name")