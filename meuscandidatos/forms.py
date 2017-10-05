from django import forms
from django.forms import ModelForm
from .models import UserSkills
from django.core.exceptions import NON_FIELD_ERRORS

class UserSkillsForm(ModelForm):

    class Meta:
        model = UserSkills
        fields = ('fullName','email','html','css','javascript','python','django','iosDevelopment','androidDevelopment')
        labels = {            
            "fullName": "Nome Completo",
            "email": "E-mail",
            "html": "Html (0 a 10)",
            "css": "Csss (0 a 10)",
            "javascript": "JavaScript (0 a 10)",
            "python": "Python (0 a 10)",
            "django": "Django (0 a 10)",
            "iosDevelopment": "Desenvolvimento em IOS (0 a 10)",
            "androidDevelopment": "Desenvolvimento em Android (0 a 10)"
        }
        
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Já existe um Usuário %(User) com o %(email)s informado.",
            }
        }

        
 



