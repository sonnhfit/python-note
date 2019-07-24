import pymongo
import datetime

client = pymongo.MongoClient('localhost', 27017)
db = client.test

collection = db.my_TTL_collection

timestamp = datetime.datetime.now()
utc_timestamp = datetime.datetime.utcnow()

collection.ensure_index("date", expireAfterSeconds=10)

collection.insert({'_id': 'session',
                   "date": timestamp,
                   "session": "test session"})

collection.insert({'_id': 'utc_session',
                   "date": utc_timestamp,
                   "session": "test session"})

# NOTE:
# the utc_session will be deleted after around 10 seconds,
# the other depending on your timezone
