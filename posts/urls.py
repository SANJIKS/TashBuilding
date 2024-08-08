from django.urls import path
from .views import CategoryListView, CategoryDetailView, FooterAPIView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
    path('footers/', FooterAPIView.as_view(), name='get-footers')
]
