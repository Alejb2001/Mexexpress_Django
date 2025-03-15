from django.contrib import admin
from shopApp.models import Product,HistoricalCost

# Register your models here.
admin.site.register(Product)
admin.site.register(HistoricalCost)
