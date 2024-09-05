import socket
import cv2
import numpy as np

# Load the cascade
fire_cascade = cv2.CascadeClassifier('D:\\ML projects\\Handcalculator\\fire_detection_cascade_model.xml')


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8089))
server.listen(1)

while True:
    conn, addr = server.accept()
    # cmnd = conn.recv(4)  # The default size of the command packet is 4 bytes
    # print(cmnd)
    size = int.from_bytes(conn.recv(4), byteorder='big')
    #print(size)
        # Receive the full message
    data = conn.recv(size)
    message = data.decode('ascii')
    #print(message)
    if message == 'QUIT':
        print("Received quit command. Closing connection.")
        conn.sendall(b'QUIT-DONE')
        break  # Exit the loop and close the connection
    if message == 'PROCESS':
        #process image
        try:
            frame = cv2.imread(r'D:\\SEM 4\\Acedemics\\Electrical mearsuments\\project\\image\\image.jpg')
    
            if frame is None:
                print("Failed to grab frame")
                continue
    
            # Convert frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
            # Detect fire in the frame
            fire = fire_cascade.detectMultiScale(frame, 1.2, 5)
    
            if len(fire) > 0:  # Check if any fire is detected
                result = "1"
                conn.sendall(result.encode('ascii'))
                print(result)
            else:
                result = "0"
                conn.sendall(result.encode('ascii'))
                print(result)
            
        except Exception as e:
            error = "Error: " + str(e)
            conn.sendall(error.encode('ascii'))
    
conn.close()
server.close()




