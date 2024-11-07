# delivery/forms.py

from django import forms
from .models import Ordem

class OrderForm(forms.ModelForm):
    class Meta:
        model = Ordem
        fields = ["nome", "endereco", "items"]
