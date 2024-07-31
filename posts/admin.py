from django.contrib import admin
from .models import MainCarousel, MainCarouselItem, Category, ColorCarousel, Color, ColorCarouselImage

admin.site.register([Category, MainCarousel, MainCarouselItem, ColorCarousel, Color, ColorCarouselImage])