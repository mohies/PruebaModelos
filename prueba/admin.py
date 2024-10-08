from django.contrib import admin
from .models import *
	
# Register your models here.
models = [Biblioteca, Autor, Libro,Cliente,DatosCliente]

# Registro de modelos en el admin
for model in models:    
    admin.site.register(model)
