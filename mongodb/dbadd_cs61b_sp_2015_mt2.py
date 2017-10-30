from dbops27 import add_question, add_tags, dump, clear

course = "cs61b"
year = '2015'
term = 'spring'
category = 'midterm2'
teacher = 'hug'

def add_exam():
  content = "True or false: if A and B are 2-3-4 trees with the same exact elements, they must be identical. If true, justify; if false, provide a counter-example."
  solution = "False: insert 1,2,3,4,5 and insert 2,3,4,5,1; these 2 sequences of inserts produce different trees."
  add_question(content, course, year, term, category, teacher, solution)

  content = "Write the minimum and maximum height of a BST with 15 nodes. (Height is the maximum number of links from the root to a leaf)"
  solution = "3, 14"
  add_tags(content, ['data structures', 'binary search tree'])
  add_question(content, course, year, term, category, teacher, solution)

  content = "The minimum and maximum height of a Quick Union object with 15 elements where isConnected(a, b) returns true for every pair of items. (Height is the maximum number of links from the root to a leaf)"
  solution = "1, 14"
  add_tags(content, ['data structures'])
  add_question(content, course, year, term, category, teacher, solution)

  content = "The minimum and maximum height of a Weighted Quick Union object with 15 elements where isConnected(a, b) returns true for every pair of items. (Height is the maximum number of links from the root to a leaf)"
  solution = "1, 3"
  add_tags(content, ['data structures'])
  add_question(content, course, year, term, category, teacher, solution)

  content = "The minimum and maximum height of a 2-3-4 Tree containing 15 items. Recall that a node in a 2-3-4 tree may have 1, 2, or 3 items inside. (Height is the maximum number of links from the root to a leaf)"
  solution = "1, 3"
  add_tags(content, ['data structures'])
  add_question(content, course, year, term, category, teacher, solution)

  content = "The minimum and maximum height of an LLRB set containing 15 items. (Height is the maximum number of links from the root to a leaf)"
  solution = "3, 5"
  add_tags(content, ['data structures'])
  add_question(content, course, year, term, category, teacher, solution)

  content = "The minimum and maximum height of a binary heap containing 15 items. (Height is the maximum number of links from the root to a leaf)"
  solution = "3, 3"
  add_tags(content, ['data structures'])
  add_question(content, course, year, term, category, teacher, solution)

  content = "The minimum and maximum number of items in a single bucket for a chaining hash table with 30 items and 15 buckets (i.e. with a load factor of 2)."
  solution = "0, 30"
  add_tags(content, ['data structures'])
  add_question(content, course, year, term, category, teacher, solution)

add_exam()