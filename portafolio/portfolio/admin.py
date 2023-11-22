from django.contrib import admin
from .models import Project
#Necesario para poder ver los campos ocultos created update
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'update')

admin.site.register(Project,ProjectAdmin)
# configuracion extendida para camiar el nombre de la aplicacion en admin
