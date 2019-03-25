from flask import Flask
from flask_restplus import Resource, Api, reqparse, fields
from DataAccess.DataAccess import *
from ItemService.api_models import ApiModel

# Instantiate App
app = Flask(__name__)

# Setup Swagger with flask_restplus
api = Api(app, version='1.0', title='CodysList')

# Instantiate api models
apimodel = ApiModel(api)

# Instantiate Database (File)
Dao = MongoDB()

# Item Endpoints
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
        print(Dao.get(args))
        return Dao.get(args)

    @api.expect(apimodel.item_format())
    @api.response(200, 'Success', apimodel.item_format())
    @api.response(500, 'Failure', apimodel.item_failure_response())
    def post(self):
        try:
            Dao.insert(api.payload)
        except Exception as e:
            print("Failed POST to create and item with payload: ", api.payload, ", Threw exception :", e)

    @api.response(200, 'Success')
    @api.response(500, 'Failure')
    @api.doc(params={"item_id": "id of item to delete"})
    def delete(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('item_id', type=int)
            args = parser.parse_args()
            Dao.delete(args)
        except Exception as e:
            print("Failed Delete item with args ", args, ", Threw exception :", e)

@api.route('/items')
class Items(Resource):
    @api.response(200, 'Success', apimodel.item_list_response_format())
    @api.response(500, 'Failure', apimodel.item_failure_response())
    def get(self):
        return Dao.get_all()

if __name__ == '__main__':
    app.run(debug=True)
