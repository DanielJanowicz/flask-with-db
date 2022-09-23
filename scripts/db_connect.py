## Importing packages
import sqlite3
import pandas as pd

## Creating connection function
def db_connection():
    conn = sqlite3.connect('patients.db')
    conn.row_factory = sqlite3.Row
    return conn

db = db_connection()
patientListSql = db.execute('SELECT * FROM patient_table').fetchall()
patientListSql

## Saving data to a dataframe
df = pd.DataFrame(patientListSql)
df

## Renaming the Columns
df.columns = ['mrn', 'firstname', 'lastname', 'dob', 'hospcode', 'admitdate', 'department', 'fallrisk']
df

df.to_csv('patients.csv', index=False)