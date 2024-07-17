from django.contrib import admin
from .models import MainCarousel, MainCarouselItem, Category, ColorCarousel, ColorCarouselItem

admin.site.register([Category, MainCarousel, MainCarouselItem, ColorCarousel, ColorCarouselItem])