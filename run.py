from flask import Flask, request, jsonify

app = Flask(__name__)

USER = {}

#Home page
@app.route('/', methods=['GET'])
def home():
	return jsonify({'message' : 'welcome to my page'}), 200

@app.route('/api/v1/signup', methods=['POST'])
def signup():
	name = request.get_json()["name"]
	username = request.get_json()["username"]
	email = request.get_json()["email"]
	password = request.get_json()["password"]

	if username not in USER:
		USER.update({username:{"name":name, "email":email, "password":password}})
		return jsonify(USER), 200
	return jsonify({'message' : 'username already exist'}), 409

if __name__ == '__main__':
	app.run(debug=True)