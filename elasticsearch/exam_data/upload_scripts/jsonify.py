import json

def jsonify_exam_data(filename, school, teacher, course, term, exam_type):
  data = {}
  data['school'] = school # UCB
  data['teacher'] = teacher # Paxson
  data['course'] = course # CS161
  data['term'] = term # SP16
  data['exam_type'] = exam_type # MT1

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
