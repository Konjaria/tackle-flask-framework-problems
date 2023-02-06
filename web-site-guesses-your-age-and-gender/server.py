from flask import Flask
from flask import render_template
import random as rd
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def hmpage():
    # Angela's version: current_year = datetime.datetime.now().year
    # My version below both work
    current_year = str(datetime.date.today()).split("-")[0]
    random_number = rd.randint(0, 9)
    return render_template('index.html', year=current_year, num=random_number)

@app.route('/<name>')
def api_call(name):
    response = requests.get(url=f'https://api.agify.io/?name={name}')
    print(response.status_code)
    age_data = response.json()
    initial_guess = age_data.get("age")

    response1 = requests.get(url=f"https://api.genderize.io/?name={name}")
    print(response1.status_code)
    gender_data = response1.json()
    sex = gender_data.get("gender")

    if initial_guess is not None or sex is not None:
        return render_template('name-scrapper.html', username=name, gender=sex, age_initial_guess=initial_guess)
    return "<h1>Unfortunately we couldn't found any kind of data about you.</h1>"


if __name__ == "__main__":
    app.run()
