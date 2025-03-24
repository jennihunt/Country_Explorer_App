## **Day 1: Django Project Setup and Database Configuration**

### **Project Initialization:**

- Set up a new Django project and create an app (e.g., explorer).
- Configure PostgreSQL as the database backend.

### **Model Design and Admin Setup:**

- Design Django models to represent country data (fields for name, flag URL, capital, population, region, etc.).
- Customize the Django Admin interface for managing country records.

### **Basic Routing and Templates:**

- Set up basic URL routes and create initial templates for the gallery view.

---

## **Day 2: API Integration and Data Persistence**

### **Fetch Country Data:**

- Develop a Django management command (or view) to fetch data from the REST Countries API.
- Parse the API response and populate the PostgreSQL database using your models.

### **Data Refresh Mechanism:**

- Implement error handling for API calls.
- Optionally, allow users to trigger a manual refresh of the country data.



#refresh option******
time stamp last updated btn or logging middleware