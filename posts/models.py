from django.db import models
from colorfield.fields import ColorField

class Category(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    key = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self) -> str:
        return self.title

class MainImage(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)

class MainLSTKhome(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    button_title = models.CharField(max_length=200, null=True, blank=True)
    description_1 = models.TextField(null=True, blank=True)
    description_2 = models.TextField(null=True, blank=True)
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

class SizeCarousel(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

class Size(models.Model):
    carousel = models.ForeignKey(SizeCarousel, on_delete=models.SET_NULL, null=True, related_name='items')
    size = models.CharField(max_length=200, null=True, blank=True)

class SizeCarouselImage(models.Model):
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, related_name='items')
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    number = models.PositiveSmallIntegerField(default=0)
    size = models.CharField(max_length=120, null=True, blank=True)


    def __str__(self) -> str:
        return f'{self.title} --- {self.size.carousel.title}'


class Footer(models.Model):
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    title_whatsapp = models.CharField(max_length=120, null=True, blank=True)
    title_telegram = models.CharField(max_length=120, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)



class Tab(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
class TabItem(models.Model):
    tab = models.ForeignKey(Tab, on_delete=models.SET_NULL, null=True, blank=True, related_name='items')
    title = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    image_title = models.CharField(max_length=300, null=True, blank=True)
    image2 = models.ImageField(upload_to='posts/', null=True, blank=True)


class Advantage(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=120, null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    

# class AdvantageItem(models.Model):
#     advantage = models.ForeignKey(Advantage, on_delete=models.SET_NULL, null=True, related_name='items')
#     comparison = models.CharField(max_length=200, null=True, blank=True)
#     lstk = models.CharField(max_length=200, null=True, blank=True)
#     traditional_materials = models.CharField(max_length=200, null=True, blank=True)


class Unique(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)


class UniqueItem(models.Model):
    unique = models.ForeignKey(Unique, on_delete=models.SET_NULL, null=True, related_name='items')
    advantage = models.CharField(max_length=120, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=300, null=True, blank=True)


class MainText(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    second_text = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title if self.title else 'MainText'

class House(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    house_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    work_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title if self.title else 'House'

class Table(models.Model):
    house = models.ForeignKey(House, on_delete=models.SET_NULL, null=True, blank=True, related_name='tables')
    option = models.CharField(max_length=120, null=True, blank=True)
    choice = models.CharField(max_length=120, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.option} - {self.choice}'

class HouseImage(models.Model):
    house = models.ForeignKey(House, on_delete=models.SET_NULL, null=True, blank=True, related_name='images')
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return f'Image for {self.house}' if self.house else 'HouseImage'

class HouseImageCarousel(models.Model):
    house = models.ForeignKey(House, on_delete=models.SET_NULL, null=True, blank=True, related_name='house_image_carousels')
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return f'Image Carousel for {self.house}' if self.house else 'HouseImageCarousel'


class HouseSchemeCarousel(models.Model):
    house = models.ForeignKey(House, on_delete=models.SET_NULL, null=True, blank=True, related_name='house_scheme_carousels')
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return f'Scheme Carousel for {self.house}' if self.house else 'HouseSchemeCarousel'


class Form(models.Model):
    name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=120)

class Video(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    link_inst = models.CharField(max_length=200, null=True, blank=True)
    link_youtube = models.CharField(max_length=200, null=True, blank=True)


class VideoItem(models.Model):
    video = models.ForeignKey(Video, on_delete=models.SET_NULL, related_name='videos', null=True)
    link = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    text = models.TextField(null=True, blank=True)


class ComLSTK(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    button_title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)


class BigDescription(models.Model):
    description = models.TextField(null=True, blank=True)


class Technologically(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    button_title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)



class Carousel(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)


class CarouselItem(models.Model):
    carousel = models.ForeignKey(Carousel, on_delete=models.SET_NULL, null=True, related_name='carousels')
    title = models.CharField(max_length=120, null=True, blank=True)
    size = models.CharField(max_length=120, null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)


class Navbar(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    link_inst = models.CharField(max_length=200, null=True, blank=True)
    link_youtube = models.CharField(max_length=200, null=True, blank=True)


class NavbarItem(models.Model):
    navbar = models.ForeignKey(Navbar, on_delete=models.SET_NULL, related_name='items', null=True)
    text = models.TextField(null=True, blank=True)