import re, tempfile

files = ['cs61a_fa14_mt1.py', 'cs61a_fa14_mt2.py', 'cs61a_fa14_final.py', 'cs61a_fa15_mt1.py', 'cs61a_fa15_mt2.py', 'cs61a_fa15_final.py', 'cs61a_fa16_mt1.py', 'cs61a_fa16_mt2.py', 'cs61a_fa16_final.py', 'cs61a_sp15_mt1.py', 'cs61a_sp15_mt2.py', 'cs61a_sp15_final.py', 'cs61b_sp17_mt1.py']
for filename in files:
  temp = tempfile.NamedTemporaryFile(mode="r+")
  with open(filename, 'r') as infile:
      sanitized_data = re.sub(r'[^\x00-\x7f]', r'', infile.read())
      temp.write(sanitized_data)

  temp.seek(0)
  with open(filename, 'w') as outfile:
  	outfile.write(temp.read())

  temp.close()