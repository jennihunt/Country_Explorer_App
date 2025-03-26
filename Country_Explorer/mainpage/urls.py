from django.urls import path
from .views import GalleryView,DetailView,reload_countries


urlpatterns=[
    path('',GalleryView.as_view(),name='country_list'),
    path('<int:pk>/',DetailView.as_view(),name='country_detail'),
    path("reload/", reload_countries, name="reload_countries"),
]