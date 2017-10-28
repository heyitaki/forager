from dbops27 import dump, clear, search
from bson.json_util import loads, dumps

def test():
  #query = "  hello world  -y   2017  -a -c  midterm1    recursion"
  #print search(query)
  query = "-t midterm1 hash"
  result = search(query)
  for item in result:
    print dumps(item)

test()