import Adafruit_BMP.BMP085 as BMP085
import time
from datetime import datetime
import csv

# Create a BM085/BMP180 sensor object
sensor = BMP085.BMP085()

# You may customize and add other values
city = "BARCELONA"

# Infinite loop, end with Control+C
while True:
    # Get local time in ISO format
    localtime = datetime.now().isoformat()

    # Read the temperature from the sensor
    temperature = sensor.read_temperature()

    # Open the CSV file to append new text
    with open('/home/pi/temperatura.csv', 'a', newline='') as csvfile:
        # Configure the CSV object
        temp_writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        # Write the CSV line to your file with the expected parameters
        temp_writer.writerow([localtime,city,temperature])
    # Do it every 60 seconds
    time.sleep(60)
