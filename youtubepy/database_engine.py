"""

"""


import pymongo
import datetime
import urllib


def push_logs(url, count):
    """

    :param url:
    :param count:
    :return:
    """
    connection = pymongo.MongoClient("mongodb://idiot_ag:"+urllib.parse.quote("SteveJobs@123") + "@mycluster-shard-00"
                                     "-00-n5cdv.mongodb.net:27017,mycluster-shard-00-01-n5cdv.mongodb.net:27017,"
                                     "mycluster-shard-00-02-n5cdv.mongodb.net:27017/test?ssl=true&"
                                     "replicaSet=MyCluster-shard-0&authSource=admin&retryWrites=true")
    db = connection['Application_Logs']
    collection = db['YouTubePy']
    record = {"URL": url, "Count": count, "Date": datetime.datetime.now()}
    collection.insert_one(record)
    connection.close()
