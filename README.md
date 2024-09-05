# Smart Fire-Detection-and-Mitigation system


This project integrates a fire detection system using a combination of sensors, a camera, and actuators. The system detects fires through both sensor data and a real-time camera feed, and responds accordingly with actuators like a fan and a submerged water motor to mitigate the detected fire.

## Features

- **Real-time Fire Detection**: Uses a camera and computer vision (Haar Cascade) for detecting fire.
- **Sensor Monitoring**: Includes flame, temperature, and gas sensors to detect fire conditions.
- **Automated Actuation**: Controls a fan and water motor when a fire is detected.
- **LabVIEW Interface**: Provides real-time monitoring, control, and visualization of sensor outputs.

## Sensors and Actuators

### Sensors

- **Flame Sensor**: Detects visible flames.
- **Temperature Sensor**: Monitors ambient temperature to detect heat anomalies.
- **MQ2 Gas Sensor**: Detects the presence of flammable gases (e.g., propane, methane).
- **Camera**: Detects fire visually using a pre-trained Haar Cascade model.

### Actuators

- **Fan**: Cools down the surrounding area when the temperature is high and work as a eshaust fan when gas detected.
- **Submerged Water Motor**: Activates to release water when a fire is detected.
- **Buzzer**: Alerts users when a fire or dangerous gas is detected.

## Project Structure

### Python Fire Detection Script (`fire_detection.py`)

- Performs real-time fire detection using a camera and Haar Cascade for image processing.
- Communicates over TCP/IP with the LabVIEW interface to send fire detection results.

### LabVIEW Interface

- Monitors sensor outputs and controls the actuators.
- Displays real-time video feed for fire detection and graphical gauges for sensor outputs.

#### LabVIEW Interface Overview

- **Live Video Feed**: Shows the camera feed for real-time fire detection.
- **Sensor Gauges**:
  - IR sensor gauge with voltage output.
  - Temperature gauge with real-time temperature readings.
  - MQ2 gas sensor gauge indicating gas levels.
- **Controls**:
  - Set threshold values for the sensors (flame, temperature, gas) to trigger actuators.
- **Outputs**:
  - Indicator lights and gauges show whether fire or gas is detected.

## Python Script (`fire_detection.py`)

### Key Functions

- **Server Setup**: Acts as a TCP server, listening for commands.
- **Image Processing**: Processes the camera feed to detect fire using the Haar Cascade model.
- **Result Communication**: Sends detection results (1 for fire, 0 for no fire) back to the client (LabVIEW interface).
- **Error Handling**: Sends any errors encountered during image processing back to the client.

### Usage

1. **Run the Python Script**:
    ```bash
    python fire_detection.py
    ```

2. **Start the LabVIEW Interface**: Configure the sensor thresholds and start monitoring through the VI file.

## System Requirements

- Python 3.x
- OpenCV (cv2 library)
- LabVIEW
- Flame, temperature, MQ2 gas sensors, and a camera
- Fan, submerged water motor, and buzzer as actuators

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/fire-detection-system.git
    ```

2. **Install the required Python libraries**:
    ```bash
    pip install opencv-python numpy
    ```

3. **Run the Python Script**:
    ```bash
    python fire_detection.py
    ```

4. **Open LabVIEW VI**: Configure thresholds, start the interface, and monitor the system.



