import requests
from datetime import datetime
from mainpage.models import Country

api_url = "https://restcountries.com/v3.1/all"
def fetch_store_countries():
    
    response = requests.get(api_url)

    if response.status_code == 200:
        countries_data = response.json()
        for country in countries_data:
            name = country.get('name', {}).get('common')
            capital = country.get('capital', [None])[0]
            currencies=country.get("currencies",{})#look at this
            population = country.get('population', None)
            region = country.get('region', None)
            subregion = country.get('subregion', None)
            flag_url = country.get('flags', {}).get('png', None)
            languages=country.get('languages',{})
            continents=country.get("continents",[])

            if name:
                Country.objects.update_or_create(
#                     Why Use update_or_create() ?
#                    ✅ Avoids duplicates (ensures one country per name).
#                    ✅ Efficient (doesn’t require checking existence first).
#                    ✅ Easy to maintain (single line instead of try/except)
                    name=name,
                    defaults={
                        "capital": capital,
                        "currencies":currencies,
                        "population": population,
                        "region": region,
                        "subregion": subregion,
                        "flag_url": flag_url,
                        "languages":languages,
                        "continents":continents,
                        'last_updated':datetime.now()
                        }
                )

        print('Successfully fetched and stored country data')
    else:
        print('Failed to fetch country data')
