import os
from drive import Robot_controll
import RPi.GPIO as GPIO
import time

class LineFollowingCar:
    def __init__(self):
        # Initialize the Robot_controll instance
        self.car = Robot_controll()

        # Set up GPIO pins for line sensors
        self.line_sensor_pins = [5, 6, 13, 19, 26]

        # Setup GPIO for line sensors
        GPIO.setmode(GPIO.BCM)
        for pin in self.line_sensor_pins:
            GPIO.setup(pin, GPIO.IN)

    def follow_line(self):
        try:
            while True:
                # Clear the terminal screen
                os.system('clear')

                # Read line sensor values
                sensor_values = [GPIO.input(pin) for pin in self.line_sensor_pins]

                # Print sensor values
                print("Sensor Values:", sensor_values)

                # Example logic: If any sensor detects the line, turn towards that direction
                if any(sensor_values):
                    if sensor_values[1] == 0:  # Sensor 1 detects the line
                        print("Turning left")
                    elif sensor_values[4] == 0:  # Sensor 5 detects the line
                        print("Turning right")
                        self.car.turn_right()        
                    else:
                        print("Moving forward")
                        self.car.move_backward()
                else:
                    # If no sensor detects the line, stop
                    print("Stopping")
                    self.car.stop()

                # Adjust the sleep time according to your requirements
                # time.sleep(0.1)

        except KeyboardInterrupt:
            print("\nExiting program...")
        finally:
            # Clean up GPIO
            GPIO.cleanup()

if __name__ == "__main__":
    line_following_car = LineFollowingCar()
    line_following_car.follow_line()



