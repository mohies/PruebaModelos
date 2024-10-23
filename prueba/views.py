from django.shortcuts import render
from .models import *
from django.db.models import Q,Prefetch
from django.db.models import Avg,Max,Min
from django.views.defaults import page_not_found
# Create your views here.
def index(request):
    bibliotecas = Biblioteca.objects.all()  # Obtiene todas las bibliotecas
    return render(request, 'index.html', {'bibliotecas': bibliotecas})

def listar_libros(request):
    libros=Libro.objects.select_related("Biblioteca").prefetch_related("autores")
    libros=libros.all()
    return render(request,'prueba/lista.html',{"libros_mostrar":libros})
    
def dame_libro(request,id_libro):
    libro=Libro.objects.select_related("Biblioteca").prefetch_related("autores").get(id=id_libro)
    return render(request,'prueba/libro.html',{"libro_mostrar":libro})

def dame_libros_fecha(request,anyo_libro,mes_libro):
    libros=Libro.objects.select_related("Biblioteca").prefetch_related("autores")
    libros=libros.filter(fecha_publicacion__year=anyo_libro,fecha_publicacion__month=mes_libro)
    return render(request,'prueba/libro.html',{"libro_mostrar":libros})  

def dame_libros_idioma(request,tipo):
    libros=Libro.objects.select_related("Biblioteca").prefetch_related("autores")
    libros=libros.filter(Q(tipo=tipo) | Q(tipo="ES") | Q(fecha_publicacion__year="2024") ).order_by("fecha_publicacion") #q de query es para buscar y si quiero añadir otra condicion puedo ponerla
    return render(request,'prueba/lista.html',{"libros_mostrar":libros})
  
def dame_libros_biblioteca(request,id_biblioteca,texto_libro):
    libros=Libro.objects.select_related("Biblioteca").prefetch_related("autores")
    libros=libros.filter(Biblioteca=id_biblioteca).filter(descripcion__contains=texto_libro).order_by("-nombre")
    return render(request,'prueba/lista.html',{"libros_mostrar":libros})  
def dame_ultimo_cliente_libro(request,libro):
    cliente=Cliente.objects.filter(prestamos__libro=libro).order_by("-prestamos__fecha_prestamo")[:1].get()
    return render(request,'prueba/cliente.html',{"cliente":cliente})   #esto es para acceder a las talas intermedias
def libros_no_prestados(request):
    libros=Libro.objects.select_related("Biblioteca").prefetch_related("autores")
    libros=libros.filter(prestamos=None)
    return render(request,'prueba/lista.html',{"libros_mostrar":libros})  
def dame_agrupaciones_puntos_cliente(request):
    resultado = Cliente.objects.aggregate(Avg("puntos"), Max("puntos"), Min("puntos"))
    media=resultado["puntos__avg"]
    maximo=resultado["puntos__max"]
    minimo=resultado["puntos__min"]
    return render(request,'prueba/agrupaciones.html',{"media":media,"maximo":maximo,"minimo":minimo})
def dame_biblioteca(request,id_biblioteca):
    biblioteca=Biblioteca.objects.prefetch_related(Prefetch("libros_biblioteca")).get(id=id_biblioteca)
    return render(request,'prueba/biblioteca.html',{"biblioteca":biblioteca})

#errores
def mi_error_404(request, exception=None):
    return render(request, 'prueba/errores/404.html', None,None,404)
