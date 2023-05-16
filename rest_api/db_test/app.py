from flask import Flask,request, jsonify
from flask_sqlalchemy import SQLAlchemy
import urllib.parse
from flask_migrate import Migrate

password = urllib.parse.quote_plus('TM@chine123')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{password}@localhost:3306/flask_db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

@app.route('/create-user', methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        name = data["name"]
        email = data["email"]

        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()

        return 'User created successfully', 201  # Return a success message with HTTP status code 201
    except KeyError as e:
        error_message = f'Missing required field: {e.args[0]}'
        return jsonify({'error': error_message}), 400  # Return a JSON response with an error message and HTTP status code 400
    except Exception as e:

      if str(e).find("Duplicate entry") >= 0:
        return jsonify({'error': "Duplicate entry"}), 500  # Return a JSON response with the error message and HTTP status code 500
      else:
        # Handle other exceptions and return an appropriate error response
        print(str(e))
        return jsonify({'error': "Internal error."}), 500  # Return a JSON response with the error message and HTTP status code 500


app.run(host="localhost", port=8000, debug=True)
