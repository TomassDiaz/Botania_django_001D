from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class tipoUsuario(models.Model):
    idtipoUsuario = models.AutoField(
        primary_key=True, db_column='idtipo', verbose_name='id_tipoUsuario'
    )
    tipoUsuario = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.tipoUsuario)

class Usuario(models.Model):
    # Nombre - AppPaterno -  correo - clave - direccion - telefono - Region - Provincia
    # Comuna - Codigo postal

    nombre = models.CharField(max_length=50, blank=False, null=False)
    apaterno = models.CharField(max_length=30, blank=False, null=False)
    amaterno = models.CharField(max_length=30, blank=False, null=False)
    correo = models.EmailField(unique=True, blank=False, null=False, max_length=100)
    clave = models.CharField(max_length=30, blank=False, null=False)
    direccion = models.CharField(max_length=50, blank=False, null=False)
    telefono = models.CharField(max_length=10, blank=False, null=False)
    region = models.CharField(max_length=50, blank=False, null=False)
    provincia = models.CharField(max_length=50, blank=False, null=False)
    comuna = models.CharField(max_length=50, blank=False, null=False)
    codpos = models.CharField(max_length=7, blank=False, null=False)
    tipoUsuario = models.ForeignKey(tipoUsuario, on_delete=models.CASCADE, db_column='idtipo')

    def __str__(self):
        return str(self.nombre) + " " + str(self.apaterno) + " " + str(self.amaterno)

class Catalogo(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=50)
    tamaño = models.CharField(max_length=30)
    temporada = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    moneda = models.CharField(max_length=10, default='CLP')

    def __str__(self):
        return self.nombre
    


class ItemCarrito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Catalogo, on_delete=models.CASCADE)
    cantidad = models.PositiveBigIntegerField(default=1)
