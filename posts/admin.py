from django.contrib import admin
from .models import BigDescription, Carousel, CarouselItem, ComLSTK, Footer, MainCarousel, MainCarouselItem, Category, Navbar, NavbarItem, SizeCarousel, Size, SizeCarouselImage, MainImage, MainCard, MainCardItem, Tab, TabItem, Advantage, Technologically, Unique, UniqueItem, MainText, House, HouseImage, HouseImageCarousel, HouseSchemeCarousel, Table, MainLSTKhome, Video, VideoItem

admin.site.register([Category, MainCarousel, MainCarouselItem, SizeCarousel, Size, SizeCarouselImage, Footer, Tab, TabItem, Advantage, Unique, UniqueItem, MainText, HouseImage, House, HouseSchemeCarousel, HouseImageCarousel, Table, MainImage, MainLSTKhome, Video, BigDescription, ComLSTK, Technologically, Carousel, CarouselItem, VideoItem, Navbar, NavbarItem])
