# TV Example
#
# Note: To run this example you will need a wireless tv shield for your OpenMV Cam.
#
# The wireless video tv Shield allows you to view your OpenMV Cam's frame buffer on the go.

import sensor, image, tv

sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.RGB565) # or sensor.GRAYSCALE
sensor.set_framesize(sensor.QQVGA)
tv.init() # Initialize the tv.
tv.channel(8) # For wireless video transmitter shield
while(True):
    tv.display(sensor.snapshot()) # Take a picture and display the image.
