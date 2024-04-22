import RPi.GPIO as GPIO
import os
#-------------installing the dependencies----------------------------
#os.system("sudo pip3 install RPi.GPIO")
#---------------------------------------------------------------------

# Set up GPIO pins for left motor
left_forward_pin = 17
left_backward_pin = 18

# Set up GPIO pins for right motor
right_forward_pin = 22
right_backward_pin = 23

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(left_forward_pin, GPIO.OUT)
GPIO.setup(left_backward_pin, GPIO.OUT)
GPIO.setup(right_forward_pin, GPIO.OUT)
GPIO.setup(right_backward_pin, GPIO.OUT)

# Function to move the car forward
def move_forward():
    GPIO.output(left_forward_pin, GPIO.HIGH)
    GPIO.output(left_backward_pin, GPIO.LOW)
    GPIO.output(right_forward_pin, GPIO.HIGH)
    GPIO.output(right_backward_pin, GPIO.LOW)

# Function to move the car backward
def move_backward():
    GPIO.output(left_forward_pin, GPIO.LOW)
    GPIO.output(left_backward_pin, GPIO.HIGH)
    GPIO.output(right_forward_pin, GPIO.LOW)
    GPIO.output(right_backward_pin, GPIO.HIGH)

# Function to turn the car left
def turn_left():
    GPIO.output(left_forward_pin, GPIO.LOW)
    GPIO.output(left_backward_pin, GPIO.HIGH)
    GPIO.output(right_forward_pin, GPIO.HIGH)
    GPIO.output(right_backward_pin, GPIO.LOW)

# Function to turn the car right
def turn_right():
    GPIO.output(left_forward_pin, GPIO.HIGH)
    GPIO.output(left_backward_pin, GPIO.LOW)
    GPIO.output(right_forward_pin, GPIO.LOW)
    GPIO.output(right_backward_pin, GPIO.HIGH)

# Function to stop the car
def stop():
    GPIO.output(left_forward_pin, GPIO.LOW)
    GPIO.output(left_backward_pin, GPIO.LOW)
    GPIO.output(right_forward_pin, GPIO.LOW)
    GPIO.output(right_backward_pin, GPIO.LOW)

try:
    while True:
        # Take user input
        direction = input("Enter direction (w/s/a/d to move, q to quit): ")

        # Move the car based on user input
        if direction == 'w':
            move_forward()
        elif direction == 's':
            move_backward()
        elif direction == 'a':
            turn_left()
        elif direction == 'd':
            turn_right()
        elif direction == 'q':
            break
        else:
            print("Invalid input! Please enter w/s/a/d to move or q to quit.")

except KeyboardInterrupt:
    print("\nExiting program...")
finally:
    # Clean up GPIO
    GPIO.cleanup()
