from flask import Flask, request, jsonify
import re

app = Flask(__name__)

USER = {}

#Home page
@app.route('/', methods=['GET'])
def home():
	return jsonify({'message' : 'welcome to my page'}), 200

@app.route('/api/v1/signup', methods=['POST'])
def signup():

	data = request.get_json()
	name = data["name"]
	username = data["username"]
	email = data["email"]
	password = data["password"]

	if re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+[a-zA-Z0-9-.]+$)", email) == None:
		return jsonify({"message" : "email is invalid"}), 403
	else:
		if username not in USER:
			USER.update({username:{"name":name, "email":email, "password":password}})
			return jsonify(USER), 200
		return jsonify({'message' : 'username already exist'}), 409

if __name__ == '__main__':
	app.run(debug=True)