from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

@app.route('/sum', methods=['POST'])
def add_numbers():
    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")

    if num1 is None or num2 is None:
        return jsonify({"error": "Missing input numbers"}), 400

    try:
        sum_result = float(num1) + float(num2)
        return jsonify({"sum": sum_result})
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Now, port 5000 is explicitly mentioned
