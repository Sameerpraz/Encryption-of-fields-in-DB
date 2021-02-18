from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','name','address']
# Register your models here.
admin.site.register(Customer,CustomerAdmin)