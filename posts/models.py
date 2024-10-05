from django.db import models
from colorfield.fields import ColorField

class Category(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    key = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return f'Категория {self.id}: {self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class MainImage(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)

    def __str__(self) -> str:
        return f'Основное изображение {self.id}: {self.title}'

    class Meta:
        verbose_name = 'Основное изображение'
        verbose_name_plural = 'Основные изображения'

class MainLSTKhome(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    button_title = models.CharField(max_length=200, null=True, blank=True)
    description_1 = models.TextField(null=True, blank=True)
    description_2 = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)

    def __str__(self) -> str:
        return f'Дом LSTK {self.id}: {self.title}'

    class Meta:
        verbose_name = 'Дом LSTK'
        verbose_name_plural = 'Дома LSTK'

class MainCard(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)

    def __str__(self) -> str:
        return f'Основная карта {self.id}: {self.title}'

    class Meta:
        verbose_name = 'Основная карта'
        verbose_name_plural = 'Основные карты'

class MainCardItem(models.Model):
    main_card = models.ForeignKey(MainCard, on_delete=models.SET_NULL, null=True, related_name='items')
    advantage = models.CharField(max_length=120, null=True, blank=True)
    title = models.CharField(max_length=120, null=True, blank=True)
    text = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return f'Элемент карты {self.id}: {self.title}'

    class Meta:
        verbose_name = 'Элемент карты'
        verbose_name_plural = 'Элементы карт'

class MainCarousel(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self) -> str:
        return f'Карусель {self.id}: {self.title}'

    class Meta:
        verbose_name = 'Карусель'
        verbose_name_plural = 'Карусели'

class MainCarouselItem(models.Model):
    carousel = models.ForeignKey(MainCarousel, on_delete=models.SET_NULL, null=True, related_name='items')
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    number = models.PositiveSmallIntegerField(default=0)

    def __str__(self) -> str:
        return f'Элемент карусели {self.id}: {self.title}'

    class Meta:
        verbose_name = 'Элемент карусели'
        verbose_name_plural = 'Элементы карусели'

class SizeCarousel(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self) -> str:
        return f'Карусель размеров {self.id}: {self.title}'

    class Meta:
        verbose_name = 'Карусель размеров'
        verbose_name_plural = 'Карусели размеров'

class Size(models.Model):
    carousel = models.ForeignKey(SizeCarousel, on_delete=models.SET_NULL, null=True, related_name='items')
    size = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return f'Размер {self.id}: {self.size}'

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

class SizeCarouselImage(models.Model):
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, related_name='items')
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    number = models.PositiveSmallIntegerField(default=0)

    def __str__(self) -> str:
        return f'Изображение {self.id}: {self.title} для {self.size}'

    class Meta:
        verbose_name = 'Изображение карусели'
        verbose_name_plural = 'Изображения карусели'

class Footer(models.Model):
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    title_whatsapp = models.CharField(max_length=120, null=True, blank=True)
    title_telegram = models.CharField(max_length=120, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f'Футер {self.id}: {self.address}'

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футеры'


class Tab(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self) -> str:
        return self.title if self.title else 'Tab'


class TabItem(models.Model):
    tab = models.ForeignKey(Tab, on_delete=models.SET_NULL, null=True, blank=True, related_name='items')
    title = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    image_title = models.CharField(max_length=300, null=True, blank=True)
    image2 = models.ImageField(upload_to='posts/', null=True, blank=True)

    def __str__(self) -> str:
        return self.title if self.title else 'TabItem'


class Advantage(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title if self.title else 'Advantage'


class Unique(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)

    def __str__(self) -> str:
        return self.title if self.title else 'Unique'


class UniqueItem(models.Model):
    unique = models.ForeignKey(Unique, on_delete=models.SET_NULL, null=True, related_name='items')
    advantage = models.CharField(max_length=120, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self) -> str:
        return self.title if self.title else 'UniqueItem'


class MainText(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    second_text = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
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
        return f'{self.option} - {self.choice}' if self.option and self.choice else 'Table'


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

    def __str__(self):
        return f'{self.name} - {self.phone_number}'


class Video(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    link_inst = models.CharField(max_length=200, null=True, blank=True)
    link_youtube = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title if self.title else 'Video'


class VideoItem(models.Model):
    video = models.ForeignKey(Video, on_delete=models.SET_NULL, related_name='videos', null=True)
    link = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.link if self.link else 'VideoItem'


class ComLSTK(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    button_title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)

    def __str__(self):
        return self.title if self.title else 'ComLSTK'


class BigDescription(models.Model):
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'BigDescription'


class Technologically(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    button_title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)

    def __str__(self):
        return self.title if self.title else 'Technologically'


class Carousel(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.title if self.title else 'Carousel'


class CarouselItem(models.Model):
    carousel = models.ForeignKey(Carousel, on_delete=models.SET_NULL, null=True, related_name='carousels')
    title = models.CharField(max_length=120, null=True, blank=True)
    size = models.CharField(max_length=120, null=True, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)

    def __str__(self):
        return self.title if self.title else 'CarouselItem'


class Navbar(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    link_inst = models.CharField(max_length=200, null=True, blank=True)
    link_youtube = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title if self.title else 'Navbar'


class NavbarItem(models.Model):
    navbar = models.ForeignKey(Navbar, on_delete=models.SET_NULL, related_name='items', null=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.text if self.text else 'NavbarItem'