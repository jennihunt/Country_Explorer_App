# Country Explorer App
This app utilizes information/data from  [REST Countries Api](https://restcountries.com/)  and stores info in PostgreSQL database.
- uses model Country to represent country data

## **Setup Instructions**
- First you need to open a poetry enviroment
    - poetry install to get dependencies
    - start poetry eval $(poetry env activate)

- Connect to the postgreSQL database
    - Create Postgresql database in command line 
        - FIRST ENTER THE PQSL COMMAND LINE 
        - CREATE DATABASE country_explorer [ WITH ] [ OWNER [=] user_name ]
        - change Database feild to match your postgresql db username and password

    - create a superuser to be able to check admin package
        - python manage.py createsuperuser

- Make migrations ,Migrate and then runserver
- You can generate postgresql db with REST Countries api data by running following code in terminal
    - python manage.py fetch_countries
    - Or by clicking the ReUpdate countries info button found in nav bar or footer
##
# What you can expect to see in App:
### **Visual Presentation and Navigation:**

- **Gallery View:**
    - homepage displays a grid of country cards.
    - Each card shows the country’s flag, name, region, and population.
- **Detail View:**
    - When a user clicks on a country card, links to  a detailed page with additional information (capital, languages, currencies, etc.).
- **Search and Filtering:**
    - search bar by name and region,working on filters (by population) so users can quickly locate countries of interest.

    - Static files hold css styling and javascript functionality

### **API integration and data persistence**

### **Fetch Country Data:**

- Developed a Django management command (or view) to fetch data from the REST Countries API.
    - you call this by running python manage.py fetch_countries

- Parsed the API responses and populate the PostgreSQL database using country model.

### **Data Refresh Mechanism:**

- Implemented error handling for API calls.
- Allow users to trigger a manual refresh of the country data.
    - Persistent refresh button
    - Correct location for functionality (`utils.py`)
    - Proof of refresh is shown in both a pop up model and the updated date on each country item displayed


# Things to still work on
- Add count on mainpage
- set up search functionality for  population
- set up live search

# **Stretch Goals To Work On **

### **Additional Models:**

- Add a `Language` model and a `Flag` model and establish the relationships between all three of your models.
    - `Language` could trigger functionality to display text in that language

### **Interactive Map Integration:**

- Use a JavaScript mapping library (e.g., Leaflet) to plot countries on an interactive map.
- Allow users to click on a map marker to see country details.

### **User Favorites and Reviews:**

- Implement login/logout functionality using the `User` model.
- Enable users to mark countries as favorites.
- Optionally add a review or rating system for each country.

### **PDF Report Generation:**
- Allow users to generate a PDF report of selected countries or search results.
- Include key statistics and visual summaries in the report.

### **Advanced Data Visualizations:**

- Incorporate charts or graphs (using libraries like Chart.js) to display statistics such as population distribution by region.