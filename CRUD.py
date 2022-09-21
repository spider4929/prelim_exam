from crypt import methods
from flask import Flask, jsonify, request

app = Flask(__name__)

heart_records = [
    {
        "heart_id": 1,
        "date": "March 12, 2022",
        "heart_rate": 90,
    },
    {

        "heart_id": 2,
        "date": "March 13, 2022",
        "heart_rate": 80
    }
]

@app.route('/records', methods=['GET'])
def getHeartData():
    return jsonify(heart_records)

@app.route('/records/<int:heart_id>', methods=['GET'])
def getSpecificHeartData(heart_id):
    record = [ record for record in heart_records if record['heart_id'] == heart_id ]
    return jsonify(record)

@app.route('/records', methods=['POST'])
def addHeartData():
    records = request.get_json()
    heart_records.append(records)
    return {'heart_id': len(heart_records)},200

@app.route('/delete_records/<int:heart_id>', methods=['DELETE'])
def deleteHeartData(heart_id):
    record = [ record for record in heart_records if record['heart_id'] == heart_id ]
    heart_records.remove(record[0])

    return jsonify(heart_records),200

@app.route('/update_records/<int:heart_id>', methods=['PUT'])
def updateHeartData(heart_id):
    record = [ record for record in heart_records if record['heart_id'] == heart_id ]
    record[0]['heart_rate'] = request.json['heart_rate']
    return jsonify(heart_records)

if __name__ == '__main__':
    app.run()