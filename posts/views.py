from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, MainCarousel, ColorCarousel
from .serializers import CategorySerializer, MainCarouselSerializer, ColorCarouselSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'