from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Country
# Create your views here.
class GalleryView(ListView):
    model=Country
    template_name='mainpage/country/country_list.html'
    context_object_name='countries'


class DetailView(DetailView):
    model=Country
    template_name='mainpage/country/country_detail.html'