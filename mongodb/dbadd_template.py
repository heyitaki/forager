''' 
Quick illustration of how to leverage dbops27. Output of this file is below:

$ python dbops-test.py
{u'category': u'innovate berkeley', u'term': u'fall', u'solution': u'Forage!', u'content': u'What is your name?', u'year': u'2017', u'_id': u'760541843', u'teacher': u'final'}
'''

from dbops27 import add_question, dump, clear

# format: add(content, course, year, season, category, teacher, solution)
add_question('What is your name?', 'cs61a', '2017', 'fall', 'final', 'denero', 'Forage!')
dump()