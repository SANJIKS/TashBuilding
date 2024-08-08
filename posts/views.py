from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, MainCarousel, Footer
from .serializers import CategoryDetailSerializer, CategorySerializer, MainCarouselSerializer, FooterSerializer


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