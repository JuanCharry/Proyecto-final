from django.contrib import admin
from .models import Empleado

# Register your models here.
class EmpAd(admin.ModelAdmin):
    list_display = (
        'name',
        'last_name',
        'job',
        'email',
        'salario',
    )
    
admin.site.register(Empleado , EmpAd)