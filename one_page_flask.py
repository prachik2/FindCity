import requests
import json

from flask import Flask, app
from elasticsearch import Elasticsearch
from flask import render_template

res = requests.get('http://localhost:9200')
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
app = Flask(__name__)


@app.route('/')
def country_state_city_data():
    if res.status_code == 200:
        country_req = requests.get(
            'https://raw.githubusercontent.com/praneshsaminathan/country-state-city/master/countries.json')
        country_dict = json.loads(country_req.content)

        state_req = requests.get(
            'https://raw.githubusercontent.com/praneshsaminathan/country-state-city/master/states.json')
        state_dict = json.loads(state_req.content)

        cities_req = requests.get(
            'https://raw.githubusercontent.com/praneshsaminathan/country-state-city/master/cities.json')
        city_dict = json.loads(cities_req.content)

        context_dict = {
            'country':country_dict['countries'],
            'state':state_dict['states'],
            'city':city_dict['cities']
        }

        return render_template('one_page.html', context_dict=context_dict)

