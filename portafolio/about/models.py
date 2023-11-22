from django.db import models
#modelo para Formacion
class Course(models.Model):
    title=models.CharField(max_length=150,verbose_name='Titulo')
    degree_title=models.CharField(max_length=300, verbose_name='Titulo Obtenido')
    description=models.TextField(verbose_name='Descripción',default='Default description')
    link=models.URLField(max_length=200,blank='True',null='True', verbose_name='Enlace')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Fecha creación')
    update=models.DateTimeField(auto_now=True,verbose_name='Fecha de modificación')


    class Meta:
        verbose_name='formacion'
        verbose_name_plural='formaciones'
        ordering =['-created']
        def __str__(self):
            return (self.title)

#modelo para skill
# Create your models here.
class Skill(models.Model):
    title=models.CharField(max_length=150,verbose_name='Titulo')
    image=models.ImageField(upload_to='skills', verbose_name='Imagen')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Fecha creación')
    update=models.DateTimeField(auto_now=True,verbose_name='Fecha de modificación')

    class Meta:
        verbose_name='conocimiento'
        verbose_name_plural='conocimientos'
        ordering =['-created']
    def __str__(self):
        return (self.title)