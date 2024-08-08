from django.db import models
from colorfield.fields import ColorField

class Category(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

class MainImage(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)

class MainCard(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)

class MainCardItem(models.Model):
    main_card = models.ForeignKey(MainCard, on_delete=models.SET_NULL, null=True, related_name='items')
    advantage = models.CharField(max_length=120, null=True, blank=True)
    title = models.CharField(max_length=120, null=True, blank=True)
    text = models.CharField(max_length=500, null=True, blank=True)

    
class MainCarousel(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self) -> str:
        return self.title


class MainCarouselItem(models.Model):
    carousel = models.ForeignKey(MainCarousel, on_delete=models.SET_NULL, null=True, related_name='items')
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    number = models.PositiveSmallIntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.title} --- {self.carousel.title}'

class ColorCarousel(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

class Color(models.Model):
    carousel = models.ForeignKey(ColorCarousel, on_delete=models.SET_NULL, null=True, related_name='items')
    color = ColorField(default='#FF0000')

class ColorCarouselImage(models.Model):
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, related_name='items')
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    number = models.PositiveSmallIntegerField(default=0)
    size = models.CharField(max_length=120, null=True, blank=True)


    def __str__(self) -> str:
        return f'{self.title} --- {self.color.carousel.title}'


class Footer(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    youtube = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    whatsapp = models.CharField(max_length=50, null=True, blank=True)
    telegram = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    
