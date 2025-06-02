# Country Explorer App
Country Explorer is a web application that lets users search for and explore information about countries worldwide. The app leverages the  [REST Countries Api](https://restcountries.com/)  to fetch up-to-date data and stores relevant details in a PostgreSQL database for efficient access and further analysis.

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
## Features
🌍 Search and discover countries by name or region
📊 View detailed information, including population, languages, currencies, capital, and more
🗺️ Interactive, user-friendly interface built with Python, HTML, CSS, and JavaScript
💾 Persistent storage of country data in PostgreSQL
🔄 Fetches and updates country information using the REST Countries API

##Technologies Used
- Backend: Python (Flask or Django recommended)
- Frontend: HTML, CSS, JavaScript
- Database: PostgreSQL
- APIs: REST Countries API

# Getting Started
## Prerequisites
- Python 3.x
- PostgreSQL
- pipenv or pip for managing Python dependencies
  
## Installation
Clone the repository
- git clone https://github.com/jennihunt/Country_Explorer_App.git
- cd Country_Explorer_App
- 
Install dependencies
pipenv install
# or
pip install -r requirements.txt

Configure the database
- Create a PostgreSQL database (e.g., country_explorer)
- Update your database credentials in the app’s configuration file (config.py or .env as applicable)

Run migrations (if applicable)
# Example for Flask-Migrate or Django
- flask db upgrade
# or
- python manage.py migrate

Start the application
- flask run
# or
- python manage.py runserver
  
Open your browser
Visit http://localhost:5000 or the port shown in your terminal

# Usage
- Search for a country by name or browse the list
- Click on a country to view its details
- All data is regularly updated from the REST Countries API and stored in PostgreSQL for fast retrieval
S



















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
