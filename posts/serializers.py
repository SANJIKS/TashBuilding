from rest_framework import serializers
from .models import Category, MainCarousel, MainCarouselItem, ColorCarousel, Color, ColorCarouselImage


class MainCarouselItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCarouselItem
        fields = '__all__'


class MainCarouselSerializer(serializers.ModelSerializer):
    items = MainCarouselItemSerializer(many=True, read_only=True)

    class Meta:
        model = MainCarousel
        fields = '__all__'

class ColorCarouselImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorCarouselImage
        fields = '__all__'
        
class ColorSerializer(serializers.ModelSerializer):
    items = ColorCarouselImageSerializer(many=True, read_only=True)

    class Meta:
        model = Color
        fields = '__all__'


class ColorCarouselSerializer(serializers.ModelSerializer):
    items = ColorSerializer(many=True, read_only=True)

    class Meta:
        model = ColorCarousel
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryDetailSerializer(serializers.ModelSerializer):
    main_carousels = MainCarouselSerializer(many=True, read_only=True, source='maincarousel_set')
    color_carousels = ColorCarouselSerializer(many=True, read_only=True, source='colorcarousel_set')

    class Meta:
        model = Category
        fields = '__all__'