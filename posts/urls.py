from django.urls import path
from .views import CategoryListView, CategoryDetailView, FooterAPIView, HouseDetailView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
    path('footers/', FooterAPIView.as_view(), name='get-footers'),
    path('house/<int:id>/', HouseDetailView.as_view(), name='house-detail')
]
