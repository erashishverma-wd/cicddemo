from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello/<username>', methods=['GET'])
def hello(username):
    return jsonify(message=f'Hello, {username}!'), 200


@app.route('/api/getSum/<num1>/<num2>', methods=['GET'])
def get_sum(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 + num2
        return jsonify(sum=result), 200
    except ValueError:
        return jsonify(error='Invalid input. Please provide two numbers.'), 400
    



if __name__ == '__main__':
    app.run(debug=True)