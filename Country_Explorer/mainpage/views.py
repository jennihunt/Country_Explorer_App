from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .utils import fetch_store_countries
from django.db.models import Q
# . Q objects provides you complete control over the where clause of the query.
# If you want to {OR/AND/ALL FOR ONE NOT FOR ALL}  your conditions.
from django.http import JsonResponse
from django.utils import timezone
import requests

from .models import Country
# Create your views here.

class GalleryView(ListView):
    model=Country
    template_name='mainpage/country/country_list.html'
    context_object_name='countries'


class DetailView(DetailView):
    model=Country
    template_name='mainpage/country/country_detail.html'

def reload_countries(request):
    time=timezone.now()
    try:
        fetch_store_countries()
        return JsonResponse({"message": f"Data reloaded successfully at {time}!", "status": "success"})
    except Exception as e:
        return JsonResponse({"message": "Failed to reload data.", "status": "error"})
    
def search(request):
    return render(request,'mainpage/search/search.html')

def search_results(request):
    query = request.GET.get('q')
    results = Country.objects.filter(Q(name__icontains=query)|Q(region__icontains=query)) if query else None
   
    return render(request, 'mainpage/search/searchresults.html', {'countries': results, 'query': query})

