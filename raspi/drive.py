import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

class Robot_controll:
    def __init__(self):
        # Set up GPIO pins for left motor
        self.left_forward_pin = 17
        self.left_backward_pin = 18

        # Set up GPIO pins for right motor
        self.right_forward_pin = 22
        self.right_backward_pin = 23

        # Setup GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.left_forward_pin, GPIO.OUT)
        GPIO.setup(self.left_backward_pin, GPIO.OUT)
        GPIO.setup(self.right_forward_pin, GPIO.OUT)
        GPIO.setup(self.right_backward_pin, GPIO.OUT)

    # Function to move the car forward
    def move_forward(self):
        GPIO.output(self.left_forward_pin, GPIO.HIGH)
        GPIO.output(self.left_backward_pin, GPIO.LOW)
        GPIO.output(self.right_forward_pin, GPIO.HIGH)
        GPIO.output(self.right_backward_pin, GPIO.LOW)

    # Function to move the car backward
    def move_backward(self):
        GPIO.output(self.left_forward_pin, GPIO.LOW)
        GPIO.output(self.left_backward_pin, GPIO.HIGH)
        GPIO.output(self.right_forward_pin, GPIO.LOW)
        GPIO.output(self.right_backward_pin, GPIO.HIGH)

    # Function to turn the car left
    def turn_left(self):
        GPIO.output(self.left_forward_pin, GPIO.LOW)
        GPIO.output(self.left_backward_pin, GPIO.HIGH)
        GPIO.output(self.right_forward_pin, GPIO.HIGH)
        GPIO.output(self.right_backward_pin, GPIO.LOW)

    # Function to turn the car right
    def turn_right(self):
        GPIO.output(self.left_forward_pin, GPIO.HIGH)
        GPIO.output(self.left_backward_pin, GPIO.LOW)
        GPIO.output(self.right_forward_pin, GPIO.LOW)
        GPIO.output(self.right_backward_pin, GPIO.HIGH)

    # Function to stop the car
    def stop(self):
        GPIO.output(self.left_forward_pin, GPIO.LOW)
        GPIO.output(self.left_backward_pin, GPIO.LOW)
        GPIO.output(self.right_forward_pin, GPIO.LOW)
        GPIO.output(self.right_backward_pin, GPIO.LOW)

if __name__ == "__main__":
    try:
        car = Robot_controll()
        while True:
            # Take user input
            direction = input("Enter direction (w/s/a/d to move, q to quit): ")

            # Move the car based on user input
            if direction == 'w':
                car.move_forward()
            elif direction == 's':
                car.move_backward()
            elif direction == 'a':
                car.turn_left()
            elif direction == 'd':
                car.turn_right()
            elif direction == 'q':
                break
            else:
                print("Invalid input! Please enter w/s/a/d to move or q to quit.")

    except KeyboardInterrupt:
        print("\nExiting program...")
    finally:
        # Clean up GPIO
        GPIO.cleanup()
