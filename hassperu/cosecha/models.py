from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class TipoDeCultivo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo')

    def __str__(self):
        return self.nombre
    
class Cultivo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo')
    tipo_cultivo = models.ForeignKey('TipoDeCultivo', on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
   


class Cliente(models.Model):
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"    

class Variedade(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo')

    def __str__(self):
        return self.nombre
    

class FaseCultivo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo')

    def __str__(self):
        return self.nombre

class Colaborador(models.Model):
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Cosecha(models.Model):
    fecha_hora = models.DateTimeField()
    ubicacion = models.CharField(max_length=100)
    cantidad_cosechada = models.PositiveIntegerField()
    equipo_utilizado = models.CharField(max_length=100)
    calidad_cosechado = models.CharField(max_length=20)
    observaciones = models.TextField()
    fase = models.ForeignKey('FaseCultivo', on_delete=models.CASCADE)
    persona_ejecuta = models.ForeignKey(Colaborador, on_delete=models.CASCADE, default=1)
    cultivo = models.ForeignKey('Cultivo', on_delete=models.CASCADE, default=1)
    variedad = models.ForeignKey('Variedade', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Cosecha - {self.fecha_hora}"