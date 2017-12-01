import jsonify

jsonify.jsonify_exam_data('cs61a_fa16_mt1.json', 'UCB', 'Denero', 'CS61A', 'FA16', 'MT1')
jsonify.jsonify_question_data(
  'cs61a_fa16_mt1_q1.json',
  1,
  'For each of the expressions in the table below, write the output displayed by the interactive Python interpreter when the expression in evaluated. The output may have many lines. If an error occers, write "Error", but include all output displayed before the error. If a function is displayed, write "Function". The first two rows have been provided as examples. Recall: The interactive interpreter displays the value of a successfully evaluated expression, unless it is None. Assume that you have started python3 and executed the following statements:',
  'True 2 None 3 5 None None 3 fish 1 5 2',
  True,
  ['python', 'output', 'exeggcute']
)