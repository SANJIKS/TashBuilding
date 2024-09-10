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
    title = models.CharField(max_length=120, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    youtube = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    whatsapp = models.CharField(max_length=50, null=True, blank=True)
    telegram = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)



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
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    

class AdvantageItem(models.Model):
    advantage = models.ForeignKey(Advantage, on_delete=models.SET_NULL, null=True, related_name='items')
    comparison = models.CharField(max_length=200, null=True, blank=True)
    lstk = models.CharField(max_length=200, null=True, blank=True)
    traditional_materials = models.CharField(max_length=200, null=True, blank=True)


class Unique(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
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


class HouseCarousel(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)


class House(models.Model):
    carousel = models.ForeignKey(HouseCarousel, on_delete=models.SET_NULL, null=True, blank=True, related_name='items')
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class HouseImageCarousel(models.Model):
    house = models.ForeignKey(House, on_delete=models.SET_NULL, null=True, blank=True)


class HouseImageItem(models.Model):
    carousel = models.ForeignKey(HouseImageCarousel, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='posts', null=True, blank=True)

class HouseSchemeCarousel(models.Model):
    house = models.ForeignKey(House, on_delete=models.SET_NULL, null=True, blank=True)


class HouseSchemeItem(models.Model):
    carousel = models.ForeignKey(HouseSchemeCarousel, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='posts', null=True, blank=True)
