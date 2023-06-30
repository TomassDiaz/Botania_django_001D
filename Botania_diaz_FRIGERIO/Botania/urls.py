from django.urls import path
from . import views


urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path("crud", views.crud, name="crud"),
    path("crudTipo", views.crudTipo, name="crudTipo"),
    path('nosotros', views.nosotros, name='nosotros'),
    path('suscripcion', views.suscripcion, name='suscripcion'),
    path('registrar', views.registrar, name='registrar'),
    path('delUser', views.delUser, name='delUser'),
    path('editUser', views.editUser, name='editUser'),
    path("tipoUser_add", views.tipoUser_add, name="tipoUser_add"),
    path('productos', views.productos, name='productos'),
    path('miperfil', views.miperfil, name='miperfil'),
    path('iniciarsesion', views.iniciarsesion, name='iniciarsesion'),
    path('carrito', views.carrito, name='carrito'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('catalogo/agregar', views.agregar_catalogo, name='agregar_catalogo'),
    path('catalogo/modificar', views.modificar_catalogo, name='modificar_catalogo'),
    path('eliminar/<str:pk>', views.eliminar_catalogo, name='eliminar_catalogo'),
    path('modificar/<str:pk>', views.modificar_catalogo, name='modificar_catalogo'),
]
