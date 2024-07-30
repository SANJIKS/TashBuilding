from django.db import models
from colorfield.fields import ColorField

class Category(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

class MainCarousel(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='main_carousels')
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
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='color_carousels')
    title = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

class ColorCarouselItem(models.Model):
    carousel = models.ForeignKey(ColorCarousel, on_delete=models.SET_NULL, null=True, related_name='items')
    color = ColorField(default='#FF0000')
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    number = models.PositiveSmallIntegerField(default=0)
    size = models.CharField(max_length=120, null=True, blank=True)


    def __str__(self) -> str:
        return f'{self.title} --- {self.carousel.title}'
