import datetime

import pytz
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


cityid_to_timezone = {
    'moscow': 'Europe/Moscow',
    'berlin': 'Europe/Berlin',
    'tokyo': 'Asia/Tokyo',
    'newyork': 'America/New_York',
}

cityid_to_cityname = {
    'moscow': 'Moscow',
    'berlin': 'Berlin',
    'tokyo': 'Tokyo',
    'newyork': 'New York',
}


@app.route('/<city_id>')
def time(city_id):
    if city_id in cityid_to_timezone:
        tz = pytz.timezone(cityid_to_timezone[city_id])
        zone_time = datetime.datetime.now(tz)
        return render_template("time.html",
                               city=cityid_to_cityname[city_id],
                               time=zone_time.strftime('%H:%M'))
    return render_template("not_found.html")

