from django.shortcuts import render
from .models import *
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request, 'index.html')

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