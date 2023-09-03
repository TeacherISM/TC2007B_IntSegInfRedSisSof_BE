from django.utils import timezone
from django.db import models
from datetime import timedelta

# Create your models here.
class HomeUser(models.Model):
    # Login Information
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    pass_phase = models.CharField(max_length = 255)
    
    # User Information
    full_name = models.CharField(max_length = 255)  # divide in name(s) and other?
    email = models.EmailField(null = True)
    created_at = models.DateTimeField(default = timezone.now())
    last_login = models.DateTimeField(null = True)
    time_spended = models.DurationField(default = timedelta(days = 0, hours = 0, minutes = 0, seconds = 0))
    rol = models.CharField(max_length = 15, choices = (("U", "Usuario"), 
                                                       ("A", "Administrador")), default = "Usuario")
    verified_at = models.DateTimeField(null = True)

    # Data analysis    
    birth = models.DateField(null = True)
    genre = models.CharField(max_length = 255, null = True)
    country = models.CharField(max_length = 255, null = True)      
    institution = models.CharField(max_length = 255, null = True)
    carrer = models.CharField(max_length = 15, choices = (("Ing", "Ingeniería y Ciencias"), 
                                                          ("HumyEdu", "Humanidades y Educación"),
                                                          ("Sociales", "Ciencias Sociales"), 
                                                          ("Salud", "Ciencias de la Salud"),
                                                          ("Arq-Art-Dis", "Arquitectura, Arte y Diseño"),
                                                          ("Negocios", "Negocios")), null = True)

    grade = models.CharField(max_length = 10, choices = (("Pregrado", "Pregrado"), 
                                                         ("Posgrado", "Posgrado"), 
                                                         ("Continua", "Educación continua")), null = True)
    
    
    def __str__(self):
        return self.full_name.__str__()
    
    class Meta:
        app_label = "app1"


class Session(models.Model):
    # Identification
    user = models.ForeignKey(HomeUser, null = False, blank = False, on_delete = models.CASCADE)
    ip_address = models.GenericIPAddressField(null = True, blank = False)

    # Duration
    date_init = models.DateTimeField(null = False, blank = False)
    date_end = models.DateTimeField(null = False, blank = False)

    def __str__(self):
        return self.user.full_name.__str__() + " con dirección IP: " + self.ip_address.__str__()

    class Meta:
        app_label = "app1"


