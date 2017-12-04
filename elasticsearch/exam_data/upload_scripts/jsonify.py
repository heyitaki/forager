import json

def jsonify_exam_data(filename, src_link, school, teacher, course, term, exam_type, redundancy):
  data = {}
  data['src_link'] = src_link
  data['school'] = school # UCB
  data['teacher'] = teacher # Paxson
  data['course'] = course # CS161
  data['term'] = term # SP16
  data['exam_type'] = exam_type # MT1
  data['redundancy'] = redundancy # all extra info

  with open('../info_exam/%s' % filename, 'w') as out:
    json.dump(data, out)

def jsonify_question_data(filename, number, q_txt, s_txt, has_solution, extra):
  data = {}
  data['number'] = number
  data['q_txt'] = q_txt
  data['s_txt'] = s_txt
  data['has_solution'] = has_solution
  data['extra'] = extra
  
  with open('../info_question/%s' % filename, 'w') as out:
    json.dump(data, out)