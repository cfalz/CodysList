from __future__ import print_function
import json
import sys

default_picture='../static/Images/picture-not-available.jpg'

class Serializer(object):

    def _data_to_obj(self,obj, data):
        for k in self._get_matching_keys(obj.__dict__, data):
            obj.__dict__[k] = data[k]

    def _get_matching_keys(self,dic1,dic2):
        return set(dic1.keys()).intersection(dic2.keys())

    def _print_all_attrs(self,obj):
        print(obj.__dict__)


class Item(Serializer):

    def __init__(self,Accessor,item_id=None,description=None,ingredients=[],price="$10.59",name=None,seller=None,state=None,city=None,lat=None,lng=None,img=default_picture, contact= "(123) 456-7891"):
        self.item_id = item_id
        self.description = description
        self.ingredients = ingredients
        self.price = price
        self.name = name
        self.seller = seller
        self.state = state
        self.city = city
        self.lat = lat
        self.lng = lng
        self.img = img
        self.contact = contact
        self.accessor = Accessor

    def store(self):
        return self.accessor.write(self)

    def create_item(self, data):
        self._data_to_obj(self,data)
        if len(self.accessor.read(self, item_id=self.item_id)) != 0:
            return {"Failure":"Itemid is not unique"}, 500
        return self.accessor.write(self)

    def get_items_from_seller(self,data):
        self._data_to_obj(self,data)
        return self.accessor.read(self,seller=data.get("id"))

    def get_item(self,data):
        self._data_to_obj(self,data)
        return self.accessor.read(self,item_id=self.item_id)

    def get_items(self):
        return self.accessor.read(self)

    def __str__(self):
        return "Item"


class Dao(object):
    def __init__(self,Accessor):
        self.dao = [Item]
        self.accessor = Accessor.connect()

    def __getattr__(self, method):
        try:
            for obj in self.dao:
                if hasattr(obj,method) and callable(getattr(obj,method)):
                    return getattr(obj(self.accessor),method)
        except AttributeError:
            print("AttributeError: method {} doesn't exit".format(method))

class Accessor(object):
    def __init__(self,type):
        self._type = type

    def connect(self,type=None):
        if type is not None:
            self._type = type
        if isinstance(self._type, File):
            return File()
        if isinstance(self._type, Database):
            return Database()

    def read(self, obj, **constraint):
        raise NotImplementedError

    def write(self, obj):
        raise NotImplementedError

class File(Accessor):

    def __init__(self):
        import os.path as path
        import sys
        self.dir = path.abspath(path.join(__file__,"../../.."))+"/database/"
        self._type = self

    def read(self, obj, **constraint):
        data = None
        results = []
        try:
            print("Dir: ", self.dir)
            print("Obj: ", str(obj))
            print("Full: ", self.dir + str(obj).lower()+'.json')
            with open(self.dir + str(obj).lower()+'.json','r') as f:
                data = json.load(f)
        except:
            print("Could not open file {} for reading".format(str(obj).lower()+'.json'))
            sys.exit()

        if constraint:
            for line in data:
                if self._is_meeting_constraint(line, constraint):
                    results.append(line)
        else:
            results = data

        return results

    def write(self, obj):
        existing_data = []
        #try:
        with open(self.dir + str(obj).lower() +'.json', 'r') as f:
            existing_data = json.load(f)

        existing_data.append(self._remove_accessor(obj.__dict__))
        # print("Existing Data After Appending", existing_data)
        #except ValueError:
        # print("[!] File.write() ERROR: Could not open {} for reading ".format(file.lower()+".json"))
        # print("Error in File write while reading")
        # return {"Failure":"{} not written, Error in read".format(str(obj))}, 500
        # try:
        with open(self.dir +str(obj).lower() +'.json', 'w') as f:
            json.dump(existing_data,f, indent=2)
        # except ValueError:
        # print("[!] File.write() ERROR: Could not open {} for writing\n".format(file.lower()+".json"))
        # print("Error in File write while writing")
        # return {"Failure":"{} not written, Error in write".format(str(obj))}, 500

        # return {"Success":"{} was successfully written".format(str(obj))}, 200

    def _get_matching_keys(self,dic1,dic2):
        return set(dic1.keys()).intersection(dic2.keys())

    def _is_meeting_constraint(self,line, constraint):
        for k in self._get_matching_keys(line, constraint):
            if line[k] != constraint[k]:
                return False
        return True

    def _remove_accessor(self,obj):
        temp = {}
        for k, v in obj.items():
            if k.lower() != "accessor":
                temp[k] = v
        return temp

class Database(Accessor):
    def __init__(self):
        self._type = self

    def read(self, obj, **constraint):
        pass

    def write(self, obj):
        pass


if __name__ == "__main__":
    item2 = {"item_id": 777, "description": "added via new Dao interface!", "ingredients": ["cool 1"], "price": 99.99, "seller": 100, "name": "New Dao created item"}

    access = File()
    dao = Dao(access)
    print(dao.create_item(item2))
    print(dao.get_item({"item_id":222}))
    print(dao.get_items())

