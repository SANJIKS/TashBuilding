from django.contrib import admin
from .models import Footer, MainCarousel, MainCarouselItem, Category, ColorCarousel, Color, ColorCarouselImage, MainImage, MainCard, MainCardItem

admin.site.register([Category, MainCarousel, MainCarouselItem, ColorCarousel, Color, ColorCarouselImage, Footer])