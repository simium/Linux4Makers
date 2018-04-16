import Adafruit_BMP.BMP085 as BMP085
import time
from datetime import datetime
import sqlite3

# Create a BM085/BMP180 sensor object
sensor = BMP085.BMP085()

# You may customize and add other values
city = "BARCELONA"

# Create a SQLite3 connection to a DB file
# (it will create it if it cant find it)
conn = sqlite3.connect('/home/pi/temperatura.db')
c = conn.cursor()

# Execute a SQL query to create the table,
# commit the changes
# and close the connection
c.execute('''CREATE TABLE IF NOT EXISTS temperaturas
        (localtime text, city text, temperatura real)''')
conn.commit()
conn.close()

# Infinite loop, end with Control+C
while True:
    # Get local time in ISO format
    localtime = datetime.now().isoformat()

    # Read the temperature from the sensor
    temperature = sensor.read_temperature()

    # Connect to the DB again
    conn = sqlite3.connect('temperatura.db')
    c = conn.cursor()

    # Execute an INSERT query with your values,
    # commit the changes
    # and close the connection
    c.execute("INSERT INTO temperaturas VALUES ('{0}','{1}',{2})".format(localtime, city, temperature))
    conn.commit()
    conn.close()

    # Do it every 60 seconds
    time.sleep(60)
