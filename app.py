from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from honeypot import honeypot_detection
from security import encrypt_data, decrypt_data

app = Flask(__name__)

# Load pre-trained behavioral biometrics model
model = tf.keras.models.load_model('mouse_movement_model.h5')

@app.route('/api/analyze-mouse', methods=['POST'])
def analyze_mouse():
    data = request.json['mouseData']
    mouse_movement = np.array([[d['x'], d['y'], d['time']] for d in data])
    
    # Preprocess data for ML model
    mouse_movement = np.expand_dims(mouse_movement, axis=0)
    
    # Predict if human or bot
    prediction = model.predict(mouse_movement)
    is_human = prediction[0][0] > 0.5
    
    # Check for honeypot trap
    honeypot_triggered = honeypot_detection(request)

    if honeypot_triggered:
        return jsonify({'isHuman': False})
    
    return jsonify({'isHuman': is_human})

# Encryption example
@app.route('/api/secure', methods=['POST'])
def secure_data():
    data = request.json['data']
    encrypted = encrypt_data(data)
    return jsonify({'encrypted': encrypted})

if __name__ == '__main__':
    app.run(debug=True)
