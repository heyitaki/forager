import re
import tempfile

filename = 'cs61a_fa16_mt1.py'
temp = tempfile.NamedTemporaryFile(mode="r+")
with open(filename, 'r') as infile:
    sanitized_data = re.sub(r'[^\x00-\x7f]', r'', infile.read())
    temp.write(sanitized_data)

temp.seek(0)
with open(filename, 'w') as outfile:
	outfile.write(temp.read())

temp.close()