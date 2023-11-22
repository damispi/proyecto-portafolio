from django.shortcuts import render
from .models import Project

def portfolio (request):
    #traer todos los datos de la base de datos
    projects=Project.objects.all()

    return render(request,'portfolio/portfolio.html',{'projects':projects})


# Create your views here.
