import cv2
from pyzbar.pyzbar import decode
import requests
import numpy as np

# URL of the webcam server
stream_url = "http://192.168.248.185:8080/"

try:
    # Open a connection to the webcam server
    response = requests.get(stream_url, stream=True)
    response.raise_for_status()  # Raise an error for non-successful responses
    
    # Read the entire content of the response into memory
    content = response.content
except requests.RequestException as e:
    print("Error:", e)
    exit()

# Open the file in append mode
f = open("demofile2.txt", "a")

# Create a flag to keep track of window status
window_open = True

while window_open:
    # Iterate over the content of the response
    for chunk in content.iter_chunks(chunk_size=1024):
        # Convert the received chunk to a numpy array
        nparr = np.frombuffer(chunk, dtype=np.uint8)

        # Decode the frame
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Check if the frame is valid
        if frame is None:
            print("Error: Failed to decode frame")
            continue

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Decode QR codes from the grayscale frame
        qr_codes = decode(gray)

        # Process the decoded QR codes
        for qr_code in qr_codes:
            qr_data = qr_code.data.decode('utf-8')
            print("Data:", qr_data)
            
            # Write the decoded data to the file
            f.write(qr_data + '\n')

        # Display the frame (optional)
        cv2.imshow("OurQR_Code_Scanner", frame)

        # Close the video stream when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            window_open = False
            break

# Close the OpenCV window
cv2.destroyAllWindows()

# Close the file
f.close()
