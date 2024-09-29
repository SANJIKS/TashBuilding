from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, House, MainCarousel, Footer, Form, MainImage, MainLSTKhome, Unique, Advantage
from .serializers import CategoryDetailSerializer, CategorySerializer, HouseDetailSerializer, MainCarouselSerializer, FooterSerializer, FormSerializer, MainImageSerializer, MainLSTKSerializer, UniqueSerializer, AdvantageSerializer

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
