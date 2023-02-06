# This code is a Flask web application that displays a webpage with the current year and a random number, and another webpage with data on a person's name, including an estimated age and gender.

# Importing necessary modules and libraries
from flask import Flask, render_template
import random as rd
import datetime
import requests

# Creating a Flask object for the application
app = Flask(__name__)

# Defining a route for the home page of the application
@app.route('/')
def hmpage():
    # Calculating the current year
    current_year = str(datetime.date.today()).split("-")[0]

    # Generating a random number between 0 and 9
    random_number = rd.randint(0, 9)

    # Returning the index.html template and passing the current year and random number as variables
    return render_template('index.html', year=current_year, num=random_number)

# Defining a route that takes a person's name as an argument
@app.route('/<name>')
def api_call(name):
    # Making a request to the agify API to retrieve estimated age data
    response = requests.get(url=f'https://api.agify.io/?name={name}')
    age_data = response.json()
    initial_guess = age_data.get("age")

    # Making a request to the genderize API to retrieve gender data
    response1 = requests.get(url=f"https://api.genderize.io/?name={name}")
    gender_data = response1.json()
    sex = gender_data.get("gender")

    # If data was retrieved from either API, return the name-scrapper.html template with the data, otherwise return a message indicating no data was found
    if initial_guess is not None or sex is not None:
        return render_template('name-scrapper.html', username=name, gender=sex, age_initial_guess=initial_guess)
    return "<h1>Unfortunately we couldn't found any kind of data about you.</h1>"

# Running the application if the script is executed as the main module
if __name__ == "__main__":
    app.run()
