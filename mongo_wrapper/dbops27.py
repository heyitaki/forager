# Compatible with Python version 2.7+

import hashlib
import json
from bson.json_util import loads, dumps
from pymongo import MongoClient

DB_NAME = 'forage'
COLLECTION_NAME = 'questions'
CONNECTION_STRING = 'mongodb://root:root@cluster0-shard-00-00-inppe.mongodb.net:27017,cluster0-shard-00-01-inppe.mongodb.net:27017,cluster0-shard-00-02-inppe.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'

def dump():
  ''' For debugging purposes. Prints queue to console. '''
  for doc in connect().find({}): print doc

def add(content, year, term, category, teacher, solution):
  ''' Add question entry to MongoDB. 
  
  @param content: Question content, encoded as a string
  @param year: Year of test or 'n/a' if unavailable, string
  @param term: Season ('summer', 'fall', 'winter', 'spring') or 'n/a' if unavailable, string
  @param category: Type of test ('midterm', 'final', 'practice') or 'n/a' if unavailable, string
  @param teacher: First/last name of teacher or 'n/a' if unavailable, string
  @param solution: Content of solution, string
  @return: Whether or not the operation was successful; what to do on failure is up to user, not this wrapper
  '''
  collection = connect()
  bson_data = constructBson(content, year, term, category, teacher, solution)
  return collection.insert_one(bson_data).acknowledged

def clear(certainty):
  ''' Deletes all entries and clears DB. '''
  if certainty:
    connect().drop()

##### HELPER METHODS #####
def constructBson(content, year, term, category, teacher, solution):
  ''' Creates and returns BSON entry to add to MongoDB. '''
  data = {}
  data['_id'] = hash1(content)
  data['content'] = content
  data['year'] = year
  data['term'] = term
  data['category'] = category
  data['teacher'] = teacher
  data['solution'] = solution
  return loads(json.dumps(data))

def connect():
  ''' Connects to the Mongo DB and returns the specified collection (for now, 'questions' by default). '''
  client = MongoClient(CONNECTION_STRING)
  db = getattr(client, DB_NAME)
  collection = getattr(db, COLLECTION_NAME)
  return collection

def hash1(data):
  return str(abs(hash(data)))

##### DEBUGGING METHODS #####

def info(object, spacing=10, collapse=1): 
    ''' Print methods and doc strings of a given object. '''
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n\n".join(["%s %s" %
                      (method.ljust(spacing),
                       processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList])

def test():
  pass