''' 
Quick illustration of how to leverage dbops27. Output of this file is below:
$ python dbops-test.py
{
u'content': u'What is your name?', 
u'year': u'2017', 
u'term': u'fall', 
u'category': u'final', 
u'teacher': u'Joe'
u'solution': u'Forage!', 
u'_id': u'760541843', 
}
'''

from dbops27 import add, dump, clear
course = "CS186"
year = '2016'
term = 'Spring'
category = 'Midterm 1'
teacher = 'Joseph Hellerstein'

content = "When querying for a 16 bit record, exactly 16 bytes of data is read from disk."
solution = "False, a page's worth of data is always read from disk."
add(content, course, year, term, category, teacher, solution)

content = "Writing to an SSD drive is more costly than reading from an SSD drive."
solution = "True, writes to an SSD can involve reorganization to avoid uneven wear and tear."
add(content, course, year, term, category, teacher, solution)

content = "In a heap file, all pages must be filled to capacity except the last page."
solution = "False, there is no such requirement"
add(content, course, year, term, category, teacher, solution)

content = "If the file size is smaller than the number of buffer frames, a sequential scan of the file using either MRU or LRU (starting with an empty buffer pool) will have the same hit rate."
solution = "True, our eviction policy doesn't matter because the file fits in memory"
add(content, course, year, term, category, teacher, solution)

content = "Assuming integers take 4 bytes and pointers take 4 bytes, a slot directory that is 256 bytes can address 64 records in a page."
solution = "False, an entry in slot directory is 8 bytes because a single entry consists of both a pointer and an integer (length)."
add(content, course, year, term, category, teacher, solution)

content = "In a page containing fixed-length records with no nullable fields, the size of the bitmap never changes."
solution = "True, the size of the records is fixed, so the number we can fit on a page is fixed."
add(content, course, year, term, category, teacher, solution)

content = "Using a record header for variable length records does not need delimeter characters to separate fields in the records."
solution = "True."
add(content, course, year, term, category, teacher, solution)

content = "Using a record header for variable length records always matches or beats space cost when compared to fixed-length record format."
solution = "False."
add(content, course, year, term, category, teacher, solution)

content = "Using a record header for variable length records can access any field without scanning the entire record."
solution = "True."
add(content, course, year, term, category, teacher, solution)

content = "Using a record header for variable length records has compact representation of null values."
solution = "True."
add(content, course, year, term, category, teacher, solution)

content = "With 4 buffer frames and MRU replacement policy, list the four pages in the buffer pool after the following access pattern in which pages are immediately unpinned: TAMETEAMMATEMEATLID."
solution = "ADEM."
add(content, course, year, term, category, teacher, solution)

content = "With 4 buffer frames and LRU replacement policy, list the four pages in the buffer pool after the following access pattern in which pages are immediately unpinned: TAMETEAMMATEMEATLID."
solution = "DILT."
add(content, course, year, term, category, teacher, solution)

content = "With 4 buffer frames and clock replacement policy, list the four pages in the buffer pool after the following access pattern in which pages are immediately unpinned: TAMETEAMMATEMEATLID."
solution = "DILT."
add(content, course, year, term, category, teacher, solution)

content = "Sometimes, adding more memory to our system will not reduce I/O costs for a sort-merge join."
solution = "True, a simple counter example is joining two 1-tuple relations."
add(content, course, year, term, category, teacher, solution)

content = "A Grace hash join will always perform better than a naive hash join."
solution = "False, a simple counter example is joining two 1-tuple relations."
add(content, course, year, term, category, teacher, solution)

content = "Sometimes, replacing an Alternative 2 index with an Alternative 1 index on the same key will speed up an index-nested-loops join."
solution = "True, Alternative 1 lookups don't require the additional IO's to follow the record id to the data pages, which is necessary with an Alternative 2 index."
add(content, course, year, term, category, teacher, solution)

content = "A Grace hash join can often complete in 2 passes if the size of the smaller relation is less than roughly the square of the number of buffers available for the join."
solution = "True, if we assume a hash function which spreads evenly."
add(content, course, year, term, category, teacher, solution)

dump()