from django.core.management.base import BaseCommand
from mainpage.utils import fetch_store_countries




class Command(BaseCommand):
    

    def handle(self, *args, **kwargs):
        try:
            success = fetch_store_countries()
        
            self.stdout.write(self.style.SUCCESS("Countries updated successfully!"))
      
        except Exception as e:
            
            print(f"ERRor: {e}")
            self.stdout.write(self.style.ERROR("Failed to update countries."))

