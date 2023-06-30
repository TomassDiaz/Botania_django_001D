from django.shortcuts import render, redirect
from .models import Usuario, tipoUsuario, Catalogo
from .forms import UsuarioForm, tipoForm, CatalogoForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/inicio.html", context)

def crud(request):
    usuario = Usuario.objects.all()
    context = {"usuario": usuario}
    return render(request, "pages/miperfil.html", context)

def crudTipo(request):
    tipos = tipoUsuario.objects.all()
    context = {"tipo": tipos}
    return render(request, "pages/tipoUser_list.html", context)

def nosotros(request):
    context = { }
    return render(request, "pages/nosotros.html", context)

def suscripcion(request):
    context = { }
    return render(request, "pages/suscripcion.html", context)

def productos(request):
    context = { }
    return render(request, "pages/productos.html", context)

def miperfil(request):
    context = { }
    return render(request, "pages/miperfil.html", context)

def iniciarsesion(request):
    context = { }
    return render(request, "pages/iniciarsesion.html", context)

def carrito(request):
    context = { }
    return render(request, "pages/carrito.html", context)

def registrar(request):
    if request.method != "POST":
        tipo = tipoUsuario.objects.all()
        context = {"tipo": tipo}
        return render(request, "pages/registrar.html", context)
    else:
        nombre = request.POST["nombre"]
        apaterno = request.POST["apaterno"]
        amaterno = request.POST["amaterno"]
        correo = request.POST["correo"]
        clave = request.POST[" clave"]
        direccion = request.POST["direccion "]
        telefono = request.POST["telefono "]
        region = request.POST["region "]
        provincia = request.POST["provincia "]
        comuna = request.POST["comuna "]
        codpos = request.POST["codpos"]
        tipoUsuario = request.POST["tipoUsuario"]
       

        objTipo = tipoUsuario.objects.get(idtipoUsuario=tipo)
        objUsuario = Usuario.objects.create(
            nombre = nombre,
            apaterno = apaterno,
            amaterno = amaterno,
            correo = correo,
            clave = clave,
            direccion = direccion,
            telefono = telefono,
            region = region,
            provincia = provincia,
            comuna = comuna,
            codpos = codpos,
            activo=1,
        )
        objUsuario.save()
        context = {"mensaje": "Registrado "}
        return render(request, "pages/registrar.html", context)

def delUser(request, pk):
    context = {}
    try:
        user = Usuario.objects.get(rut=pk)
        user.delete()
        usuarios = Usuario.objects.all()
        context = {"mensaje": "Eliminado", "usuario": usuarios}
        return render(request, "pages/inicio.html", context)
    except:
        usuarios = Usuario.objects.all()
        context = {"mensaje": "Error", "usuario": usuarios}
        return render(request, "pages/miperfil.html", context)

def editUser(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        apaterno = request.POST["apaterno"]
        amaterno = request.POST["amaterno"]
        correo = request.POST["correo"]
        clave = request.POST[" clave"]
        direccion = request.POST["direccion "]
        telefono = request.POST["telefono "]
        region = request.POST["region "]
        provincia = request.POST["provincia "]
        comuna = request.POST["comuna "]
        codpos = request.POST["codpos"]
        
        objTipo = tipoUsuario.objects.get(idTipoUsuario=tipo)

        user = Usuario()
        user.nombre = nombre
        user.apaterno = apaterno
        user.amaterno = amaterno
        user.correo = correo
        user.clave = clave
        user.direccion = direccion
        user.telefono = telefono
        user.region = region
        user.provincia = provincia
        user.comuna = comuna
        user.codpos = codpos
        user.activo=1
        
        user.save()

        tipo = tipoUsuario.objects.all()
        context = {"mensaje": "Modificado", "tipo": tipo, "usuario": user}

        return render(request, "pages/miperfil.html", context)
    else:
        usuarios = Usuario.objects.all()
        context = {"usuario": usuarios}
        return render(request, "pages/miperfil.html", context)



def tipoUser_add(request):
    catalogo = Catalogo.objects.all()
    context = {
        "catalogo": catalogo
        }
    return render(request, "catalogo/lista.html", context)

def catalogo(request):
    catalogo = Catalogo.objects.all()
    context = {
        "catalogo": catalogo
        }
    return render(request, "catalogo/lista.html", context)

def agregar_catalogo(request):
    form = CatalogoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("catalogo")
    context = {  "form": form}
    return render(request, "catalogo/agregar.html", context)

def modificar_catalogo(request):
    context = { }
    return render(request, "catalogo/modificar.html", context)

def eliminar_catalogo(request, pk):
    catalogo = Catalogo.objects.get(id=pk)
    catalogo.delete()
    return redirect("catalogo")

def modificar_catalogo(request, pk):
    catalogo = Catalogo.objects.get(id=pk)
    form = CatalogoForm(request.POST, instance=catalogo)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('catalogo')
    context = {
        "form": form
    }
    return render(request, "catalogo/modificar.html", context)





##CARRITO

def carrito(request):
    items = items.objects.filter(usuario = request.user)
    return render(request, "pages/carrito.html", {'items': items})

def agregar_al_carrito(request, producto_id):
    producto = producto.objects.get(pk=producto)

##CIERRE CARRITO