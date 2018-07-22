from flask import Flask, Response, jsonify 
from flask_restplus import Api, Resource, fields, reqparse 
from flask_cors import CORS, cross_origin
import os 
from sentimentanalysis import scrape_tweet as sc

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app) 
api = Api(app, version='1.0', title='API for sentiment analysis', validate=False) 
ns = api.namespace('api_server', 'Returns sentiments on string on twitter')

model_input = api.model('Enter the keyword and no of tweets:', {"Keyword": fields.String()})
port = int(os.getenv('PORT', 8080)) 

@ns.route('/sieve') 
class SIEVE(Resource): 
    @api.response(200, "Success", model_input)   
    @api.expect(model_input)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Keyword', type=int)
        args = parser.parse_args()
        inp = str(args["Keyword"]) 
        result = sc(inp)
        return jsonify({"Sentiments": result}) 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=port, debug=False)