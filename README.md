# ESP32-CAM Face Recognition AI Project

## Overview
This project demonstrates how to perform real-time face recognition using an ESP32-CAM module, Python Flask server, and Arduino-based hardware control.

## Features
- ESP32-CAM captures and streams camera feed.
- Flask server processes the face recognition using `face_recognition` library.
- Arduino receives recognition result and controls an actuator.

## Folder Structure
```
esp32_face_recognition/
├── arduino/                # Arduino hardware control
│   └── arduino_control.ino
├── esp32/                  # ESP32-CAM firmware
│   └── esp32_cam_face_stream.ino
├── server/                 # Python Flask AI server
│   ├── app.py
│   ├── requirements.txt
│   └── known_faces/        # Folder for reference face images
├── README.md
```

## Setup

### ESP32-CAM
1. Install ESP32 Board Manager on Arduino IDE.
2. Upload `esp32_cam_face_stream.ino` to your ESP32-CAM.
3. Update your Wi-Fi credentials.

### Python Flask Server
```bash
cd server/
pip install -r requirements.txt
python app.py
```
Ensure you have an image named `budi.jpg` inside the `known_faces/` directory for recognition.

### Arduino
1. Connect an LED or servo to digital pin.
2. Upload `arduino_control.ino` to Arduino.
3. Connect Arduino to ESP32 via Serial or via PC.

## Usage
- Power on ESP32-CAM.
- ESP32 sends image to server `/upload`.
- Server checks if face matches and returns "AUTHORIZED" or "UNAUTHORIZED".
- Arduino reacts based on this result.

## Optional Enhancements
- Replace serial with MQTT.
- Deploy server using Docker.
- Build a face registration UI.