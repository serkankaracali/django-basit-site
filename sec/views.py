from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth
from .models import Sec


def ana(request):
    if request.method == 'POST':
        # Form değerlerini al
        ilk_isim = request.POST['first-name']
        soy_isim = request.POST['last-name']
        konu = request.POST['Subject']
        email = request.POST['email']
        mesaj = request.POST['message']

        baglanti = Sec(ilk_isim=ilk_isim, soy_isim=soy_isim, konu=konu, email=email, mesaj=mesaj)
        baglanti.save()

        return redirect('/')
    else:
        return render(request, 'base.html', {})

def mesaj(request):
    if request.method == 'POST':
        # Form değerlerini al
        ilk_isim = request.POST['first-name']
        soy_isim = request.POST['last-name']
        konu = request.POST['Subject']
        email = request.POST['email']
        mesaj = request.POST['message']
        return redirect('')
    else:
        return render(request, 'base.html')
    