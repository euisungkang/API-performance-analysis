from flask import Flask, jsonify
from flask_restful import Resource, Api
import json

# Open model.json data as default data to return
f = open('../../model.json')
data = json.load(f)

static_data = { "hello" : "world" }

# Initialize app
app = Flask(__name__)
api = Api(app)

# Native method to Flask
@app.route('/rest_flask_native', methods=['GET', 'POST'])
def flask_native():
    global data
    return data

# Flask-restful method
class returnData(Resource):
    global data

    def get(self):
        # print(data)
        return data
    
api.add_resource(returnData, '/rest_flask_restful')

# Run app
if __name__=='__main__':
    app.run()