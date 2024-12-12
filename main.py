from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the API!"

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'name': 'John Doe',
        'age': 30,
        'occupation': 'Software Developer'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)