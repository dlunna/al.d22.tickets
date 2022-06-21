from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Area(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "area"
        verbose_name_plural = "areas"
        ordering = ["-created"]

    def __str__(self):
        return self.name

class Tipo(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "tipo"
        verbose_name_plural = "tipos"
        ordering = ["-created"]

    def __str__(self):
        return self.name

class Post(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del solicitante")
    area = models.ManyToManyField(Area, verbose_name="Areas", related_name="areas_vinculadas")
    falla = models.TextField(verbose_name="Falla")
    inventario = models.CharField(max_length=200, verbose_name="Número de inventario")
    serie = models.CharField(max_length=200, verbose_name="Número de serie")
    tipo = models.ManyToManyField(Tipo, verbose_name="Tipo de componente", related_name="tipos_vinculados")
    #tipo = models.TextField(verbose_name="Tipo pc, lap")
    solucion = models.TextField(verbose_name="Solución")
    #mantenimiento = models.TextField(verbose_name="Tipo de Mantenimiento")
    #content = RichTextField(verbose_name="Contenido", null=True, blank=True)
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=timezone.now)
    image = models.ImageField(verbose_name="Imagen", upload_to="binnacle", null=True, blank=True)   
    preventivo = models.BooleanField(verbose_name="Activar para mantenimiento preventivo", null=True, blank=True)
    correctivo = models.BooleanField(verbose_name="Activar para mantenimiento correctivo", null=True, blank=True)
    estado = models.BooleanField(verbose_name="Activar para cerrar")
    #On delete - borrar en cascada todos
    #Lo contrario a cascade PROTECT pero debe tener null=True, blank=True
    author = models.ForeignKey (User, verbose_name="Autor", on_delete=models.CASCADE)
    #categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_post")
    

    closed = models.DateField(verbose_name="Fecha de finalización del trabajo", null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ["-created"]

    def __str__(self):
        return self.inventario