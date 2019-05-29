from django.contrib import admin

from .models import Sec

class SecAdmin(admin.ModelAdmin):
  liste_ekrani = ('ilk_isim', 'soy_isim','konu', 'email', 'mesaj')
  

admin.site.register(Sec, SecAdmin)
