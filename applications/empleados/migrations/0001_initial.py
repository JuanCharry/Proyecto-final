# Generated by Django 5.0.4 on 2024-05-01 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=20, verbose_name='Apellido')),
                ('job', models.CharField(choices=[('0', 'Contador '), ('1', 'Gerente '), ('2', 'Economista '), ('3', 'Programador'), ('4', 'Otro'), ('5', 'Administrados'), ('6', 'Psicologo'), ('7', 'Ingeniro ambiental')], max_length=1, verbose_name='Trabajo')),
                ('email', models.EmailField(max_length=30)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
