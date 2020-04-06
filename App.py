from flask import Flask, request, render_template, jsonify
import datetime
from pytz import timezone
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route('/<city>')
def time(city):
    if city == 'moscow':
        zone_time = datetime.datetime.now('Europe/Moscow')
        return render_template("time.html", city=city, time=zone_time.strftime('%H:%M'))
    if city == 'berlin':
        zone_time = datetime.datetime.now('Europe/Berlin')
        return render_template("time.html", city=city, time=zone_time.strftime('%H:%M'))
    if city == 'tokyo':
        zone_time = datetime.datetime.now('Asia/Tokyo')
        return render_template("time.html", city=city, time=zone_time.strftime('%H:%M'))
    if city == 'newyork':
        zone_time = datetime.datetime.now('America/New_York')
        return render_template("time.html", city=city, time=zone_time.strftime('%H:%M'))
    else:
        return render_template("not_found.html")

if __name__ == '__main__':
    app.run()
