from django.contrib import admin
from .models import Block_massag, Block_spa_program ,Block_taping, Block_obuchine


class MassagAdmin(admin.ModelAdmin):
    list_display = ('title', 'time','content','PoleOt','price')

admin.site.register(Block_massag, MassagAdmin)

class SpaAdmin(admin.ModelAdmin):
    list_display = ('title', 'time','content','price')

admin.site.register(Block_spa_program, SpaAdmin)

class TapingAdmin(admin.ModelAdmin):
    list_display = ('title','content','price')

admin.site.register(Block_taping, TapingAdmin)


class ObuchineAdmin(admin.ModelAdmin):
    list_display = ('title', 'time','content','price')

admin.site.register(Block_obuchine, ObuchineAdmin)