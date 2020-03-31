from flask import Flask, request, render_template
from datetime import datetime
import pytz


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route('/moscow')
def datetime.now(tz=city_tz):
        city_tz=pytz.timezone('Europe/Moscow')
        return render_template("time.html", city='Moscow', time=city_tz.strftime('%T'))
@app.route('/berlin')
def datetime.now(tz=city_tz):
        city_tz=pytz.timezone('Europe/Berlin')
        return render_template("time.html", city='Berlin', time=city_tz.strftime('%T'))
@app.route('/tokio')
def datetime.now(tz=city_tz):
        city_tz=pytz.timezone('Asia/Tokio')
        return render_template("time.html", city='Tokio', time=city_tz.strftime('%T'))
@app.route('/newyork')
def datetime.now(tz=city_tz):
        city_tz=pytz.timezone('America/New York')
        return render_template("time.html", city='New York', time=city_tz.strftime('%T'))

@app.route('/api', methods = ['GET'])
def getTime():
      error = None
      if request.method == 'GET':
         searchword=request.args.get('city', ' ' )
      else:
          return render_template("not_found.html")
def get_tasks(city_tz):
    return jsonify({"city": 'city', "hour": datetime.datetime.now(city_tz).hour , "minute": datetime.datetime.now(city_tz).minute})
