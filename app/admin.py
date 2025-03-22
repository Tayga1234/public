from django.contrib import admin

# Register your models here.
from .models import *

# Enregistrer chaque modèle pour qu'il soit visible et gérable dans l'interface d'administration
admin.site.register(Topbar)
admin.site.register(Accueil)
admin.site.register(About)
admin.site.register(Evaluation)
admin.site.register(Footer)
admin.site.register(Countdown)
admin.site.register(Abonne)

