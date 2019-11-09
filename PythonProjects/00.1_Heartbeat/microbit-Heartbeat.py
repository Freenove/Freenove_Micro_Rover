from microbit import *
while True:
    display.show(Image.HEART)  # Display heartbeat pattern
    sleep(500)                # Stop for 500ms
    display.show(Image.HEART_SMALL)
    sleep(500)