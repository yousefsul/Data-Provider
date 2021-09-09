import datetime

from bson import ObjectId
from pymongo import MongoClient

MONGO_CLIENT = "mongodb://yousef:Ys2021xch@209.151.150.58:63327/?authSource=admin&readPreference=primary&appname" \
               "=MongoDB%20Compass&ssl=false"


class ConnectMongoDB:
    """
    connect to devDB and client database
    define the clients_collection,visits_collection,claims_collection as none
    """

    def __init__(self):
        try:
            self.mongo_client = MongoClient(MONGO_CLIENT)
            self.db = self.mongo_client.client_2731928905_DB
            self.ack_collection = None
            self.dict_837_collection = None
        except ConnectionError:
            print(ConnectionError, "connection error have been occured")

    def connect_to_ack_collection(self):
        self.ack_collection = self.db.ack_coll

    def connect_to_837_collection(self):
        self.dict_837_collection = self.db['837_dict_coll']

    def get_unproccessed_files(self):
        return self.dict_837_collection.find(
            {"header_section.current_status.status": "matched"})

    def get_edi_files(self, param):
        return self.dict_837_collection.find_one({
            'header_section.trans_src_id': param
        })

    def get_ack_dict(self, param):
        return self.ack_collection.find_one({
            'header_section.trans_src_id': param
        })

    def update_st_status(self, segment, status, param):
        self.dict_837_collection.find_and_modify(
            query={"_id": param},
            update={"$set": {
                f'{segment}.status': status}
            },
            upsert=True
        )

    def update_file_status(self, param):
        self.dict_837_collection.find_and_modify(
            query={"_id": param},
            update={"$set": {
                "header_section.current_status.status": "accepted",
                "header_section.current_status.date": {
                    "date": datetime.datetime.now().date().strftime("%Y%m%d"),
                    "time": datetime.datetime.now().time().strftime("%H:%M:%S")
                }}
            },
            upsert=True
        )

    def update_file_status_history(self, param):
        self.dict_837_collection.update_one(
            {"_id": param},
            {"$push": {
                "header_section.status_history": {
                    "status": "accepted",
                    "date": {
                        "date": datetime.datetime.now().date().strftime("%Y%m%d"),
                        "time": datetime.datetime.now().time().strftime("%H:%M:%S")
                    }
                }
            }}
        )

    def get_database_name(self):
        return self.db._Database__name

    def get_277ca_dict(self):
        return self.ack_collection.find_one({
            'ST-3.01': '277'
        })
