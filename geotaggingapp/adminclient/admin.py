from django.contrib import admin

# Register your models here.
from .models import Farmer, Plant, Record

class FarmerAdmin(admin.ModelAdmin):
    model = Farmer
    search_fields = ['farmerID','farmerName', 'birthDate', 'gender', 'numWorkers']
    list_display = ('farmerID','farmerName', 'birthDate', 'gender', 'numWorkers')
admin.site.register(Farmer,FarmerAdmin)

class PlantAdmin(admin.ModelAdmin):
    model = Plant
    search_fields = ['plantID','farmerID','long', 'lat', 'datePlanted']
    list_display = ('plantID','farmerID','long', 'lat', 'datePlanted')
admin.site.register(Plant,PlantAdmin)

class RecordAdmin(admin.ModelAdmin):
    model = Record
    search_fields = ['recordID', 'plantID', 'date', 'time']
    list_display = ('recordID', 'plantID', 'date', 'time')
admin.site.register(Record,RecordAdmin)

