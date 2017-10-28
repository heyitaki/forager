from dbops27 import dump, clear, search

def test():
  #query = "  hello world  -y   2017  -a -c  midterm1    recursion"
  #print search(query)
  query = "-t midterm1"
  result = search(query)
  for item in result:
    print item

test()