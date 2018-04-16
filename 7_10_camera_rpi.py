import picamera

# Create a Pi Camera object
camera = picamera.PiCamera()

# Take a picture with no extra parameters
camera.capture("/home/pi/rpicam.jpg")
