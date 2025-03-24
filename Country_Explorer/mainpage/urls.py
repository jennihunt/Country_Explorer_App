from django.urls import path
from .views import GalleryView,DetailView


urlpatterns=[
    path('',GalleryView.as_view(),name='country_list'),
    path('<int:pk>/',DetailView.as_view(),name='country_detail')
]