from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import AddPostFormMassag, AddPostFormTravel
from .models import Block_massag, Block_spa_program, Block_taping, Block_obuchine
from django.contrib import messages



def index(request):
    return render(request, 'main/index.html')

def travel(request):
    recipients = ['ilya.2787@gmail.com']
    if request.method == "POST":
        form = AddPostFormTravel(request.POST)
        if form.is_valid():
            try:
                send_mail(form.cleaned_data['name_t'], form.cleaned_data['telefon_t'], recipients, fail_silently=False)
            except:
                send_mail("Заявка на путешествие с сайта",
                          "Здравствуйте я бы хотел отправиться с вами:\n\nМеня зовут: " + str(
                              form.cleaned_data['name_t']) +
                          "\n" "Мой номер: " + form.cleaned_data['telefon_t'] +
                          "\n\nЖду звонка от вас", settings.EMAIL_HOST_USER,
                          recipients, fail_silently=False)
            messages.success(request, 'Заявка успешно отправленна')
    else:
        form = AddPostFormTravel()
    return render(request, 'main/travel.html', {"forms": form})

def about_me(request):
    return render(request, 'main/about_me.html')

def meditation(request):
    return render(request, 'main/meditation.html')

def seo(request):
    return render(request, 'main/SEO.html')

def massag(request):
    ServicesMassage = Block_massag.objects.all()
    ServicesSpa = Block_spa_program.objects.all()
    ServicesTap = Block_taping.objects.all()
    ServicesObuch = Block_obuchine.objects.all()
    recipients = ['ilya.2787@gmail.com']
    if request.method == "POST":
        forms = AddPostFormMassag(request.POST)
        if forms.is_valid():
            try:
                send_mail(forms.cleaned_data['name'], forms.cleaned_data['telefon'], forms.cleaned_data['email'], recipients, fail_silently=False)
            except:
                send_mail("Заявка на услугу с сайта",
                          "Здравствуйте я бы хотел заказать одну из ваших услуг:\n\nМеня зовут: " + str(
                              forms.cleaned_data['name']) +
                          "\n" "Мой номер: " + forms.cleaned_data['telefon'] +
                          "\n" + "Мой Email: " + forms.cleaned_data['email'] +
                          "\n\nЖду звонка или письма от вас", settings.EMAIL_HOST_USER,
                          recipients, fail_silently=False)
            messages.success(request, 'Заявка успешно отправленна')
    else:
        forms = AddPostFormMassag()
    return render(request, 'main/massag.html', {"SM": ServicesMassage,
                                                "Spa": ServicesSpa,
                                                "Tap": ServicesTap,
                                                "Obuch": ServicesObuch,
                                                "form": forms})




