from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {
        "Contact": '0000000000',
        "Name": 'Vampire',
        "done": False,
        "id": 1
    },
    {
        "Contact": "1111111111",
        "Name": "Zombie",
        "done": False,
        "id": 2
    }
]

@app.route("/app-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": 'error',
            "message": 'Please Provide the data!'
        }, 400)

@app.route("/get-data")
def getData():
    return jsonify({'data': data})


if(__name__ == "__main__"):
    app.run(debug=True)
