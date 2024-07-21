from django.urls import path, include

from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="inicio"),
    path('complejos/', complejos, name="complejos"),
    
    
    

    path('acerca/', acerca, name="acerca"),
    path('contacto/', contacto, name="contacto"),
    


#___Profesor____

path('profesores/', profesores, name="profesores"),
path('profesorForm/', profesorForm, name="profesorForm"),
path('profesorUpdate/<id_profesor>/', profesorUpdate, name="profesorUpdate"),
path('profesorDelete/<id_profesor>/', profesorDelete, name="profesorDelete"),

#__Profesional__

path('profesionales/', profesionales, name="profesionales"),
path('profesionalForm/', profesionalForm, name="profesionalForm"),
path('profesionalUpdate/<id_profesional>/', profesionalUpdate, name="profesionalUpdate"),
path('profesionalDelete/<id_profesional>/', profesionalDelete, name="profesionalDelete"),

#__Responsable___

path('responsables/', ResponsableList.as_view(), name="responsables"),    
path('responsableCreate/', ResponsableCreate.as_view(), name="responsableCreate"), 
path('responsableUpdate/<int:pk>/', ResponsableUpdate.as_view(), name="responsableUpdate"), 
path('responsableDelete/<int:pk>/', ResponsableDelete.as_view(), name="responsableDelete"),

#____Buscar__

path('buscarComplejos/', buscarComplejos, name="buscarComplejos"),
path('encontrarCursos/', encontrarComplejos, name="encontrarComplejos"),

#Registro, login, logout
path('login/', loginRequest, name="login"),
path('logout/', LogoutView.as_view(template_name="repositorio/logout.html"), name="logout"),
path('registro/', registro, name="registro"),

#Editar Perfil
path('perfil/', editarPerfil, name="perfil"),
path('<int:pk>/password/', CambiarClave.as_view(), name="cambiarClave"),

#Avatar
path('agregar_avatar/', agregarAvatar, name="agregar_avatar")]