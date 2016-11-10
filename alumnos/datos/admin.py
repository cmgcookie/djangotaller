from django.contrib import admin

# Register your models here.
from .models import infoGeneral

class infoGeneralAdmin(admin.ModelAdmin):
    pass

admin.site.register(infoGeneral, infoGeneralAdmin)