class Survey(models.Model):
    user = models.ForeignKey(HomeUser, null = False, blank = False, on_delete = models.CASCADE)
    date_init = models.DateTimeField(null = False, blank = False)
    date_end = models.DateTimeField(null = False, blank = False)

    # -----------------------------------------------------------------------------------------------
    # Social Entrepreneur Profile
    # -----------------------------------------------------------------------------------------------

    # Autocontrol 
    question1 = models.SmallIntegerField(null = True, blank = False)    # Motivation
    question2 = models.SmallIntegerField(null = True, blank = False)    # Perseverance and resilience
    question3 = models.SmallIntegerField(null = True, blank = False)    # Perseverance and resilience
    question4 = models.SmallIntegerField(null = True, blank = False)    # Tolerance to uncertainty, ambiguity and mastery of stress

    # Leadership
    question5 = models.SmallIntegerField(null = True, blank = False)    # Strategic planning
    question6 = models.SmallIntegerField(null = True, blank = False)    # Communication and persuasion
    question7 = models.SmallIntegerField(null = True, blank = False)    # Communication and persuasion
    question8 = models.SmallIntegerField(null = True, blank = False)    # Mobilize people
    question9 = models.SmallIntegerField(null = True, blank = False)    # Mobilize people
    question10 = models.SmallIntegerField(null = True, blank = False)   # Collaborative working

    # Conscience and social value
    question11 = models.SmallIntegerField(null = True, blank = False)   # Social implication
    question12 = models.SmallIntegerField(null = True, blank = False)   # Social implication
    question13 = models.SmallIntegerField(null = True, blank = False)   # Empathy
    question14 = models.SmallIntegerField(null = True, blank = False)   # Identification of social/environmental problems
    question15 = models.SmallIntegerField(null = True, blank = False)   # Identification of social/environmental problems
    question16 = models.SmallIntegerField(null = True, blank = False)   # Sustainability orientation
    question17 = models.SmallIntegerField(null = True, blank = False)   # Ethical sense

    # Social innovation and financial sustainability
    question18 = models.SmallIntegerField(null = True, blank = False)   # Creativity
    question19 = models.SmallIntegerField(null = True, blank = False)   # Economic and financial literacy
    question20 = models.SmallIntegerField(null = True, blank = False)   # Economic and financial literacy
    question21 = models.SmallIntegerField(null = True, blank = False)   # Economic and financial literacy
    question22 = models.SmallIntegerField(null = True, blank = False)   # Valuation of ideas, results and impacts on the environment and people
    question23 = models.SmallIntegerField(null = True, blank = False)   # Learning and adaptability
    question24 = models.SmallIntegerField(null = True, blank = False)   # Management of limited resources for social projects

    # -----------------------------------------------------------------------------------------------
    # Complex Thinking 
    # -----------------------------------------------------------------------------------------------

    # Systemic thinking
    question25 = models.SmallIntegerField(null = True, blank = False)   # Knowledge
    question26 = models.SmallIntegerField(null = True, blank = False)   # Knowledge
    question27 = models.SmallIntegerField(null = True, blank = False)   # Skills
    question28 = models.SmallIntegerField(null = True, blank = False)   # Skills
    question29 = models.SmallIntegerField(null = True, blank = False)   # Attitudes and values
    question30 = models.SmallIntegerField(null = True, blank = False)   # Attitudes and values

    # Scientific thinking
    question31 = models.SmallIntegerField(null = True, blank = False)   # Knowledge
    question32 = models.SmallIntegerField(null = True, blank = False)   # Knowledge
    question33 = models.SmallIntegerField(null = True, blank = False)   # Knowledge
    question34 = models.SmallIntegerField(null = True, blank = False)   # Skills
    question35 = models.SmallIntegerField(null = True, blank = False)   # Skills
    question36 = models.SmallIntegerField(null = True, blank = False)   # Skills
    question37 = models.SmallIntegerField(null = True, blank = False)   # Attitudes and values

    # Critical thinking
    question38 = models.SmallIntegerField(null = True, blank = False)   # Knowledge
    question39 = models.SmallIntegerField(null = True, blank = False)   # Knowledge
    question40 = models.SmallIntegerField(null = True, blank = False)   # Skills
    question41 = models.SmallIntegerField(null = True, blank = False)   # Skills
    question42 = models.SmallIntegerField(null = True, blank = False)   # Attitudes and values
    question43 = models.SmallIntegerField(null = True, blank = False)   # Attitudes and values

    # Innovative thinking
    question44 = models.SmallIntegerField(null = True, blank = False)   # Knowledge
    question45 = models.SmallIntegerField(null = True, blank = False)   # Knowledge
    question46 = models.SmallIntegerField(null = True, blank = False)   # Skills
    question47 = models.SmallIntegerField(null = True, blank = False)   # Skills
    question48 = models.SmallIntegerField(null = True, blank = False)   # Skills
    question49 = models.SmallIntegerField(null = True, blank = False)   # Attitudes and values

    class Meta:
        app_label = "app1"


class Deliver(models.Model):
    user = models.ForeignKey(HomeUser, null = False, blank = False, on_delete = models.CASCADE) # ¿Qué desaparezcan las entregas de un usuario cuando lo eliminamos inmediatamente?
    date = models.DateTimeField(null = False, blank = False)

    # Types of files that an user can deliver
    text_file = models.TextField(null = True, blank = False)
    image_file = models.ImageField(null = True, blank = False)
    url_file = models.URLField(null = True, blank = False)
    file = models.FileField(null = True, blank = False)

    class Meta:
        app_label = "app1"
