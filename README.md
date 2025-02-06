# Catalog App Backend

This is the backend service for the **Catalog App**, built using Django.

## Getting Started

Make sure port 8000 is available. 

run following commands:
  
     lsof -i :8000
     
This will show you the process ID (PID) of the application using port 8000. If you see a process, kill it using the below command. (Make sure to restart it once you are done with the catalog_app)

    kill -9 <PID>

You can run this backend in two ways:


### 1. Clone and Install Dependencies
   Clone this repository:
   
      git clone https://github.com/prashantkaushik97/catalog_be/
      cd catalog_be
   
   Install dependencies:
   
      pip install -r requirements.txt
      
     python manage.py runserver 0.0.0.0:8000
  
  


### 2. Run with Docker

     docker pull prkaushi/catalog_be
     
     docker run -p 8000:8000 prkaushi/catalog_be
     
  Check for the port docker image is runnign on. 
  

