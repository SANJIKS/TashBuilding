from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BigDescription, Carousel, Category, ComLSTK, House, MainCarousel, Footer, Form, MainImage, MainLSTKhome, Navbar, Technologically, Unique, Advantage, Video
from .serializers import BigDescriptionSerializer, CarouselSerializer, CategoryDetailSerializer, CategorySerializer, ComLSTKSerializer, HouseDetailSerializer, MainCarouselSerializer, FooterSerializer, FormSerializer, MainImageSerializer, MainLSTKSerializer, NavbarSerializer, TechnologicallySerializer, UniqueSerializer, AdvantageSerializer, VideoSerializer

class VideoView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class AdvantageView(generics.ListAPIView):
    queryset = Advantage.objects.all()
    serializer_class = AdvantageSerializer

class UniqueView(generics.ListAPIView):
    queryset = Unique.objects.all()
    serializer_class = UniqueSerializer
    
class MainLSTKView(generics.ListAPIView):
    queryset = MainLSTKhome.objects.all()
    serializer_class = MainLSTKSerializer

class MainImageView(generics.ListAPIView):
    queryset = MainImage.objects.all()
    serializer_class = MainImageSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'id'


class FooterAPIView(APIView):
    def get(self, reqeust):
        footer = Footer.objects.first()
        serializer = FooterSerializer(footer)
        return Response(serializer.data, status=200)
    
class HouseDetailView(generics.RetrieveAPIView):
    queryset = House.objects.all()
    serializer_class = HouseDetailSerializer
    lookup_field = 'id'


class FormCreateView(generics.CreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

class ComLSTKView(generics.ListAPIView):
    queryset = ComLSTK.objects.all()
    serializer_class = ComLSTKSerializer


class BigDescriptionView(generics.ListAPIView):
    queryset = BigDescription.objects.all()
    serializer_class = BigDescriptionSerializer


class TechnologicallyView(generics.ListAPIView):
    queryset = Technologically.objects.all()
    serializer_class = TechnologicallySerializer


class CarouselListView(generics.ListAPIView):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer


class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class NavbarListView(generics.ListAPIView):
    queryset = Navbar.objects.all()
    serializer_class = NavbarSerializer