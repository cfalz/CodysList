import requests as requester
import json

class Requester(object):
    def __init__(self, request_client=requester, server_url='http://localhost:5000'):
        self.request_client = request_client
        self.server_url = server_url

    def get_items(self):
        try:
            return self.request_client.get(self.server_url + '/items').json()
        except Exception as e:
            print("Exception in get_items ", e)
            return None

    def get_item(self, item_id):
        try:
            return self.request_client.get(self.server_url + '/item?item_id=' + str(item_id)).json()
        except Exception as e:
            print("Exception in get_item", e)
            return None

    def post_item(self, payload, headers={'accept': 'application/json', 'Content-Type': 'application/json'}):
        try:
            print(self.server_url + '/item', headers, json.dumps(payload))
            return self.request_client.post(self.server_url + '/item', headers = headers, data=json.dumps(payload)).json()
        except Exception as e:
            print("Exception in post_item", e)
            return None

if __name__ == '__main__':
    controller = Requester()
    item_id = 14375
    data = { "item_id": item_id, "seller": 0, "name": "item " + str(item_id), "price": 0, "img": "string", "description": "string", "ingredients": [ "string" ], "lat": 0, "lng": 0}
    print("Attempting to create item with id ", data["item_id"], " in client controller")
    print(controller.post_item(data))
    print("Attempting to get item with id ", data["item_id"], " in client controller")
    print(controller.get_item(data["item_id"]))
