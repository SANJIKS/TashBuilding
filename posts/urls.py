from django.urls import path
from .views import BigDescriptionView, CarouselListView, CategoryListView, CategoryDetailView, ComLSTKView, FooterAPIView, HouseDetailView, FormCreateView, MainImageView, MainLSTKView, NavbarListView, TechnologicallyView, UniqueView, AdvantageView, VideoListView, VideoView

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
    path('videos/', VideoView.as_view(), name='video'),
    path('com-lstk/', ComLSTKView.as_view(), name='com-lstk'),
    path('big-description/', BigDescriptionView.as_view(), name='big-description'),
    path('technologically/', TechnologicallyView.as_view(), name='technologically'),
    path('carousels/', CarouselListView.as_view(), name='carousel-list'),
    path('videos/', VideoListView.as_view(), name='video-list'),
    path('navbars/', NavbarListView.as_view(), name='navbar-list'),
]
