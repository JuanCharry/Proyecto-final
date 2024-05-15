from rest_framework import serializers
#?
from .models import Empleado

from rest_framework import serializers
from .models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer): 
    class Meta:
        model =  Empleado
        fields = (
            'id',
            'name',
            'last_name',
            'job',
            'email',
            'salario'
        )
        read_only_fields = ('name', 'last_name', 'job', 'salario')




class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'
