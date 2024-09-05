import socket
import cv2
import numpy as np

# Load the pre-trained fire detection model (Haar Cascade)
fire_cascade = cv2.CascadeClassifier('path\\fire_detection_cascade_model.xml')

# Create a socket object for server-side communication (TCP/IP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to localhost (your machine) and port 8089
server.bind(('localhost', 8089))

# Start listening for incoming connections (allow only 1 connection at a time)
server.listen(1)

# Infinite loop to keep the server running
while True:
    # Accept a connection from a client
    conn, addr = server.accept()
    
    # Read the first 4 bytes to get the size of the incoming message
    size = int.from_bytes(conn.recv(4), byteorder='big')
    
    # Receive the actual message from the client (based on the size)
    data = conn.recv(size)
    
    # Decode the received message (assumed to be in ASCII format)
    message = data.decode('ascii')
    
    # If the client sends a 'QUIT' command, the server will close the connection
    if message == 'QUIT':
        print("Received quit command. Closing connection.")
        conn.sendall(b'QUIT-DONE')
        break  # Exit the loop to stop the server
    
    # If the client sends a 'PROCESS' command, the server processes the image
    if message == 'PROCESS':
        try:
            # Load the image for fire detection from the labview 
            frame = cv2.imread(r'path\\image.jpg')
    
            # Check if the image was loaded properly
            if frame is None:
                print("Failed to grab frame")
                continue
    
            # Convert the image to grayscale (required for the cascade classifier)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
            # Use the fire cascade classifier to detect fire in the frame
            fire = fire_cascade.detectMultiScale(frame, 1.2, 5)
    
            # If fire is detected, send '1' to the client
            if len(fire) > 0:
                result = "1"
                conn.sendall(result.encode('ascii'))
                print(result)
            # If no fire is detected, send '0' to the client
            else:
                result = "0"
                conn.sendall(result.encode('ascii'))
                print(result)
            
        except Exception as e:
            # In case of an error, send the error message back to the client
            error = "Error: " + str(e)
            conn.sendall(error.encode('ascii'))
    
# Close the connection and stop the server
conn.close()
server.close()


