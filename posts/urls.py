from django.urls import path
from .views import CategoryListView, CategoryDetailView, FooterAPIView, HouseDetailView, FormCreateView, MainImageView, MainLSTKView, UniqueView, AdvantageView, VideoView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
    path('footers/', FooterAPIView.as_view(), name='get-footers'),
    path('house/<int:id>/', HouseDetailView.as_view(), name='house-detail'),
    path('form/', FormCreateView.as_view(), name='form-create'),
    path('main-images/', MainImageView.as_view(), name='main-images'),
    path('lstk-images/', MainLSTKView.as_view(), name='lstk'),
    path('unique/', UniqueView.as_view(), name='unique'),
    path('advantages/', AdvantageView.as_view(), name='advantage'),
    path('videos/', VideoView.as_view(), name='video')
]
