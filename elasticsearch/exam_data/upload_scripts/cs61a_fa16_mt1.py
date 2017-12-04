from redundancy import ucb, denero, cs61a, fa16, mt1
import jsonify

jsonify.jsonify_exam_data('cs61a_fa16_mt1.json', 'UCB', 'Denero', 'CS61A', 'FA16', 'MT1', '%s %s %s %s %s' % (ucb, denero, cs61a, fa16, mt1))

jsonify.jsonify_question_data(
  'cs61a_fa16_mt1_q1.json',
  '1',
  'For each of the expressions in the table below, write the output displayed by the interactive Python interpreter when the expression in evaluated. The output may have many lines. If an error occurs, write "Error", but include all output displayed before the error. If a function is displayed, write "Function". The first two rows have been provided as examples. Recall: The interactive interpreter displays the value of a successfully evaluated expression, unless it is None. Assume that you have started python3 and executed the following statements:',
  'True 2 None 3 5 None None 3 fish 1 5 2',
  True,
  'exeggcute print what would error'
)

jsonify.jsonify_question_data(
  'cs61a_fa16_mt1_q2.json',
  '2',
  'Fill in the environment diagram that results from executing the code below until the entire program is finished, an error occurs, or all frames are filled. You may not need to use all of the spaces or frames. A complete answer will: • Add all missing names and parent annotations to all local frames. • Add all missing values created or referenced during execution. • Show the return value for each local frame.',
  'func λ',
  True,
  'goldeen state splash klay curry lambda return global f1 f2 f3 f4 parent return value while'
)

jsonify.jsonify_question_data(
  'cs61a_fa16_mt1_q3a.json',
  '3a',
  'Implement counter, which takes a non-negative single-digit integer d. It returns a function count that takes a non-negative integer n and returns the number of times that d appears as a digit in n. You may not use recursive calls or any features of Python not yet covered in the course.',
  'n , last = n // 10 , n % 10 if last == d : k += 1 return k return count',
  True,
  'countizard recursion def counter(d): """ Return a function of N that returns the number of times D appears in N. >>> counter (8)(8018) 2 >>> counter (0)(2016) 1 >>> counter (0)(0) 0 """ def count k = 0 while last = n % 10'
)

jsonify.jsonify_question_data(
  'cs61a_fa16_mt1_q3b.json',
  '3b',
  'Implement significant, which takes positive integers n and k. It returns the k most significant digits of n as an integer. These are the first k digits of n, starting from the left. If n has fewer than k digits, it returns n. You may not use round, int, str, or any functions from the math module. You may use pow, which raises its first argument to the power of its second: pow(9, 2) is 81 and pow(9, 0.5) is 3.0.',
  'n < pow (10 , k): return n return significant (n // 10 , k)',
  True,
  'countizard recursion def significant (n , k): """ Return the K most significant digits of N. >>> significant (12345 , 3) 123 >>> significant (12345 , 7) 12345 """ if return n return significant'
)

jsonify.jsonify_question_data(
  'cs61a_fa16_mt1_q4a.json',
  '4a',
  'Implement repeat_sum, which takes a one-argument function f, a value x, and a non-negative integer n. It returns the sum of n + 1 terms. Each term, indexed by k starting at 0, is the result of applying f to x repeatedly k times. You may assign to only one name in each of the three assignment statements. You may not use recursive calls or any features of Python not yet covered in the course.',
  'while k <= n : total = total + x x = f (x) k = k + 1',
  True,
  'caterepeat def repeat_sum (f , x , n ): """ Compute the following summation of N+1 terms , where the last term calls F N times : x + f(x) + f(f(x)) + f(f(f(x))) + ... + f(f (... f(x))) >>> repeat_sum ( lambda x: x*x, 3 , 0) # 3 3 >>> repeat_sum ( lambda x: x*x, 3 , 1) # 3 + 9 12 >>> repeat_sum ( lambda x: x+2 , 3 , 4) # 3 + 5 + 7 + 9 + 11 35 """ total , k = 0 , 0 while return total'
)

jsonify.jsonify_question_data(
  'cs61a_fa16_mt1_q4b.json',
  '4b',
  'Implement sum_squares, which takes a non-negative integer n and uses repeat_sum to return the sum of the squares of the first n positive integers. Assume repeat_sum is implemented correctly. You may use pow, which raises its first argument to the power of its second: pow(9, 2) is 81 and pow(9, 0.5) is 3.0.',
  'lambda x : pow ( round ( pow (x , 0.5) + 1) , 2)',
  True,
  'caterepeat def sum_squares (n): """ Return the sum of the first N perfect squares. >>> sum_squares (0) 0 >>> sum_squares (3) # 1**2 + 2**2 + 3**2 14 >>> sum_squares (5) # 1**2 + 2**2 + 3**2 + 4**2 + 5**2 55 """ f = return repeat_sum (f , 0 , n)'
)

jsonify.jsonify_question_data(
  'cs61a_fa16_mt1_q5a.json',
  '5a',
  'Implement multiadder, which takes a positive integer n and returns an order n numeric function that sums an argument sequence of length n.',
  'if n == 1: return lambda x : x else : return lambda a : lambda b : multiadder (n -1)(a + b)',
  True,
  'multikarp Terminology. An order 1 numeric function is a function that takes a number and returns a number. An order 2 numeric function is a function that takes a number and returns an order 1 numeric function. Likewise, an order n numeric function is a function that takes a number and returns an order n − 1 numeric function. The argument sequence of a nested call expression is the sequence of all arguments in all subexpressions, in the order they appear. For example, the expression f(3)(4)(5)(6)(7) has the argument sequence 3, 4, 5, 6, 7 def multiadder ( n ): """ Return a function that takes N arguments , one at a time , and adds them . >>> f = multiadder (3) >>> f (5)(6)(7) # 5 + 6 + 7 18 >>> multiadder (1)(5) 5 >>> multiadder (2)(5)(6) # 5 + 6 11 >>> multiadder (4)(5)(6)(7)(8) # 5 + 6 + 7 + 8 26 """ assert n > 0'
)

jsonify.jsonify_question_data(
  'cs61a_fa16_mt1_q5b.json',
  '5b',
  'Complete the expression below by writing one integer in each blank so that the whole expression evaluates to 2016. The compose1 function appears on your midterm 1 study guide in the middle of the left column of page 2. Assume multiadder is implemented correctly.',
  'compose1 ( multiadder (4)(1000) , multiadder (3)(10)(1000))(1)(2)(3)',
  True,
  'multikarp Terminology. An order 1 numeric function is a function that takes a number and returns a number. An order 2 numeric function is a function that takes a number and returns an order 1 numeric function. Likewise, an order n numeric function is a function that takes a number and returns an order n − 1 numeric function. The argument sequence of a nested call expression is the sequence of all arguments in all subexpressions, in the order they appear. For example, the expression f(3)(4)(5)(6)(7) has the argument sequence 3, 4, 5, 6, 7 compose1 ( multiadder ( )(1000) , multiadder ( )(10)( ))(1)(2)(3)'
)
