from django.db import models

class Sec(models.Model):
  ilk_isim = models.CharField(max_length=200)
  soy_isim = models.CharField(max_length=200)
  konu = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  mesaj = models.TextField(max_length=1000)
  
  def __str__(self):
    return self.ilk_isim
