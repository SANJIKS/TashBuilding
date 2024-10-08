from rest_framework import serializers
from .models import BigDescription, Carousel, CarouselItem, Category, ComLSTK, Footer, MainCarousel, MainCarouselItem, MainText, Navbar, NavbarItem, SizeCarousel, Size, SizeCarouselImage, MainImage, MainCard, MainCardItem, Tab, TabItem, Advantage, Table, Technologically, Unique, UniqueItem, House, HouseImageCarousel, HouseSchemeCarousel, Form, MainImage, MainLSTKhome, Video, VideoItem

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class MainLSTKSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainLSTKhome
        fields = '__all__'

class MainImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainImage
        fields = '__all__'

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'
        

class HouseImageCarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseImageCarousel
        fields = ('image',)


class HouseSchemeCarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseSchemeCarousel
        fields = ('image',)

class HouseDetailSerializer(serializers.ModelSerializer):
    house_image_carousel = HouseImageCarouselSerializer(many=True, read_only=True, source='house_image_carousels')
    house_scheme_carousel = HouseSchemeCarouselSerializer(many=True, read_only=True, source='house_scheme_carousels')
    tables = TableSerializer(many=True, read_only=True)

    class Meta:
        model = House
        fields = '__all__'
        
class HouseSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = House
        fields = ('id', 'category', 'title', 'description', 'images')

    def get_images(self, obj):
        request = self.context.get('request')
        if not request:
            return [image.image.url for image in obj.images.all()]
        return [request.build_absolute_uri(image.image.url) for image in obj.images.all()]


class UniqueItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniqueItem
        fields = '__all__'


class UniqueSerializer(serializers.ModelSerializer):
    items = UniqueItemSerializer(many=True, read_only=True)    
    class Meta:
        model = Unique
        fields = '__all__'

class TabItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TabItem
        fields = '__all__'


class TabSerializer(serializers.ModelSerializer):
    items = TabItemSerializer(many=True, read_only=True)    

    class Meta:
        model = Tab
        fields = '__all__'


# class AdvantageItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AdvantageItem
#         fields = '__all__'


class AdvantageSerializer(serializers.ModelSerializer):
    # items = AdvantageItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Advantage
        fields = '__all__'


class MainImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainImage
        fields = '__all__'


class MainCardItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCardItem
        fields = '__all__'

class MainCardSerializer(serializers.ModelSerializer):
    items = MainCardItemSerializer(many=True, read_only=True)    
        
    class Meta:
        model = MainCard
        fields = '__all__'



class MainCarouselItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCarouselItem
        fields = '__all__'


class MainCarouselSerializer(serializers.ModelSerializer):
    items = MainCarouselItemSerializer(many=True, read_only=True)

    class Meta:
        model = MainCarousel
        fields = '__all__'

class SizeCarouselImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeCarouselImage
        fields = '__all__'
        
class SizeSerializer(serializers.ModelSerializer):
    items = SizeCarouselImageSerializer(many=True, read_only=True)

    class Meta:
        model = Size
        fields = '__all__'


class SizeCarouselSerializer(serializers.ModelSerializer):
    items = SizeSerializer(many=True, read_only=True)

    class Meta:
        model = SizeCarousel
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MainTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainText
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    house = HouseSerializer(many=True, read_only=True, source='house_set')

    class Meta:
        model = Category
        fields = '__all__'


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'



class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'


class ComLSTKSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComLSTK
        fields = '__all__'


class BigDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BigDescription
        fields = '__all__'


class TechnologicallySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technologically
        fields = '__all__'


class CarouselItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselItem
        exclude = ['carousel']

class CarouselSerializer(serializers.ModelSerializer):
    carousels = CarouselItemSerializer(many=True, read_only=True)

    class Meta:
        model = Carousel
        fields = ['id', 'title', 'carousels']


class VideoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoItem
        exclude = ['video']

class VideoSerializer(serializers.ModelSerializer):
    videos = VideoItemSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = ['id', 'title', 'link_inst', 'link_youtube', 'videos']


class NavbarItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavbarItem
        exclude = ['navbar']

class NavbarSerializer(serializers.ModelSerializer):
    items = NavbarItemSerializer(many=True, read_only=True)

    class Meta:
        model = Navbar
        fields = ['id', 'title', 'link_inst', 'link_youtube', 'items']