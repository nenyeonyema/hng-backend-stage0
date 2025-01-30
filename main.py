#Import the required library for the application
from flask import Flask, Response
from flask_cors import CORS
from datetime import datetime
import json


#Initializes Flask app and enables CORS middleware
app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def home():
    
    res = {
        "email":"chinenyeonyema1@gmail.com",
        "current_datetime":datetime.utcnow().isoformat() + "Z",
        "github_url":"https://github.com/nenyeonyema/hng-backend-stage0",
    }

    json_response = json.dumps(res, indent=4)
    return Response(json_response, mimetype='application/json')



if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
