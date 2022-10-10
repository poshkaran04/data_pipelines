import pandas as pd
import pyodbc as pc
import os
import csv

from dotenv import load_dotenv
config = load_dotenv('.env')

server = os.environ.get('MS_SERVER')
database = os.environ.get('MS_DATABASE')
username = os.environ.get('MS_USERNAME')
password = os.environ.get('MS_PASSWORD')

connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + \
    server + ';DATABASE=' + database + ';UID='+username+';PWD='+password
cnxn = pc.connect(connection_string, autocommit=True)
cur = cnxn.cursor()

cur.execute("TRUNCATE TABLE dbo.Person")

with open('person.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    next(f)
    for row in reader:
        cur.execute(
            "INSERT INTO dbo.Person(ID, Job_Title, Email_Address, FirstName_LastName, Time_Stamp) VALUES (?, ?, ?, ?, GETDATE())", row[0], row[1], row[2], row[3])
cnxn.commit()
cnxn.close()
