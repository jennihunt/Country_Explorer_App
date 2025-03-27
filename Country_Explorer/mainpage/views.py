from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .utils import fetch_store_countries
from django.http import JsonResponse
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
    success = fetch_store_countries()
    print("hey")
    if success:
        return JsonResponse({"message": "Data reloaded successfully!", "status": "success"})
    else:
        return JsonResponse({"message": "Failed to reload data.", "status": "error"})
    
def search(request):
    return render(request,'mainpage/search/search.html')

def search_results(request):
    query = request.GET.get('q')
    results = Country.objects.filter(name__icontains=query) if query else None
   
    return render(request, 'mainpage/search/searchresults.html', {'countries': results, 'query': query})