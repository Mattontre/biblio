from django.core.management.base import BaseCommand
from gestion.models import Editorial,Autor,Genero, Cliente, Usuario, Libro
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        editoriales = [
            Editorial(nombre='Planeta'),
            Editorial(nombre='Zig-Zag'),
            Editorial(nombre='Lom Ediciones'),
        ]
        Editorial.objects.bulk_create(editoriales)
        self.stdout.write(self.style.SUCCESS('Editoriales creadas exitosamente.'))
        
        autores = [
            Autor(nombre='María Luisa Bombal'),
            Autor(nombre='Jorge Luis Borges'),
            Autor(nombre='Isabel Allende'),
        ]
        Autor.objects.bulk_create(autores)
        self.stdout.write(self.style.SUCCESS('Autores creados exitosamente.'))

        genero = [
            Genero(nombre='Terror'),
            Genero(nombre='Suspenso'),
            Genero(nombre='Fantástico'),
        ]
        Genero.objects.bulk_create(genero)
        self.stdout.write(self.style.SUCCESS('Generos creados exitosamente.'))
        
        clientes = [
            Cliente(rut='23456789-0', nombre='Cliente 2', estado='Activo'),
            Cliente(rut='34567890-1', nombre='Cliente 3', estado='Bloqueado'),
            Cliente(rut='45678901-2', nombre='Cliente 4', estado='Activo'),
            Cliente(rut='56789012-3', nombre='Cliente 5', estado='Bloqueado'),
        ]
        Cliente.objects.bulk_create(clientes)
        self.stdout.write(self.style.SUCCESS('Clientes creados exitosamente.'))
        
        Usuarios = [
            Usuario(nombre_usuario='ADMINISTRADOR', password_usuario= make_password("123456")),
            Usuario(nombre_usuario='BIBLIOTECARIO', password_usuario= make_password("123123"))
        ]
        Usuario.objects.bulk_create(Usuarios)
        self.stdout.write(self.style.SUCCESS('usuarios creadas exitosamente.'))
        
        Libros = [
            Libro(titulo='La última niebla', autor_id=1, editorial_id=1, genero_id=2),
            Libro(titulo='Ficciones', autor_id=2, editorial_id=2, genero_id=3),
        ]
        Libro.objects.bulk_create(Libros)
        self.stdout.write(self.style.SUCCESS('Libros creados exitosamente.'))