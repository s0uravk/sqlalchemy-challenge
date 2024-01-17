# Import the dependencies.

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, engine, func, text, desc
from flask import Flask, json, jsonify

Base = automap_base()
engine = create_engine('sqlite:///Resources/hawaii.sqlite')

# reflect the tables
Base.prepare(autoload_with = engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def index():
  #List of all the available routes
  return(f"Avaiable routes :<br>"
          f"/api/v1.0/precipitation<br>"
          f"/api/v1.0/stations<br>"
          f"/api/v1.0/tobs<br>"
          f"/api/v1.0/<start><br>"
          f"/api/v1.0/<start>/<end><br>"
          f"Please enter the start and end date in YYYY-MM-DD format.")
          
@app.route("/api/v1.0/precipitation")
def precipitation():
  session = Session(bind = engine)
  
  my_date = session.query(func.max(Measurement.date)).all()
  
  query_date = datetime.strptime(my_date[0][0], '%Y-%m-%d') - timedelta(days = 366)
  prcp_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > query_date).all()
  
  session.close()

  
  link1 = []
  for date, prcp in prcp_data:
    dict1= {}
    dict1['date'] = date
    dict1['prcp'] = prcp
    link1.append(dict1)

  return(jsonify(link1))

@app.route("/api/v1.0/stations")
def stations():
  session = Session(bind = engine)

  station_ls = session.query(Station.station).all()

  session.close()

  link2 = []

  for data in station_ls:
    link2.append(data.station)
  return(jsonify(link2))

@app.route("/api/v1.0/tobs")
def tobs():
  session = Session(bind = engine)

  my_date = session.query(func.max(Measurement.date)).all()
  
  query_date = datetime.strptime(my_date[0][0], '%Y-%m-%d') - timedelta(days = 366)

  active_station = session.query(Measurement.station, func.count(Measurement.station))\
                .group_by(Measurement.station)\
                .order_by(desc(func.count(Measurement.station))).all()

  results = session.query(Measurement.date, Measurement.tobs)\
            .filter(Measurement.station == active_station[0][0])\
            .filter(Measurement.date > query_date)

  session.close()

  link3 = []

  for date, tobs in results:
    dict2 = {}
    dict2['date'] = date
    dict2['tobs'] = tobs
    link3.append(dict2)

  return(jsonify(link3))

@app.route("/api/v1.0/<start>")
def startwith(start):
  session = Session(bind = engine)
  start_results = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
                  .filter(Measurement.date >= start)\
                  .group_by(Measurement.date).all()
  session.close()

  link4 = []

  for date, min, avg, max in start_results:
    dict3 = {}
    dict3['date'] = date
    dict3['min'] = min
    dict3['avg'] = avg
    dict3['max'] = max
    link4.append(dict3)

  return(jsonify(link4))

@app.route("/api/v1.0/<start>/<end>")
def startendwith(start,end):
  session = Session(bind = engine)
  start_end_results = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
                  .filter(Measurement.date >= start)\
                  .filter(Measurement.date <= end)\
                  .group_by(Measurement.date).all()
  session.close()

  link5 = []

  for date, min, avg, max in start_end_results:
    dict4 = {}
    dict4['date'] = date
    dict4['min'] = min
    dict4['avg'] = avg
    dict4['max'] = max
    link5.append(dict4)

  return(jsonify(link5))

if __name__ == '__main__':
  app.run(debug = True)
  