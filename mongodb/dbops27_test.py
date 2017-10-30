from dbops27 import dump, clear, search
from bson.json_util import loads, dumps
from dbadd_cs186_sp_2016_mt1 import add_exam as add1
from dbadd_cs186_sp_2016_mt2 import add_exam as add2

def test():
  #query = "  hello world  -y   2017  -a -c  midterm1    recursion"
  #print search(query)
  query = "disk"
  result = search(query)
  print result

# add1()
# add2()
# dump('questions')
# dump('tags')
test()