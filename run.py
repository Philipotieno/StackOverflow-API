from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
	return jsonify({'message' : 'welcome to my page'})


if __name__ == '__main__':
	app.run(debug=True)