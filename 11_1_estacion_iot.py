mport time
from http.server import BaseHTTPRequestHandler, HTTPServer
import Adafruit_BMP.BMP085 as BMP085
import RPi.GPIO as GPIO

# Customize with your own values
HOST_NAME = "192.168.1.12"
PORT_NUMBER = 9000

# Inherit the basic RequestHandler and customize for your API
class HTTPReqHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    def do_GET(self):
        # This is our API
        paths = {
            "/temperature": {"status": 200},
            "/pressure": {"status": 200},
            "/altitude": {"status": 200},
            "/ledON": {"status": 200},
            "/ledOFF": {"status": 200}
        }
        if self.path in paths:
            self.respond(paths[self.path])
        else:
            self.respond({"status": 404})
    def handle_http(self, status_code, path):
        self.send_response(status_code)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Process the return content according to our API
        content = "NOK"
        if path == "/temperature":
            content = "{0:0.2f}".format(sensor.read_temperature())
        elif path == "/pressure":
            content = "{0:0.2f}".format(sensor.read_pressure())
        elif path == "/altitude":
            content = "{0:0.2f}".format(sensor.read_altitude())
        elif path == "/ledON":
            GPIO.output(4, GPIO.HIGH)
            content = "OK"
        elif path == "/ledOFF":
            GPIO.output(4, GPIO.LOW)
            content = "OK"
        return bytes(content, "UTF-8")
    def respond(self, opts):
        response = self.handle_http(opts["status"], self.path)
        self.wfile.write(response)

if __name__ == "__main__":
    # Create a BM085/BMP180 sensor object
    sensor = BMP085.BMP085()

    # Use BCM mode as explained in page 37
    GPIO.setmode(GPIO.BCM)

    # Activate channel 4 as output and make it low as default
    GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)

    # Create an HTTPServer object
    server_class = HTTPServer

    # Map it to your own request handler class
    httpd = server_class((HOST_NAME, PORT_NUMBER), HTTPReqHandler)

    # Tell the user that the server started
    print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))

    # Infinite loop, end with Control+C
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    # Reset the GPIOs configuration 
    GPIO.cleanup(4)

    # Close the server
    httpd.server_close()

    # Tell the user that the server stopped
    print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))
