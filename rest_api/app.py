from flask import Flask, jsonify, request
from database import connectDB
import json

app = Flask(__name__)


def fetchData():
    cnx = connectDB()
    cnx.reconnect()
    cursor = cnx.cursor(dictionary=True)
    query = ("SELECT * FROM mock_data LIMIT 20;")
    cursor.execute(query)
    data = cursor.fetchall()
    cnx.close()
    return data

#

    city,
    country,
    email,
    first_name,
    gender,
    id,
    ip_address,
    last_name,
    phone_number,
    street_address,


@app.route("/")
def hello_world():
    data = fetchData()
    return jsonify(data)


@app.route("/test", methods=["POST"])
def insertNewData():
    data = request.get_json()
    cnx = connectDB()
    cnx.reconnect()
    cursor = cnx.cursor()
    query = ("INSERT INTO mock_data"
             "(city,country,email,first_name,gender,id,ip_address,last_name,phone_number,street_address)"
             "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
             )
    values = []
    for key in data:
        values.append(data[key])
    print(values)
    response = cursor.execute(query, values)
    cnx.commit()
    cursor.close()
    cnx.close()
    print(response)
    return jsonify("message:Okay")


# @app.route("/data", methods=["POST"])


app.run(host="localhost", port=8080, debug=True)
