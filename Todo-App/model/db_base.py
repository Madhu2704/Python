import pymongo
import utils.utils as ut
from icecream import ic

DB_CONFIG = ic(ut.getConfigVariables().get('mongo', {}))


class DB_BASE:

    def __init__(self, collectionName):
        self.collection = collectionName
        self.dbClient = pymongo.MongoClient(
            f"mongodb://{DB_CONFIG.get('host')}:{DB_CONFIG.get('port')}/{DB_CONFIG.get('db')}")

    def fetchCompleteCollection(self):
        return list(self.dbClient[DB_CONFIG.get('db')][self.collection].find({}))

    def insertRecord(self, recordItem):
        try:
            self.dbClient[DB_CONFIG.get(
                'db')][self.collection].insert_one(recordItem)
            return {'insertStatus': True}
        except Exception as e:
            return {'insertStatus': False, 'errorMsg': e}
