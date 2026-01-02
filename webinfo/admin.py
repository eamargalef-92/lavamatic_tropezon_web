from django.contrib import admin
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "email", "creado_en", "estado")
    list_filter = ("estado", "creado_en")  # ✅ filtro por estado a la derecha
    search_fields = ("nombre", "email", "mensaje")

    # ✅ podés editar estado desde la lista (opcional, súper cómodo)
    list_editable = ("estado",)

    # ✅ al abrir un contacto se ve el mensaje completo
    fields = ("nombre", "email", "mensaje", "creado_en", "estado")
    readonly_fields = ("creado_en",)
