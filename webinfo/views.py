from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm
from .models import Contacto

def home(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            Contacto.objects.create(
                nombre=form.cleaned_data["nombre"],
                email=form.cleaned_data["email"],
                mensaje=form.cleaned_data["mensaje"],
            )
            messages.success(request, "¡Gracias! Recibimos tu consulta.")
            form = ContactForm()  # resetea el formulario

    return render(request, "webinfo/home.html", {"form": form})
