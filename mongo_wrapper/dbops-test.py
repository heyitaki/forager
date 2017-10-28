''' 
Quick illustration of how to leverage dbops27. Output of this file is below:

$ python dbops-test.py
{u'category': u'innovate berkeley', u'term': u'fall', u'solution': u'Forage!', u'content': u'What is your name?', u'year': u'2017', u'_id': u'760541843', u'teacher': u'final'}
'''

from dbops27 import add, dump, clear

add('What is your name?', '2017', 'fall', 'innovate berkeley', 'final', 'Forage!')
dump()