from flask import Flask, jsonify, request
from database import db

app = Flask(__name__)


@app.route("/")
def fetchData():
    try:
        with db() as cnx, cnx.cursor(dictionary=True) as cursor:
            query = ("SELECT * FROM mock_data LIMIT 20;")
            cursor.execute(query)
            data = cursor.fetchall()
            return jsonify(data), 200
    except Exception as e:
        print("ERROR: ", str(e))
        return jsonify({"message": "Internal Error"})


@app.route("/person/<int:id>")
def fetch_by_id(id=None):
    try:
        query = ("SELECT * FROM mock_data WHERE id = %s")
        with db() as cnx, cnx.cursor(dictionary=True) as cursor:
            cursor.execute(query, [id])
            data = cursor.fetchall()
            print(cnx.is_closed())
            if (len(data) <= 0):
                return jsonify({"message": "User not found", "closed": cnx.is_closed()}), 404
            return jsonify({"data": data, "closed": cnx.is_closed()}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 400


@app.route("/test", methods=["POST"])
def insertNewData():
    try:
        data = request.get_json()
        query = ("INSERT INTO mock_data "
                 "(city, country, email, first_name, gender, ip_address, last_name, phone_number, street_address) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        values = tuple(data.values())
        with db() as cnx, cnx.cursor() as cursor:
            cursor.execute(query, values)
            cnx.commit()
        return jsonify({"message": "Data inserted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# @app.route("/data", methods=["POST"])
app.run(host="localhost", port=8080, debug=True)
