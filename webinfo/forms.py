from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=80,
        widget=forms.TextInput(attrs={"placeholder": "Tu nombre"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "tucorreo@ejemplo.com"})
    )
    mensaje = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={
            "rows": 4,
            "placeholder": "Contanos qué necesitás (tipo de servicio, cantidad, etc.)"
        })
    )
