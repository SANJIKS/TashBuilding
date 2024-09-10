from rest_framework import serializers
from .models import Category, Footer, MainCarousel, MainCarouselItem, MainText, SizeCarousel, Size, SizeCarouselImage, MainImage, MainCard, MainCardItem, Tab, TabItem, AdvantageItem, Advantage, Unique, UniqueItem, HouseCarousel, House, HouseImageCarousel, HouseImageItem, HouseSchemeCarousel, HouseSchemeItem

class HouseImageItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseImageItem
        fields = '__all__'

class HouseImageCarouselSerializer(serializers.ModelSerializer):
    items = HouseImageItemSerializer(many=True, read_only=True)
    class Meta:
        model = HouseImageCarousel
        fields = '__all__'

class HouseSchemeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseSchemeItem
        fields = '__all__'

class HouseSchemeCarouselSerializer(serializers.ModelSerializer):
    items = HouseSchemeItemSerializer(many=True, read_only=True)
    class Meta:
        model = HouseSchemeCarousel
        fields = '__all__'

class HouseDetailSerializer(serializers.ModelSerializer):
    house_image_carousel = HouseImageCarouselSerializer(read_only=True, source='houseimagecarousel_set')
    house_scheme_carousel = HouseSchemeCarouselSerializer(read_only=True, source='houseschemecarousel_set')
    
    class Meta:
        model = House
        fields = '__all__'
        
class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

class HouseCarouselSerializer(serializers.ModelSerializer):
    items = HouseSerializer(many=True, read_only=True)
    class Meta:
        model = HouseCarousel
        fields = '__all__'


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


class AdvantageItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvantageItem
        fields = '__all__'


class AdvantageSerializer(serializers.ModelSerializer):
    items = AdvantageItemSerializer(many=True, read_only=True)
    
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
    main_carousels = MainCarouselSerializer(many=True, read_only=True, source='maincarousel_set')
    size_carousels = SizeCarouselSerializer(many=True, read_only=True, source='sizecarousel_set')
    main_image = MainImageSerializer(many=True, read_only=True, source='mainimage_set')
    maincards = MainCardSerializer(many=True, read_only=True, source='maincard_set')
    tabs = TabSerializer(many=True, read_only=True, source='tab_set')
    advantages = AdvantageSerializer(many=True, read_only=True, source='advantage_set')
    house_carousels = HouseCarouselSerializer(many=True, read_only=True, source='housecarousel_set')

    class Meta:
        model = Category
        fields = '__all__'


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'


