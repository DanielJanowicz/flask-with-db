## Importing package
import sqlite3

## Creating database
connect = sqlite3.connect('patients.db')

## Creating cursor
db = connect.cursor()

## Deleting existing table(s)
db.execute('DROP TABLE IF EXISTS patient_table')
connect.commit()

## Creating table
table = """ CREATE TABLE patient_table (
    mrn VARCHAR(255) NOT NULL,
    firstname CHAR(25) NOT NULL,
    lastname CHAR(25) NOT NULL,
    dob DATE NOT NULL,
    hospcode VARCHAR(255) NOT NULL,
    admitdate DATE NOT NULL,
    department VARCHAR(255) NOT NULL,
    fallrisk CHAR(25) NOT NULL
    ); """

db.execute(table)
connect.commit()

## Inserting data
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, hospcode, admitdate, department, fallrisk) values('E94023', 'Sara', 'Smith', '05/21/2000', '03', '09/14/2022', 'ER', 'Low')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, hospcode, admitdate, department, fallrisk) values('E48733', 'Matt', 'Redkay', '02/14/1999', '03', '09/10/2022', 'OR', 'Low')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, hospcode, admitdate, department, fallrisk) values('E81630', 'William', 'Jeffries', '07/19/1940', '04', '08/10/2022', 'ICU', 'High')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, hospcode, admitdate, department, fallrisk) values('E43821', 'Michelle', 'Lanberry', '11/04/1994', '01', '09/20/2022', '4E', 'Medium')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, hospcode, admitdate, department, fallrisk) values('E00843', 'Julia', 'Zugaj', '04/11/2000', '02', '09/02/2022', 'PACU', 'Low')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, hospcode, admitdate, department, fallrisk) values('E94023', 'Vito', 'Bambino', '08/06/1997', '01', '09/22/2022', '5N', 'Low')")

connect.commit()

## Closing connection
connect.close()

