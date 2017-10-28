# Compatible with Python version 2.7+

import hashlib
import json
import re
from bson.json_util import loads, dumps
from pymongo import MongoClient

DB_NAME = 'forage'
COLLECTION_NAME = 'questions'
CONNECTION_STRING = 'mongodb://root:root@cluster0-shard-00-00-inppe.mongodb.net:27017,cluster0-shard-00-01-inppe.mongodb.net:27017,cluster0-shard-00-02-inppe.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'

def dump():
  ''' For debugging purposes. Prints queue to console. '''
  for doc in connect().find({}): print doc

def add(content, course, year, season, category, teacher, solution):
  ''' Add question entry to MongoDB. 
  
  @param content: Question content, encoded as a string
  @param year: Year of test or 'n/a' if unavailable, string
  @param season: Season/term ('summer', 'fall', 'winter', 'spring') or 'n/a' if unavailable, string
  @param category: Type of test ('midterm', 'final', 'practice') or 'n/a' if unavailable, string
  @param teacher: First/last name of teacher or 'n/a' if unavailable, string
  @param solution: Content of solution or 'n/a' if unavailable, string
  @return: Whether or not the operation was successful; what to do on failure is up to user, not this wrapper
  '''
  collection = connect()
  bson_data = constructBson(content, course, year, season, category, teacher, solution)
  return collection.insert_one(bson_data).acknowledged

def search(query):
  print query
  op_value_map = parse(query)
  print op_value_map
  op_field_map = {'-c': 'course', '-y': 'year', '-s': 'season', '-t': 'category', '-n': 'teacher'}
  document = {}
  for op in op_value_map:
    if op in op_field_map:
      document[op_field_map[op]] = op_value_map[op]
  return connect().find(document)

def clear(certainty):
  ''' Deletes all entries and clears DB. '''
  if certainty:
    connect().drop()

##### HELPER METHODS #####
def constructBson(content, course, year, season, category, teacher, solution):
  ''' Creates and returns BSON entry to add to MongoDB. '''
  data = {}
  data['_id'] = hash1(content)
  data['content'] = content
  data['course'] = course
  data['year'] = year
  data['season'] = season
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

def parse(query):
  ''' Search for and return a specific question entry from the DB. 
  
  Search operators:
  -y year 
  -s season 
  -c course
  -t test type
  -n teacher name
  -a has answer (boolean)
  -d difficulty >= x
  -u usefulness >= x
  "" exact match content-wise
  '''
  query += ' '
  op_map = {}
  op_patterns = {'-y': '\d{4}', '-s': '\w+', '-c': '\w+', '-t': '\w+', '-n': '\w+', '-a': '', '-d': '\d\.\d', '-u': '\d\.\d'}
  for op in op_patterns: 
    tokens = re.split('(%s)[\s]+(%s)[\s]*' % (op, op_patterns[op]), query)
    if op in tokens:
      idx = tokens.index(op)
      op_map[op] = tokens[idx+1]
      query = ''.join(tokens[:idx] + tokens[idx+2:]) if idx+2 < len(tokens) else ''.join(tokens[:-2])
  op_map['content'] = re.sub(' +', ' ', query.strip())
  return op_map

##### DEBUGGING METHODS #####
def info(object, spacing=10, collapse=1): 
    ''' Print methods and docstrings of a given object. '''
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n\n".join(["%s %s" %
                      (method.ljust(spacing),
                       processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList])