# all the imports
import os
import sqlite3
import pandas as pd
from flask import Flask, redirect, url_for, render_template, request
from contextlib import closing
from pandas_highcharts.core import serialize
import time

# create our little application :)
app = Flask(__name__)

# configuration
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, '../temperature.db'),
    RESAMPLE='M'
))

def render_chart(resample):

    # Read sqlite query results into a pandas DataFrame
    con = sqlite3.connect(app.config['DATABASE'])
    df = pd.read_sql_query("SELECT * from bailey", con, index_col='time', parse_dates='time')
    con.close()

    df = df.resample(resample).mean()

    chart = serialize(df, render_to='my-chart', output_type='json')
    return render_template('highchart.html',chart=chart)

@app.route('/hour')
def hour():
    return render_chart('H')

@app.route('/month')
def month():
    return render_chart('M')

@app.route('/day')
def day():
    return render_chart('D')

@app.route('/year')
def year():
    return render_chart('Y')

@app.route('/resample',methods = ['POST', 'GET'])
def resample():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect('/')
   else:
      user = request.args.get('nm')
      return redirect('/')


@app.route('/')
def entry():
    return redirect('/hour')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0')
