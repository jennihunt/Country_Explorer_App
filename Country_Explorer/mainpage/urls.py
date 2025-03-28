from django.urls import path
from .views import GalleryView,DetailView,reload_countries,search_results,search_region,search


urlpatterns=[
    path('',GalleryView.as_view(),name='country_list'),
    path('<int:pk>/',DetailView.as_view(),name='country_detail'),
    path("reload/", reload_countries, name="reload_countries"),
    path("search/",search,name="search"),
    path('searchresults/',search_results,name="search_results"),
    path('searchregion/',search_region,name="search_region"),
    #  path('searchpopulation/',search_population,name="search_population"),

]