from flask import Flask
from flask_restplus import Resource, Api, reqparse, fields
from Server.DataAccessObject import *
from Server.api_models import ApiModel

# Instantiate App
app = Flask(__name__)

# Setup Swagger with flask_restplus
api = Api(app, version='1.0', title='CodysList')

# Instantiate api models
apimodel = ApiModel(api)

# Instantiate Database (File)
access = File()
Dao = Dao(access)

# Item Endpoint
@api.route('/item')
class Items(Resource):
    @api.response(200, 'Success', apimodel.item_format())
    @api.response(500, 'Failure', apimodel.item_failure_response())
    @api.doc(params={"item_id": "the id of the item you need"})
    @api.marshal_with(apimodel.item_format())
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('item_id', type=int)
        args = parser.parse_args()
        print(args)
        return Dao.get_item(args)

    @api.expect(apimodel.item_format())
    @api.response(200, 'Success', apimodel.item_format())
    @api.response(500, 'Failure', apimodel.item_failure_response())
    def post(self):
        try:
            Dao.create_item(api.payload)
            item = {'item_id' : api.payload["item_id"]}
            return Dao.get_item(item)
        except Exception as e:
            print("Failed POST to create and item with payload: ", api.payload, ", Threw exception :", e)

if __name__ == '__main__':
    app.run(debug=True)
