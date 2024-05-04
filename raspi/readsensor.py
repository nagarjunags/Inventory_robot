import RPi.GPIO as GPIO
import time

# Define GPIO pins connected to the sensor
sensor_pins = [18, 23, 24, 25, 12]  # Example pins, adjust according to your setup

def setup():
    # Set GPIO mode to BCM
    GPIO.setmode(GPIO.BCM)

    # Set GPIO pins as input
    for pin in sensor_pins:
        GPIO.setup(pin, GPIO.IN)

def read_sensor():
    # Read sensor values
    values = [GPIO.input(pin) for pin in sensor_pins]
    return values

if __name__ == "__main__":
    try:
        setup()
        while True:
            sensor_data = read_sensor()
            print("Sensor Data:", sensor_data)
            time.sleep(0.5)  # Adjust sleep time as needed
    except KeyboardInterrupt:
        GPIO.cleanup()
