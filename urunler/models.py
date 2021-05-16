from django.db import models

# Create your models here.

class urun(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ürün Adı")
    description = models.TextField( verbose_name="Ürün Tanımı" )
    image = models.CharField(max_length=50, verbose_name="Ürün Resmi")
    created_date = models.DateField(auto_now_add=True, verbose_name="Kayıt tarihi")
    isPublished = models.BooleanField(default=True, verbose_name="Yayınlandı")

    def __str__(self):
        return self.name

    def get_image_path(self):
        return '/img/'+ self.image