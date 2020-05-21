from flask import Flask, request, jsonify
app = Flask(__name__)

id_count = 0

@app.route('/id', methods=['GET'])
def respond():
    response = {"id" : id_count}
    id_count += 1

    # Return the response in json format
    return jsonify(response)


# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
