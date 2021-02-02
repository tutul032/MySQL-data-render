
"""
This application establish connection to the database.
If you use different name instead of 'taskdatabase' 
Please change the name of database at line 23 database = 'taskdatabase'   
To see the log for each GET requests to the database open the XAMPP control panel
then click MySQL config -> my.ini and add the following two lines:
general_log = 1
general_log_file="general.log"
Then save the my.ini file and restart the XAMPP control panel again. 
To see the logs please click:
XAMPP control panel -> MySQL Logs -> Browse -> general
"""

# Importing dependencies  
import mysql.connector as msql
import logging
from flask import Flask, request, render_template

# Checking database connection 
try:
     conn = msql.connect(host='localhost', database = 'taskdatabase', user='root', password='')
     print('Database connection successfull')

# once database connection failed raising error
except:
     raise Exception('Database connection failed')

# setting cursor on to the database
cursor = conn.cursor()
app = Flask(__name__)

@app.route("/")
def index():
     # Fetching data to HTML from the database
     if conn.is_connected():

          cursor.execute("SELECT * FROM task")
          data = cursor.fetchall()
          # Logging database and other info at each GET request
          logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s %(threadName)s', level=logging.DEBUG)
          logging.debug('taskdatabase connected')
          # Visualizing data into HTML 
          return render_template("index.html", data = data )

     # raising error on data fetching
     else:
          return "Data fetching from database failed"

# Running the app in the port 5000 at localhost:5000
if (__name__ == "__main__"):
     app.run(port = 5000)