from django.contrib import admin
from django.urls import path
from gestion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.mostrarIndex),
    path('login', views.iniciarSesion),
    path('logout', views.cerrarSesion),
    
    path('menu_admin', views.mostrarMenuAdmin),
    path('menu_usuario', views.mostrarMenuUsuario),
    
    path('form_registrar_autor', views.mostrarRegistrarAutor),
    path('insertar_autor', views.insertarAutor),
    path('listado_autor', views.mostrarListadoAutor),
    path('form_actualizar_autor/<int:id>', views.mostrarActualizarAutor),
    path('actualizar_autor/<int:id>', views.ActualizarAutor),
    path('eliminar_autor/<int:id>', views.eliminarAutor),
    
    path('form_registrar_editorial', views.mostrarRegistrarEditorial),
    path('insertar_editorial', views.insertarEditorial),
    path('listado_editorial', views.mostrarListadoEditorial),
    path('form_actualizar_editorial/<int:id>', views.mostrarActualizarEditorial),
    path('actualizar_editorial/<int:id>', views.ActualizarEditorial),
    path('eliminar_editorial/<int:id>', views.eliminarEditorial),
    
    path('form_registrar_genero', views.mostrarRegistrarGenero),
    path('insertar_genero', views.insertarGenero),
    path('listado_genero', views.mostrarListadoGenero),
    path('form_actualizar_genero/<int:id>', views.mostrarActualizarGenero),
    path('actualizar_genero/<int:id>', views.ActualizarGenero),
    path('eliminar_genero/<int:id>', views.eliminarGenero),
    
    path('form_registrar_cliente', views.mostrarRegistrarCliente),
    path('insertar_cliente', views.insertarCliente),
    path('listado_cliente', views.mostrarListadoCliente),
    path('form_actualizar_cliente/<str:r>', views.mostrarActualizarCliente),
    path('actualizar_cliente/<str:r>', views.ActualizarCliente),
    path('eliminar_cliente/<str:r>', views.eliminarCliente),
    
    path('form_registrar_libro', views.mostrarRegistrarLibro),
    path('insertar_libro', views.insertarLibro),
    path('listado_libro', views.mostrarListadoLibro),
    path('form_actualizar_libro/<int:id>', views.mostrarActualizarLibro),
    path('actualizar_libro/<int:id>', views.ActualizarLibro),
    path('eliminar_libro/<int:id>', views.eliminarLibro),
    
    path('form_registrar_arriendo', views.mostrarRegistrarArriendo),
    path('insertar_arriendo', views.insertarArriendo),
    path('listado_arriendo', views.mostrarListadoArriendo),
    path('form_actualizar_arriendo/<int:id>', views.mostrarActualizarArriendo),
    path('actualizar_arriendo/<int:id>', views.ActualizarArriendo),
    path('eliminar_arriendo/<int:id>', views.eliminarArriendo),
    path('devolver_arriendo/<int:id>', views.devolverArriendo),
]

