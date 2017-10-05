from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import EmailValidator

class User(models.Model):    
    fullName = models.CharField(max_length=30)
    email = models.EmailField(unique=True, validators=[EmailValidator(message="E-mail inválido")])
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.fullName


class UserSkills(User): 

    html = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(10)],error_messages={'max_value': ('O valor deve estar entre 0 e 10')})
    css = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(10)],error_messages={'max_value': ('O valor deve estar entre 0 e 10')})
    javascript = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(10)],error_messages={'max_value': ('O valor deve estar entre 0 e 10')})
    python = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(10)],error_messages={'max_value': ('O valor deve estar entre 0 e 10')})
    django = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(10)],error_messages={'max_value': ('O valor deve estar entre 0 e 10')})
    iosDevelopment = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(10)],error_messages={'max_value': ('O valor deve estar entre 0 e 10')})
    androidDevelopment = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(10)],error_messages={'max_value': ('O valor deve estar entre 0 e 10')})

    def publish(self):
        self.save()

    def __str__(self):
        return self.fullName

    def getEmail(self):
        self.email