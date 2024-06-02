from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# Configuring JWT
app.config['SECRET_KEY'] = 'your_jwt_secret_key'  # Changed from JWT_SECRET_KEY to SECRET_KEY for simplicity
jwt_manager = JWTManager(app)

# User data structure
users_db = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("mypassword"),  # Changed the password string
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("mypassword"),  # Changed the password string
        "role": "admin"
    }
}

@auth.verify_password
def authenticate_user(username, password):
    user_info = users_db.get(username)
    if user_info and check_password_hash(user_info["password"], password):
        return user_info
    return None

@app.route('/basic-auth', methods=['GET'])
@auth.login_required
def access_basic_auth():
    return "Basic Authentication: Access Granted"

@app.route('/token-auth', methods=['POST'])
def token_authentication():
    username = request.json.get("username")
    password = request.json.get("password")
    if not username or not password:
        return jsonify({"error": "Username or password missing"}), 400
    user_info = users_db.get(username)
    if user_info and check_password_hash(user_info["password"], password):
        token = create_access_token(identity={'username': username, 'role': user_info['role']})
        return jsonify(access_token=token), 200
    return jsonify({"error": "Invalid username or password"}), 401

@app.route('/jwt-access', methods=['GET'])
@jwt_required()
def jwt_access():
    return "JWT Authentication: Access Granted"

@app.route('/admin-access', methods=['GET'])
@jwt_required()
def restricted_admin_access():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin rights required"}), 403
    return "Admin Access: Granted"

# Custom handlers for JWT errors
@jwt_manager.unauthorized_loader
def unauthorized_response(reason):
    return jsonify({"error": "Unauthorized: " + reason}), 401

@jwt_manager.invalid_token_loader
def invalid_token_response(reason):
    return jsonify({"error": "Invalid Token: " + reason}), 401

@jwt_manager.expired_token_loader
def expired_token_response(reason):
    return jsonify({"error": "Token Expired: " + reason}), 401

@jwt_manager.revoked_token_loader
def revoked_token_response(reason):
    return jsonify({"error": "Token Revoked: " + reason}), 401

@jwt_manager.needs_fresh_token_loader
def fresh_token_required(reason):
    return jsonify({"error": "Fresh Token Required: " + reason}), 401

if __name__ == '__main__':
    app.run(debug=True)
