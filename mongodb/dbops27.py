# Requires Python version 2.7

import hashlib
import json
import re
import sys
from bson.json_util import loads, dumps
from pymongo import MongoClient

DB_NAME = 'forage'
CONNECTION_STRING = 'mongodb://root:root@cluster0-shard-00-00-inppe.mongodb.net:27017,cluster0-shard-00-01-inppe.mongodb.net:27017,cluster0-shard-00-02-inppe.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'

def dump(collection_name):
  ''' For debugging purposes. Prints queue to console. '''
  for doc in connect(collection_name).find({}): print doc

def add_question(content, course, year, season, category, teacher, solution):
  ''' Add question entry to MongoDB questions collection. 
  
  @param content: Question content, encoded as a string
  @param year: Year of test or 'n/a' if unavailable, string
  @param season: Season/term ('summer', 'fall', 'winter', 'spring') or 'n/a' if unavailable, string
  @param category: Type of test ('midterm', 'final', 'practice') or 'n/a' if unavailable, string
  @param teacher: First/last name of teacher or 'n/a' if unavailable, string
  @param solution: Content of solution or 'n/a' if unavailable, string
  @return: Whether or not the operation was successful; what to do on failure is up to user, not this wrapper
  '''
  collection = connect('questions')
  bson_data = bsonify_question(content, course, year, season, category, teacher, solution)
  return collection.insert_one(bson_data).acknowledged

def add_tags(content, tag_lst):
  ''' Add one or more tags relating to a specific question, in the tags collection.
  Duplicates will be ignored. '''
  collection = connect('tags')
  question_id = hash1(content)
  print collection.find({'_id': question_id}).count()
  if collection.find({'_id': question_id}).count() > 0:
    prev_lst = collection.find({'_id': question_id})[0]['tags']
    tag_lst = prev_lst + list(set(tag_lst) - set(prev_lst))
    bson_data = bsonify_tags(question_id, tag_lst)
    return collection.replace_one({'_id': question_id}, bson_data).acknowledged
  bson_data = bsonify_tags(question_id, tag_lst)
  return collection.insert_one(bson_data).acknowledged

def add_rating(content, rating_type, rating_val):
  pass

def search(query):
  ''' Search the DB for a specific query and return all relevant results, in no specific order. 
  
  Currently, search works according to the following rules:
  1. Parse out specific operators (denoted by '-char' and followed by an argument)
  2. Take the remaining text and treat it as the content of the actual query
  3. Take each word from this content and compare it to the entries in the tags DB
  4. Take all of the matches from the tags DB, as well as all of the partial content matches from the 
  questions DB and return.
  '''
  op_value_map = parse(query)
  op_field_map = {'-c': 'course', '-y': 'year', '-s': 'season', '-t': 'category', '-n': 'teacher'}

  document = {}
  matches = set()
  collection = connect('tags')
  if 'content' in op_value_map:
    for word in op_value_map['content'].split():
      document['tags'] = {'$all': [word]}
      matches.update([q['_id'] for q in collection.find(document)])

  document = {}
  for op in op_value_map:
    if op in op_field_map:
      document[op_field_map[op]] = op_value_map[op]

  if 'content' in op_value_map:
    if len(matches) == 0:
      document['content'] = {'$regex': '.*%s.*' % op_value_map['content']}
    else:
      or_conditions = []
      for qid in matches:
        or_conditions.append({'_id': qid})
      or_conditions.append({'content': {'$regex': '.*%s.*' % op_value_map['content']}})
      document['$or'] = or_conditions

  return connect('questions').find(document)

def clear(collection_name, skip):
  ''' Deletes all entries and clears DB. '''
  if skip:
    connect(collection_name).drop()
    return

  valid = {'yes': True, 'y': True, 'no': False, 'n': False}
  sys.stdout.write("Are you sure you want to clear the entire DB? ")
  sys.stdout.flush()
  while True:
    choice = raw_input().lower()
    if choice not in valid:
      sys.stdout.write("Please select a valid option (y/n).")
    elif valid[choice]:
      connect(collection_name).drop()
      return
    else:
      return

##### HELPER METHODS #####
def connect(collection_name):
  ''' Connects to the Mongo DB and returns the specified collection (for now, 'questions' by default). '''
  client = MongoClient(CONNECTION_STRING)
  db = getattr(client, DB_NAME)
  collection = getattr(db, collection_name)
  return collection

def bsonify_question(content, course, year, season, category, teacher, solution):
  ''' Creates and returns BSON entry encoding relevant question info to add to MongoDB. '''
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

def bsonify_tags(question_id, tag_lst):
  ''' Creates and returns BSON entry encoding relevant tag info to add to MongoDB. '''
  data = {}
  data['_id'] = question_id
  data['tags'] = tag_lst
  return loads(json.dumps(data))

def hash1(data):
  return str(abs(hash(data)))

def parse(query):
  ''' Parse a given query according to the following operators and delimiters. Returns a mapping of each operator 
  to the corresponding value passed into the query.
  
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
  ''' Print methods and docstrings of a given object. Useful for looking into pymongo objects without much online documentation. '''
  methodList = [method for method in dir(object) if callable(getattr(object, method))]
  processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
  print "\n\n".join(["%s %s" % (method.ljust(spacing), processFunc(str(getattr(object, method).__doc__))) for method in methodList])