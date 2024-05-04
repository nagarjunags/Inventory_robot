import cv2
from pyzbar.pyzbar import decode
import time
import sqlite3

# Function to create database and table
def create_database():
    conn = sqlite3.connect('Inventory.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS inventory
                 (id INTEGER PRIMARY KEY, Rack TEXT, Product TEXT)''')
    conn.commit()
    conn.close()

# Function to insert scanned QR codes into the database
def insert_into_database(rack, product):
    conn = sqlite3.connect('Inventory.db')
    c = conn.cursor()
    c.execute("INSERT INTO inventory (Rack, Product) VALUES (?, ?)", (rack, product))
    conn.commit()
    conn.close()

# Function to capture frames from the camera and decode them
def capture_and_decode():
    scanned_qrs = []  # List to store scanned QR codes
    rack = None
    product = None

    cam = cv2.VideoCapture(0, cv2.CAP_V4L)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        success, frame = cam.read()

        if not success:
            print("Failed to capture frame from camera")
            break

        decoded_objects = decode(frame)

        for obj in decoded_objects:
            qr_data = obj.data.decode('utf-8')
            if qr_data not in scanned_qrs:
                scanned_qrs.append(qr_data)
                print("Type:", obj.type)
                print("Data:", qr_data)

                if len(scanned_qrs) % 2 == 1:  # Odd index, store in 'Rack'
                    rack = qr_data
                else:  # Even index, store in 'Product'
                    product = qr_data
                    if rack is not None and product is not None:
                        insert_into_database(rack, product)
                    else:
                        print("Error: Missing rack or product information for database insertion")
                
        # Wait for a short duration before capturing the next frame
        time.sleep(0.1)

    cam.release()

if __name__ == "__main__":
    create_database()
    capture_and_decode()
