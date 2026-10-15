from django.shortcuts import render
from gestion.models import Autor, Editorial, Genero, Cliente, Libro, Arriendo, Usuario
from django.contrib.auth.hashers import check_password

def mostrarIndex(request):
    return render(request, 'index.html')

#--------------------------------------------------------------------------------------------------------

def iniciarSesion(request):
    if request.method == "POST":
        nom = request.POST["txtusu"].upper()
        pas = request.POST["txtpas"]

        try:
            usuario = Usuario.objects.get(nombre_usuario=nom)

            if check_password(pas, usuario.password_usuario):
                request.session["estadoSesion"] = True
                request.session["idUsuario"] = usuario.id
                request.session["nomUsuario"] = usuario.nombre_usuario

                datos = {"nomUsuario": usuario.nombre_usuario}

                if usuario.nombre_usuario == "ADMINISTRADOR":
                    return render(request, "menu_admin.html", datos)
                else:
                    return render(request, "menu_usuario.html", datos)
            else:
                return render(request, "index.html", {"r2": "Error de usuario y/o contraseña."})

        except Usuario.DoesNotExist:
            return render(request, "index.html", {"r2": "Error de usuario y/o contraseña."})

    return render(request, "index.html", {"r2": "No se puede procesar la solicitud."})


def cerrarSesion(request):
    try:
        del request.session["estadoSesion"]
        del request.session["idUsuario"]
        del request.session["nomUsuario"]

        return render(request, 'index.html')
    except:
        return render(request, 'index.html')

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

def mostrarMenuAdmin(request):
    estadoSesion = request.session.get("estadoSesion")
    nomUsuario = request.session.get("nomUsuario")

    if estadoSesion is True:
        if nomUsuario == "ADMINISTRADOR":
            datos = { 'nomUsuario' : nomUsuario }
            return render(request, 'menu_admin.html', datos)
        else:
            datos = { 'r2' : 'No Tiene Permisos Suficientes Para Acceder!!' }
            return render(request, 'index.html', datos)
    else:
        datos = { 'r2' : 'Debe Iniciar Sesión Para Acceder!!' }
        return render(request, 'index.html', datos)

def mostrarMenuUsuario(request):
    estadoSesion = request.session.get("estadoSesion")
    nomUsuario = request.session.get("nomUsuario")

    if estadoSesion is True:
        if nomUsuario.upper() != "ADMINISTRADOR":
            datos = { 'nomUsuario' : nomUsuario }
            return render(request, 'menu_usuario.html', datos)
        else:
            datos = { 'r2' : 'No Tiene Permisos Suficientes Para Acceder!!' }
            return render(request, 'index.html', datos)
    else:
        datos = { 'r2' : 'Debe Iniciar Sesión Para Acceder!!' }
        return render(request, 'index.html', datos)



############################# AUTOR ############################################
def mostrarRegistrarAutor(request):
    return render(request, 'registrar_autor.html')

def insertarAutor(request):
    nom = request.POST['txtnom']
    aut = Autor(nombre = nom)
    aut.save()
    
    datos = {'r':'Autor almacenado correctamente!'}
    return render(request, 'registrar_autor.html', datos)
    
def mostrarActualizarAutor(request, id):
    aut = Autor.objects.get(id=id)
    datos = {'aut':aut}
    return render(request, 'actualizar_autor.html', datos)
    
def ActualizarAutor(request,id):
    nom = request.POST['txtnom']
    aut = Autor.objects.get(id=id)
    aut.nombre = nom
    aut.save()
    
    aut = Autor.objects.all().values()
    datos = {'aut':aut, 'r':'Autor actualizado correctamente!'}
    return render(request, 'listado_autor.html', datos)

def mostrarListadoAutor(request):
    aut = Autor.objects.all().values()
    datos = {'aut':aut}
    return render(request, 'listado_autor.html', datos)

def eliminarAutor(request, id):
    aut = Autor.objects.get(id=id)
    aut.delete()
    aut = Autor.objects.all().values()
    datos = {'aut':aut, 'r':'Autor eliminado correctamente!'}
    return render(request, 'listado_autor.html', datos)

########################## Editorial ##################################

def mostrarRegistrarEditorial(request):
    return render(request, 'registrar_editorial.html')

def insertarEditorial(request):
    nom = request.POST['txtnom']
    edi = Editorial(nombre = nom)
    edi.save()
    
    datos = {'r':'Editorial almacenada correctamente!'}
    return render(request, 'registrar_editorial.html', datos)
    
