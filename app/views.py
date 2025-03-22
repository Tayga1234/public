from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AbonneForm
from .models import *

def index(request):
    # Récupérer les objets avant le POST
    countdown_event = Countdown.objects.last() 
    accueil = Accueil.objects.first() 
    topbar = Topbar.objects.first() 
    about = About.objects.first() 
    footer = Footer.objects.first()
    evaluation = Evaluation.objects.first() 

    if request.method == 'POST':
        form = AbonneForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            whatsapp = form.cleaned_data['whatsapp']

            if Abonne.objects.filter(email=email).exists():
                messages.error(request, 'Cet email est déjà inscrit.')
            elif Abonne.objects.filter(whatsapp=whatsapp).exists():
                messages.error(request, 'Ce numéro WhatsApp est déjà inscrit.')
            else:
                # Enregistrer le nouvel abonné
                abonne = form.save()

                # Vérifier que accueil et footer existent pour éviter une erreur
                accueil_data = {
                    'logo': {'url': accueil.logo.url} if accueil else {'url': ''},
                    'site_name': accueil.site_name if accueil else 'Notre Site',
                }
                footer_data = {
                    'contact_email': footer.contact_email if footer else '',
                    'contact_phone': footer.contact_phone if footer else '',
                    'contact_address': footer.contact_address if footer else '',
                }

                # Générer le contenu HTML et texte brut
                html_content = render_to_string('mail.html', {'nom': abonne.nom, 'accueil': accueil_data, 'footer': footer_data})
                text_content = strip_tags(html_content)  # Convertit en texte brut (au cas où)

                # Envoyer l'email
                subject = "Bienvenue à notre newsletter ! 🎉"
                from_email = 'b.landry.shein@gmail.com'
                recipient_list = [abonne.email]

                email_message = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
                email_message.attach_alternative(html_content, "text/html")
                email_message.send()

                messages.success(request, 'Merci pour votre abonnement ! Un email de bienvenue vous a été envoyé.')
            return redirect('index')

    else:
        form = AbonneForm()

    context = {
        'date': countdown_event.date if countdown_event else None,
        'vague_name': countdown_event.vague_name if countdown_event else None,
        'accueil': accueil,
        'topbar': topbar,
        'about': about,
        'footer': footer, 
        'evaluation': evaluation,
        'form': form,  # Ajouter le formulaire au contexte
    }
    return render(request, 'index.html', context)
