from flask import Flask, request
import cv2, face_recognition, numpy as np

app = Flask(__name__)
known_faces = [face_recognition.face_encodings(cv2.imread("known_faces/budi.jpg"))[0]]

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image'].read()
    npimg = np.frombuffer(file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    unknown_enc = face_recognition.face_encodings(img)
    if unknown_enc:
        result = face_recognition.compare_faces(known_faces, unknown_enc[0])
        if result[0]:
            return "AUTHORIZED"
    return "UNAUTHORIZED"