def mostrarActualizarEditorial(request, id):
    edi = Editorial.objects.get(id=id)
    datos = {'edi':edi}
    return render(request, 'actualizar_editorial.html', datos)
    
def ActualizarEditorial(request,id):
    nom = request.POST['txtnom']
    edi = Editorial.objects.get(id=id)
    edi.nombre = nom
    edi.save()
    
    edi = Editorial.objects.all().values()
    datos = {'edi':edi, 'r':'Editorial actualizada correctamente!'}
    return render(request, 'listado_editorial.html', datos)

def mostrarListadoEditorial(request):
    edi = Editorial.objects.all().values()
    datos = {'edi':edi}
    return render(request, 'listado_editorial.html', datos)

def eliminarEditorial(request, id):
    edi = Editorial.objects.get(id=id)
    edi.delete()
    edi = Editorial.objects.all().values()
    datos = {'edi':edi, 'r':'Editorial eliminada correctamente!'}
    return render(request, 'listado_editorial.html', datos)

############################# GENERO ################################

def mostrarRegistrarGenero(request):
    return render(request, 'registrar_genero.html')

def insertarGenero(request):
    nom = request.POST['txtnom']
    gen = Genero(nombre = nom)
    gen.save()
    
    datos = {'r':'Genero almacenado correctamente!'}
    return render(request, 'registrar_genero.html', datos)
    
def mostrarActualizarGenero(request, id):
    gen = Genero.objects.get(id=id)
    datos = {'gen':gen}
    return render(request, 'actualizar_genero.html', datos)
    
def ActualizarGenero(request,id):
    nom = request.POST['txtnom']
    gen = Genero.objects.get(id=id)
    gen.nombre = nom
    gen.save()
    
    gen = Genero.objects.all().values()
    datos = {'gen':gen, 'r':'Genero actualizado correctamente!'}
    return render(request, 'listado_genero.html', datos)

def mostrarListadoGenero(request):
    gen = Genero.objects.all().values()
    datos = {'gen':gen}
    return render(request, 'listado_genero.html', datos)

def eliminarGenero(request, id):
    gen = Genero.objects.get(id=id)
    gen.delete()
    gen = Genero.objects.all().values()
    datos = {'gen':gen, 'r':'Genero eliminado correctamente!'}
    return render(request, 'listado_genero.html', datos)

############################# CLIENTE ################################

def mostrarRegistrarCliente(request):
    return render(request, 'registrar_cliente.html')

def insertarCliente(request):
    r = request.POST['txtrut']
    nom = request.POST['txtnom']
    est = request.POST['opest']
    cli = Cliente(rut = r, nombre = nom, estado = est)
    cli.save()
    
    datos = {'r':'Cliente almacenado correctamente!'}
    return render(request, 'registrar_cliente.html', datos)
    
def mostrarActualizarCliente(request, r):
    cli = Cliente.objects.get(rut=r)
    datos = {'cli':cli}
    return render(request, 'actualizar_cliente.html', datos)
    
def ActualizarCliente(request,r):
    nom = request.POST['txtnom']
    est = request.POST['opest']
    cli = Cliente.objects.get(rut=r)
    cli.nombre = nom
    cli.estado = est
    cli.save()
    
    cli = Cliente.objects.all().values()
    datos = {'cli':cli, 'r':'Cliente actualizado correctamente!'}
    return render(request, 'listado_cliente.html', datos)

def mostrarListadoCliente(request):
    cli = Cliente.objects.all().values()
    datos = {'cli':cli}
    return render(request, 'listado_cliente.html', datos)

def eliminarCliente(request, r):
    cli = Cliente.objects.get(rut=r)
    cli.delete()
    cli = Cliente.objects.all().values()
    datos = {'cli':cli, 'r':'Cliente eliminado correctamente!'}
    return render(request, 'listado_cliente.html', datos)

############################# LIBRO #################################

def mostrarRegistrarLibro(request):
    aut = Autor.objects.all()
    edi = Editorial.objects.all()
    gen = Genero.objects.all()
    datos = {'aut':aut, 'edi':edi, 'gen':gen}
    return render(request, 'registrar_libro.html',datos)

def insertarLibro(request):
    tit = request.POST['txttit']
    aut = request.POST['cboaut']
    edi = request.POST['cboedi']
    gen = request.POST['cbogen']
    lib = Libro(titulo=tit, autor_id =aut, editorial_id = edi, genero_id = gen)
    lib.save()
    
    datos = {'r':'Libro almacenado correctamente!'}
    return render(request, 'registrar_libro.html', datos)
    
