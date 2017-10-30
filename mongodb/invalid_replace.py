import fileinput
import sys
import re

filenames = ['dbadd_cs61b_sp_2015_final.py', 'dbadd_cs61b_sp_2015_mt2.py', 'dbadd-cs161-spring-2011-mt1.py', 'dbadd-cs161-spring-2016-mt1.py']

for filename in filenames:
  for line in fileinput.FileInput(filename,inplace=1):
      line = re.sub(r'[^\x00-\x7F]+',' ', line)
      print line,