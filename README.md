# Catalog App Backend

This is the backend service for the **Catalog App**, built using Django.

## Getting Started

You can run this backend in two ways:

### 1. Clone and Install Dependencies
   Clone this repository:
      
      git clone https://github.com/yourusername/catalog_be.git
      cd catalog_be
   
   Install dependencies:
   
      pip install -r requirements.txt
      
     python manage.py runserver 0.0.0.0:8000
  
  If you get an error for running on port 8000, change the port to any available one

### 2. Run with Docker

     docker pull prkaushi/catalog_be
     
     docker run -p 8000:8000 prkaushi/catalog_be
     
  Check for the port docker image is runnign on. 
  

