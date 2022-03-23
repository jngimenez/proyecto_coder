from django.contrib import admin

from profesionales.models import cerrajero, estudiante, futbolista

# Register your models here.
admin.site.register(cerrajero)
admin.site.register(futbolista)
admin.site.register(estudiante)

