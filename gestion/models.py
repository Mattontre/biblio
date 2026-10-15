from django.db import models

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre)

class Autor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre)
    
class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombre)

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.titulo)+"-"+str(self.autor)+"-"+str(self.editorial)+"-"+str(self.genero)

class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=12)
    nombre = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.rut)+"-"+str(self.nombre)+"-"+str(self.estado)
    
class Arriendo(models.Model):
    fecha_in = models.DateField()
    fecha_out = models.DateField(null=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    multa = models.IntegerField()
    
    def __str__(self):
        return str(self.fecha_in)+"-"+str(self.fecha_out)+"-"+str(self.libro)+"-"+str(self.cliente)+"-"+str(self.multa)
    
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=20)
    password_usuario = models.CharField(max_length=128)

    def __str__(self):
        return str(self.nombre_usuario) + " - " + str(self.password_usuario)