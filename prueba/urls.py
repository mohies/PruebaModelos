from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('prueba/lista',views.listar_libros,name='lista_libros'),
    path("prueba/libro/<int:id_libro>/", views.dame_libro,name="dame_libro"),
    path("prueba/libro/<int:anyo_libro>/<int:mes_libro>", views.dame_libros_fecha,name="dame_libros_fecha"),
    path("prueba/libro/<str:tipo>/", views.dame_libros_idioma,name="dame_libros_idioma"),
    path("prueba/<int:id_biblioteca>/libro/<str:texto_libro>",views.dame_libros_biblioteca,name="dame_libros_biblioteca"),
    

]
