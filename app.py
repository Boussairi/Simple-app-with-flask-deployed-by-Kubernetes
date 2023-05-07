from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "john": "password",
    "mary": "secretpassword"
}

@auth.verify_password
def verify_password(username, password):
    if username in users and password == users[username]:
        return username

@app.route('/')
def home():
    return 'Welcome to my Flask app!'

@app.route('/api/data', methods=['GET', 'POST'])
@auth.login_required
def api_data():
    if request.method == 'GET':
        data = {"name": "John", "age": 30}
        return jsonify(data)
    elif request.method == 'POST':
        data = request.json
        return jsonify(data)

@app.route('/api/users/<username>')
@auth.login_required
def api_users(username):
    if username in users:
        return f"{username} exists"
    else:
        return f"{username} does not exist"

if __name__ == '__main__':
    app.run(debug=True)

