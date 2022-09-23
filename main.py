## Importing packages
from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

## Function to call database
def db_connection():
    dir = os.getcwd() + '/patients.db'
    print('dir', dir)
    conn = sqlite3.connect(dir)
    conn.row_factory = sqlite3.Row
    return conn

## Setting up the route

@app.route('/')
def index():
    db = db_connection()
    patientListSql = db.execute('SELECT * FROM patients').fetchall()
    db.close()
    print('patientListSql', patientListSql)
    return render_template('index.html', patientList=patientListSql)

@app.route('/patients')
def patients():
    db1 = db_connection()
    patientListSql = db1.execute('SELECT * FROM patients').fetchall()
    db1.close()
    print('patientListSql', patientListSql)
    return render_template('index.html', patientList=patientListSql)

## Ports & Hosts
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)