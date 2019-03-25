from pymongo import MongoClient

client = MongoClient('localhost', 27017)
default_db = client.LISTDB
default_collection = default_db.items

class DataAccess(object):
    def __init__(self, db, collection):
        self.db = db
        self.collection = collection

    def insert(self, value):
        raise NotImplementedError

    def delete(self, value):
        raise NotImplementedError

    def find(self, value):
        raise NotImplementedError

class MongoDB(DataAccess):
    def __init__(self, database=default_db, collection=default_collection):
        super(MongoDB, self).__init__(database, collection)

    #value should be JSON object to store
    def insert(self, value):
        return self.collection.insert_one(value).inserted_id

    #value should be JSON with a MongoDB filter operator
    def get(self, value):
        return [item for item in self.collection.find(value)]

    #value should be JSON key,value pair specifing record to delete
    #delete the first record found satifing the condition
    def delete(self, value):
        return self.collection.delete_one(value)

    def get_all(self):
        print([item for item in self.collection.find({})])
        return [item for item in self.collection.find({})]


