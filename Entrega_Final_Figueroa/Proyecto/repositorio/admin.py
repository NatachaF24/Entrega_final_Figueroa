from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Complejo)
admin.site.register(Profesor)
admin.site.register(Profesional)
admin.site.register(Responsable)
