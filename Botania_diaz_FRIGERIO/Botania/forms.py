from .models import Usuario, tipoUsuario, Catalogo
from django.forms import ModelForm


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"


class tipoForm(ModelForm):
    class Meta:
        model = tipoUsuario
        fields = [
            "tipoUsuario",
        ]
        labels = {
            "tipoUsuario": "tipoUsuario",
        }

class CatalogoForm(ModelForm):
    class Meta:
        model = Catalogo
        fields = "__all__"