def mostrarActualizarLibro(request, id):
    aut = Autor.objects.all()
    edi = Editorial.objects.all()
    gen = Genero.objects.all()
    lib = Libro.objects.get(id=id)
    datos = {'lib':lib,'aut':aut, 'edi':edi, 'gen':gen}
    return render(request, 'actualizar_libro.html', datos)
    
def ActualizarLibro(request,id):
    tit = request.POST['txttit']
    aut = request.POST['cboaut']
    edi = request.POST['cboedi']
    gen = request.POST['cbogen']
    
    lib = Libro.objects.get(id=id)
    lib.titulo = tit
    lib.autor_id = aut
    lib.editorial_id = edi
    lib.genero_id = gen
    lib.save()
    
    lib = Libro.objects.all()
    datos = {'lib':lib, 'r':'Libro actualizado correctamente!'}
    return render(request, 'listado_libro.html', datos)

def mostrarListadoLibro(request):
    lib = Libro.objects.all()
    datos = {'lib':lib}
    return render(request, 'listado_libro.html', datos)

def eliminarLibro(request, id):
    lib = Libro.objects.get(id=id)
    lib.delete()
    
    lib = Libro.objects.all()
    datos = {'lib':lib, 'r':'Libro eliminado correctamente!'}
    return render(request, 'listado_libro.html', datos)

############################# ARRIENDO ################################

def mostrarRegistrarArriendo(request):
    lib = Libro.objects.all()
    cli = Cliente.objects.all()
    datos = {'lib':lib ,'cli':cli}
    return render(request, 'registrar_arriendo.html',datos)

def insertarArriendo(request):
    fin = request.POST['txtfin']
    lib = request.POST['cbolib']
    cli = request.POST['cbocli']
    arr = Arriendo(fecha_in=fin,fecha_out=None,libro_id=lib,cliente_id=cli,multa=0)
    arr.save()
    
    datos = {'r':'Arriendo almacenado correctamente!'}
    return render(request, 'registrar_arriendo.html', datos)
    
def mostrarActualizarArriendo(request, id):
    arr = Arriendo.objects.get(id=id)
    lib = Libro.objects.all()
    cli = Cliente.objects.all()
    
    fecha = arr.fecha_in
    dia = ""; mes=""; fecha_final = ""
    
    if fecha.day>=1 and fecha.day<=9:
        dia = "0"+str(fecha.day)
    else:
        dia = str(fecha.day)
        
    if fecha.month>=1 and fecha.month<=9:
        mes = "0"+str(fecha.month)
    else:
        mes = str(fecha.month)
        
    fecha_final = str(fecha.year)+"-"+mes+"-"+dia
    
    datos = {'arr':arr,'fecha':fecha_final,'lib':lib,'cli':cli}
    return render(request, 'actualizar_arriendo.html', datos)
    
def ActualizarArriendo(request,id):
    fin = request.POST['txtfin']
    lib = request.POST['cbolib']
    cli = request.POST['cbocli']
    arr = Arriendo.objects.get(id=id)
    arr.fecha_in = fin
    arr.libro_id = lib
    arr.cliente_id = cli
    arr.save()
    
    arr = Arriendo.objects.all()
    datos = {'arr':arr, 'r':'Arriendo actualizado correctamente!'}
    return render(request, 'listado_arriendo.html', datos)

def mostrarListadoArriendo(request):
    arr = Arriendo.objects.all()
    datos = {'arr':arr}
    return render(request, 'listado_arriendo.html', datos)

def eliminarArriendo(request, id):
    arr = Arriendo.objects.get(id=id)
    arr.delete()
    arr = Arriendo.objects.all()
    datos = {'arr':arr, 'r':'Arriendo eliminado correctamente!'}
    return render(request, 'listado_arriendo.html', datos)


from django.utils import timezone
def devolverArriendo(request,id):
    arr = Arriendo.objects.get(id=id)
    fecha_actual = timezone.now().date()
    
    fecha_inicio = arr.fecha_in
    diferencia = fecha_actual - fecha_inicio
    dias_diferencia = int(diferencia.days)
    
    mul = 0
    if dias_diferencia > 3:
        mul = 3000 * (dias_diferencia-3)
    
    arr.fecha_out = fecha_actual
    arr.multa = mul
    arr.save()
    
    arr = Arriendo.objects.all()
    datos = {'arr':arr, 'r':'Arriendo actualizado correctamente!'}
    return render(request, 'listado_arriendo.html', datos)