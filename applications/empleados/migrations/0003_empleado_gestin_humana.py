# Generated by Django 5.0.4 on 2024-05-03 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0002_rename_empleados_empleado'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='gestin_humana',
            field=models.BooleanField(default=False, verbose_name='RH :'),
        ),
    ]
