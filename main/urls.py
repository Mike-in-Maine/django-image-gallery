from django.urls import path
from . import views
from .views import search_view


urlpatterns = [
    path('',views.home, name='home'),
    path('category/<slug:slug>', views.categoryPage, name='image-category'),
    path('category/<slug:slug1>/<slug:slug2>', views.imageDetailPage, name='image-detail'),
    path('search/', search_view, name='search')
]
