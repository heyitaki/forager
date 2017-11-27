import json
import os

def jsonify_exam_data(filename, school, teacher, course, term, year, exam_type):
	data = {}
  data['school'] = school
  data['teacher'] = teacher
  data['course'] = course
  data['term'] = term
  data['year'] = year
  data['exam_type'] = exam_type

  with open(filename, 'w') as out:
    json.dump(data, out)

def jsonify_question_data(filename, number, q_txt, s_txt, has_solution, tags):
  data = {}
  data['number'] = number
  data['q_txt'] = q_txt
  data['s_txt'] = s_txt
  data['has_solution'] = has_solution
  data['tags'] = tags
  
  with open(filename, 'w') as out:
    json.dump(data, out)

def jsonify_search(q_img_path):
  q_info_path = './question_data/' + replace_last(q_img_path, 'PNG', 'json')
  s_img_path = './solutions/' + replace_last(q_img_path, 'q', 's')
  exam_info_path = './exam_data/' + q_img_path[:-7] + '.json'
  q_img_path = './questions/' + q_img_path

  data = {}

  with open(q_info_path) as q_info_file:
    data.update(json.load(q_info_file))

  with open(exam_info_path) as exam_info_file:
    data.update(json.load(exam_info_file))

  with open(q_img_path) as q_img_file:
    q_img_data = q_img_file.read()
    data['q_img'] = q_img_data.encode('base64')

  with open(s_img_path) as s_img_file:
    s_img_data = s_img_file.read()
    data['s_img'] = s_img_data.encode('base64')

  print data
  return json.dumps(data)

def replace_last(src_str, replace_what, replace_with):
  head, _sep, tail = src_str.rpartition(replace_what)
  return head + replace_with + tail

def upload_to_elastic():
  for filename in os.listdir('./questions'):
    jsonify_search(filename)

upload_to_elastic()