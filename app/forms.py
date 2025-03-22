

from django import forms
from .models import Abonne
import re
from django.core.exceptions import ValidationError

class AbonneForm(forms.ModelForm):
    class Meta:
        model = Abonne
        fields = ['nom', 'prenom', 'whatsapp', 'email']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'nl-input','placeholder': 'Votre nom', 'required': True}),
            'prenom': forms.TextInput(attrs={'class': 'nl-input', 'placeholder': 'Votre prénom', 'required': True}),
            'whatsapp': forms.TextInput(attrs={'class': 'nl-input', 'placeholder': 'Exemple: +226 00 00 00 00', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'nl-input', 'placeholder': 'Votre email', 'required': True}),
        }
        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'whatsapp': 'Numéro WhatsApp',
            'email': 'Email',
        }
        
        def clean_whatsapp(self):
            whatsapp = self.cleaned_data['whatsapp']
            if not re.match(r'^\+?\d{9,15}$', whatsapp):
                raise ValidationError('Numéro WhatsApp invalide.')
            return whatsapp