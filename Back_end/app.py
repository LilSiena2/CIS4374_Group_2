'''from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import mysql.connector
import os

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="youruser",
    password="yourpassword",
    database="taylor_ai"
)
cursor = db.cursor()

# OCR Function
def extract_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

# Upload Endpoint
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    extracted_text = extract_text(file_path)

    # Example AI Parsing (Basic Split)
    customer_name = extracted_text.split('\n')[0]
    service_type = "Alteration"  # Placeholder for AI logic
    cost = 0.0  # Placeholder

    # Insert into DB
    cursor.execute(
        "INSERT INTO tickets (customer_name, service_type, cost) VALUES (%s, %s, %s)",
        (customer_name, service_type, cost)
    )
    db.commit()

    return jsonify({"message": "File processed", "data": extracted_text})

# Get All Tickets
@app.route('/tickets', methods=['GET'])
def get_tickets():
    cursor.execute("SELECT * FROM tickets")
    records = cursor.fetchall()
    return jsonify(records)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
'''