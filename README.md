# MySQL-data-render
Install the dependencies to run the app.py such as Python Flask,
mysql.connector using:

pip install mysql-connector-python
pip install Flask

This app connects the taskdatabase which is created using main.py, 
visualize data from taskdatabase.

To enable log query for each GET request Please 
open the XAMPP control panel then click 
MySQL config -> my.ini and add the following two lines:
general_log = 1
general_log_file="general.log"
Then save the my.ini file and restart the XAMPP control panel again
by running the XAMPP_stop, XAMPP_start 
To see the logs please click:
XAMPP control panel -> MySQL Logs -> Browse -> general

Please run the main.py before running app.py. 
Keep running the xampp server and browse localhost:5000 
for the html data from taskdatabase