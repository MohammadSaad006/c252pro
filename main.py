# importing firebase_admin module
import firebase_admin

# importing firestore.py module to create firestore client
from firebase_admin import firestore

# importing credentials.py module from firebase_admin folder
from firebase_admin import credentials

# importing flask modules
from flask import Flask , request , render_template , jsonify

cred = credentials.Certificate("potentiometer-9e07c-firebase-adminsdk-p3dyz-cc8f975108.json")

firebase_admin.initialize_app(cred)

db_client = firestore.client()

app = Flask(__name__)

@app.route('/' , methods = ['GET'])
def index():
    try:
        pot = db_client.collection('Project 252').document('potentiometer values').get().to_dict()

        val = pot['pot val']

        return render_template('index.html' , value = val)

    except Exception as e:
        print(e)
        return jsonify({'status' : 'failed'})

@app.route('/add' , methods = ['POST'])
def add():
    try:
        pot_val = request.json.get('potentiometer')

        db_client.collection('Project 252').document('potentiometer values').set({'pot val' : pot_val})

        return jsonify({'status' : 'success'})

    except Exception as e:
        print(e)
        return jsonify({'status' : 'failed'})


# running server
if __name__  ==  "__main__":
    app.run(host = '0.0.0.0' , debug = True)