from django.shortcuts import render
from .models import User
from .forms import UserSkillsForm
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages


def index(request):    

    form = UserSkillsForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            
            form.save()
            messages.success(request, "Cadastro efetuado com sucesso")
            
            htmlMailSend(form)
            form = UserSkillsForm()

    return render(request, 'meuscandidatos/index.html', {'form': form})

def htmlMailSend(form):

        message = ""
        subject = "Obrigado por se candidatar"
        from_email = settings.EMAIL_HOST_USER
        to_list = [ form.cleaned_data['email'], from_email]
        
        if( form.cleaned_data['html'] is None ):
            form.cleaned_data['html'] = 0
        if( form.cleaned_data['css'] is None ):
            form.cleaned_data['css'] = 0
        if( form.cleaned_data['javascript'] is None ):
            form.cleaned_data['javascript'] = 0
        if( form.cleaned_data['python'] is None ):
            form.cleaned_data['python'] = 0
        if( form.cleaned_data['django'] is None ):
            form.cleaned_data['django'] = 0
        if( form.cleaned_data['iosDevelopment'] is None ):
            form.cleaned_data['iosDevelopment'] = 0
        if( form.cleaned_data['androidDevelopment'] is None ):
            form.cleaned_data['androidDevelopment'] = 0        


        if( form.cleaned_data['html'] >= 7 and form.cleaned_data['css'] >= 7 and form.cleaned_data['javascript'] >= 7 ):
            message = "Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador Front-End entraremos em contato."            
            res = send_mail(subject, message, from_email, to_list, fail_silently=True)            
        if( form.cleaned_data['python'] >= 7 and form.cleaned_data['django'] >= 7 ):
            message = "Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador Back-End entraremos em contato."        
            res = send_mail(subject, message, from_email, to_list, fail_silently=True)
        if( form.cleaned_data['iosDevelopment'] >= 7 or form.cleaned_data['androidDevelopment'] >= 7):
            message = "Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador Mobile entraremos em contato." 
            res = send_mail(subject, message, from_email, to_list, fail_silently=True)
        if( message == "" ):
            message = "Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador entraremos em contato." 
            res = send_mail(subject, message, from_email, to_list, fail_silently=True)
        