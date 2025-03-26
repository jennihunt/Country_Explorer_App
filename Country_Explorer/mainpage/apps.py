from django.apps import AppConfig
# from django.core.management import call_command


class MainpageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainpage'

#This will fetch countries when Django starts.
    # def ready(self):
    #     from mainpage.utils import fetch_and_store_countries
    #     fetch_and_store_countries()