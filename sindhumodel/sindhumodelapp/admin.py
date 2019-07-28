from django.contrib import admin
from sindhumodelapp.models import Worldcup

# Register your models here.
class WorldcupAdmin(admin.ModelAdmin):
    list_display=['country1','country2','date','result']

admin.site.register(Worldcup,WorldcupAdmin)
