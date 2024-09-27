from django.urls import path
from .views import CategoryListView, CategoryDetailView, FooterAPIView, HouseDetailView, FormCreateView, MainImageView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
    path('footers/', FooterAPIView.as_view(), name='get-footers'),
    path('house/<int:id>/', HouseDetailView.as_view(), name='house-detail'),
    path('form/', FormCreateView.as_view(), name='form-create'),
    path('main-images/', MainImageView.as_view(), name='main-images')
]
