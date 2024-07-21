from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render (request, "repositorio/index.html")

@login_required
def complejos(request):
    contexto = {"complejos": Complejo.objects.all()}
    return render(request, "repositorio/complejos.html", contexto)

def acerca(request):
    return render(request, "repositorio/acerca.html")

def contacto(request):
    return render(request, "repositorio/contacto.html")

# Profesores
@login_required
def profesores(request):
    contexto = {"profesores": Profesor.objects.all()}
    return render(request, "repositorio/profesores.html", contexto)

@login_required
def profesorForm(request):
    if request.method== "POST":
        miForm = ProfesorForm(request.POST)
        if miForm.is_valid():
            profesor_nombre = miForm.cleaned_data.get("nombre")
            profesor_apellido = miForm.cleaned_data.get("apellido")
            profesor_complejo = miForm.cleaned_data.get("complejo")

            profesor = Profesor(nombre=profesor_nombre, 
                          apellido=profesor_apellido,
                          complejo=profesor_complejo)
            profesor.save()
            contexto = {"profesores": Profesor.objects.all() }
            return render(request, "repositorio/profesores.html", contexto)
        
    else:
        miForm = ProfesorForm()
    
    return render(request, "repositorio/profesorForm.html", {"form": miForm})

@login_required
def profesorUpdate(request, id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    if request.method == "POST":
        miForm = ProfesorForm(request.POST)
        if miForm.is_valid():
            profesor.nombre = miForm.cleaned_data.get("nombre")
            profesor.apellido = miForm.cleaned_data.get("apellido")
            profesor.complejo = miForm.cleaned_data.get("complejo")
            profesor.save()
            contexto = {"profesores": Profesor.objects.all() }
            return render(request, "repositorio/profesores.html", contexto)       
    else:
        miForm = ProfesorForm(initial={"nombre": profesor.nombre, "apellido": profesor.apellido, "complejo": profesor.complejo})  
    
    return render(request, "repositorio/ProfesorForm.html", {"form": miForm})

@login_required
def profesorDelete(request, id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    profesor.delete()
    contexto = {"profesores": Profesor.objects.all() }
    return render(request, "repositorio/profesores.html", contexto)

# Profesionales
@login_required
def profesionales(request):
    contexto = {"profesionales": Profesional.objects.all()}
    return render(request, "repositorio/profesionales.html", contexto)

@login_required
def profesionalForm(request):
    if request.method== "POST":
        miForm = ProfesionalForm(request.POST)
        if miForm.is_valid():
            profesional_nombre = miForm.cleaned_data.get("nombre")
            profesional_apellido = miForm.cleaned_data.get("apellido")
            profesional_profesion = miForm.cleaned_data.get("profesion")

            profesional = Profesional(nombre=profesional_nombre, 
                          apellido=profesional_apellido,
                          profesion=profesional_profesion)
            profesional.save()
            contexto = {"profesionales": Profesional.objects.all() }
            return render(request, "repositorio/profesionales.html", contexto)
        
    else:
        miForm = ProfesionalForm()
    
    return render(request, "repositorio/profesionalForm.html", {"form": miForm})

@login_required
def profesionalUpdate(request, id_profesional):
    profesional = Profesional.objects.get(id=id_profesional)
    if request.method == "POST":
        miForm = ProfesionalForm(request.POST)
        if miForm.is_valid():
            profesional.nombre = miForm.cleaned_data.get("nombre")
            profesional.apellido = miForm.cleaned_data.get("apellido")
            profesional.profesion = miForm.cleaned_data.get("profesion")
            profesional.save()
            contexto = {"profesionales": Profesional.objects.all() }
            return render(request, "repositorio/profesionales.html", contexto)       
    else:
        miForm = ProfesionalForm(initial={"nombre": profesional.nombre, "apellido": profesional.apellido, "profesion": profesional.profesion})  
    
    return render(request, "repositorio/profesionalForm.html", {"form": miForm})

@login_required
def profesionalDelete(request, id_profesional):
    profesional = Profesional.objects.get(id=id_profesional)
    profesional.delete()
    contexto = {"profesionales": Profesional.objects.all() }
    return render(request, "repositorio/profesionales.html", contexto)

# Responsables

class ResponsableList(LoginRequiredMixin,ListView):
    model = Responsable

class ResponsableCreate(LoginRequiredMixin,CreateView):
    model = Responsable
    fields = ["nombre", "apellido", "posicion"]
    success_url = reverse_lazy("responsables")

class ResponsableUpdate(LoginRequiredMixin,UpdateView):
    model = Responsable
    fields = ["nombre", "apellido", "posicion"]
    success_url = reverse_lazy("responsables")

class ResponsableDelete(LoginRequiredMixin, DeleteView):
    model = Responsable
    success_url = reverse_lazy("responsables")


#Busqueda de complejos
@login_required
def buscarComplejos(request):
    return render(request, "repositorio/buscar.html")

@login_required
def encontrarComplejos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        complejos = Complejo.objects.filter(complejo__icontains=patron)
        contexto = {'complejos': complejos}    
    else:
        contexto = {'complejos': Complejo.objects.all()}
        
    return render(request, "repositorio/complejos.html", contexto)

#Login

def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            
            # Buscar Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            # Fin buscar avatar
            
            return render(request, "repositorio/index.html")
        else:
            return redirect(reverse_lazy('login'))

    else:
        miForm = AuthenticationForm()

    return render(request, "repositorio/login.html", {"form": miForm})

#Registro

def registro(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            #usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('inicio'))
    else:
        miForm = RegistroForm()

    return render(request, "repositorio/registro.html", {"form": miForm}) 
   
#Editar Perfil 

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        miForm = EdicionUsuarioForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = EdicionUsuarioForm(instance=usuario)
    return render(request, "repositorio/editarPerfil.html", {"form": miForm})
    
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "repositorio/cambiar_clave.html"
    success_url = reverse_lazy("inicio")
    
#Avatar

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            
            # Eliminar avatares anteriores
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #__________________________________________
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()

            # Imagen en inicio
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            #____________________________________________________
            return redirect(reverse_lazy("inicio"))
    else:
        miForm = AvatarForm()
    return render(request, "repositorio/agregarAvatar.html", {"form": miForm})    

