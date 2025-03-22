from django.db import models


   # Les Onglets 
class Topbar(models.Model):   
    onglet1 = models.CharField(max_length=100)
    onglet2 = models.CharField(max_length=100)
    onglet3 = models.CharField(max_length=100)
    onglet4 = models.CharField(max_length=100)
   # Les Onglets 

class Accueil(models.Model):
    # Informations générales
    site_name = models.CharField(max_length=100)
    accueil_text1 = models.TextField()
    accueil_text2 = models.TextField()
    accueil_bouton = models.TextField()
    logo = models.ImageField(upload_to='media/')
    image = models.ImageField(upload_to='media/')

class Countdown(models.Model):
    vague_name = models.CharField(max_length=100)
    date = models.DateTimeField()  # Date for the countdown

    # Section About
class About(models.Model):
    about_title = models.CharField(max_length=200)
    about_description = models.TextField()
    about_image = models.ImageField(upload_to='media/about/')

    # Section Evalution
class Evaluation(models.Model):
    evaluation_title = models.CharField(max_length=200)
    evaluation_description = models.TextField()

    text_calcul = models.TextField()
    description_calcul = models.TextField()

    text_demo = models.TextField()
    image1 = models.ImageField(upload_to='media/evalutation/')
    image2 = models.ImageField(upload_to='media/evalutation/')
    image3 = models.ImageField(upload_to='media/evalutation/')


    # Section Contact
class Footer(models.Model):
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    contact_address = models.CharField(max_length=255)
    

class Abonne(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    date_abonnement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.email})"
