from django.db import models

# Create your models here.


#!empleados 
trabajos = (
    ('0' , 'Contador '),
    ('1' , 'Gerente '),
    ('2' , 'Economista '),
    ('3' , 'Programador'),
    ('4', 'Otro'),
    ('5', 'Administrados'),
    ('6','Psicologo'),
    ('7', 'Ingeniro ambiental')
)

class Empleado(models.Model):

    name = models.CharField(
        'Nombre', 
        max_length = 50
    )
    last_name = models.CharField(
        'Apellido',
        max_length = 20 
    )
    job = models.CharField(
        'Trabajo', 
        max_length=1,
        choices = trabajos
    )
    email = models.EmailField(
        max_length = 30 ,
        blank = True
    )
    salario = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )
    gestion_humana= models.BooleanField('RH :', default = False)
    
    def __str__(self):
        return self.name + ' ' + self.job