from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/status")
def status():
    return "OK"

@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route("/add_user", methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Missing user data"}), 400
    
    username = data['username']
    if username in users:
        return jsonify({"error": "User already exists"}), 409
    
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run(debug=True)
