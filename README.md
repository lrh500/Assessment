# Parsing GlobalLandTemperaturesByCity  Data with Python and Django

**This is a web application for accessing users to analyse their work related issues using visualisation tools. The application allows users to view the temperature of each city and its details, and to analyse their information using tools such as maps.
The application is built using Python and Django and uses django's own database to store the information. The front end was also designed using Djang.**


Step 1) we use Django's Command module, which allows us to parse CSV files and convert them into database records in Django models (Models). This particular module is used to parse a file called GlobalLandTemperaturesByCity.csv and convert it into two models called country_id and global_tem. The country_id model represents the IDs and names of all countries in the world, while the global_tem model represents data about for each country. First, we delete all the rows in the country_id and global_tem tables to avoid inserting the same data repeatedly. Next, we read the CSV file using the open() function, traversing it line by line and creating new records. Finally, we save the data to the database by calling the save() function.



## Table Relationships for the Data

*Step 2) First, We use an country_list.html template for rendering the data from the Globaltem_change model in the Django web application.It creates a table with a header row containing the names of the different fields in the Globaltem_change model. Then, for each Globaltem_change object passed in via the global_tem_changes context variable, it creates a row in the table with the corresponding data for each field.Overall, this template allows the user to view the data from the Globaltem_change model in a visually appealing and easy-to-read format.*

*Then, the global_tem_change.html file contains a table for displaying climate change data. The table header includes various climate indicators, such as average temperature and temperature fluctuation range. In the table body, the for loop in Django's template language is used to iterate over the values of each climate indicator, displaying the date and numerical values of different indicators for each row of data. This HTML file can be used by Django for dynamically rendering data and presenting it to users.*

### Installation
Clone or download the project code at：

    https://github.com/lrh500/Assessment.git
    
The depolyment of the project on：
    https://assessment-odbh.onrender.com/

To access the project catalogue:

    cd Assessment

Use the pyenv version manager to install and set the local version of Python to 3.7.0.

    pyenv local 3.7.0 # this sets the local version of python to 3.7.0
    python3 -m venv .venv # this creates the virtual environment for you
    source .venv/bin/activate # this activates the virtual environment
    pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.

We will be using Django ( https://www.djangoproject.com ) as the web framework for our application. We install it

     pip install django
This will install django version 3.1.3 (or later) and its associated dependencies. 

We need to specify some settings for the website, which we do in the assessment/assessment/settings.py file. Open it and add this line above the pathlib import Path line:

    import os
	STATIC_ROOT = os.path.join(BASE_DIR, 'static')
	ALLOWED_HOSTS = ['word-otherword.herokuapp.com', 'localhost']
	
After that, enter the following code in Terminal to perform data migration

	python3 manage.py migrate
	python3 manage.py makemigrations climate_change
	python3 manage.py migrate climate_change
	python3 manage.py parse_csv

### Start the server

We use the manage.py command tool by typing this command in the terminal:

    python3 manage.py runserver
If you are doing this on another platform, then you may need to change it (change the port number 8000 as required):

    python3 manage.py runserver 0.0.0.0:8000

### Create view
We can now create a view of our data so that we can see temperatures for all cities, a map that locates a city and shows sixty months of temperature data, select a country to show the average temperature for that country and show the average temperature change as a line graph, we have a detail table that shows the maximum and minimum temperatures at ground level and uncertainty values, and we have created a navigation bar to jump back.

### Using tests
Here are also some basic tests so that you can see how to test whether your code is working properly. They are located in the "Tests" folder and cover model and view tests. There is some repetitive code to load the test database, which can be refactored into a separate file for test file calls. Use the following command to run the tests:

    python3 manage.py test
