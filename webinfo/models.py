from django.db import models

class Contacto(models.Model):
    ESTADO_CHOICES = [
        ("pendiente", "Pendiente"),
        ("atendido", "Atendido"),
    ]

    nombre = models.CharField(max_length=80)
    email = models.EmailField()
    mensaje = models.TextField(max_length=2000)
    creado_en = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default="pendiente")

    def __str__(self):
        return f"{self.nombre} - {self.email}"
