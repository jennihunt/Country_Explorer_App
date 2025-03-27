import requests
from datetime import datetime
from mainpage.models import Country
from django.db import DataError


def fetch_store_countries():
    api_url = "https://restcountries.com/v3.1/all"   
    response = requests.get(api_url)

    if response.status_code == 200:
        countries_data = response.json()
        
        for country in countries_data:
            try:
                name = country.get('name', {}).get('common')[:255]
                capital = country.get('capital', [None])[0]
                #currencies = country.get('currencies')
                population = country.get('population', None)
                region = country.get('region', None)
                subregion = country.get('subregion', None)
                flag_url = country.get('flags', {}).get('png', None)
                #languages=country.get('languages',{})
                continents=country.get("continents",[])
                        # Extract currencies safely
                currencies = country.get("currencies", {})
                if isinstance(currencies, dict):
                    formatted_currencies = {
                        code: {"name": details.get("name", ""), "symbol": details.get("symbol", "")}
                        for code, details in currencies.items()
                    }
                else:
                    formatted_currencies = {}

                # Extract languages safely
                languages = country.get("languages", {})
                if isinstance(languages, dict):
                    formatted_languages = list(languages.values())
                else:
                    formatted_languages = []




                # Debugging: Check 'currencies'
                
                #print("Currencies Data:", currencies, type(currencies))  # Print to 
                if name:
                    country,created=Country.objects.update_or_create(
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

                print(f"{'✅ Created' if created else '🔄 Updated'} country: {name}")
                print('Successfully fetched and stored country data')
            except Exception as e:
                print(f"ERROR {e}")
            # except Country.DoesNotExist:
            #     country=None
            #     print('Failed to fetch country data')
            # except DataError as e:
            #     print(f"DATA ERROR  {e}  {country}")








