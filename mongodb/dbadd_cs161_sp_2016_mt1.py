from dbops27 import add_question, add_tags, dump, clear

course = "cs161"
year = '2016'
term = 'spring'
category = 'midterm 1'
teacher = 'wagner'

def add_exam():
  content = "True or False: A problem with iframes is that if a user visits an attacker s website, that website could load a bank website inside <iframe> tags and read sensitive data from this website."
  solution = "False, the same origin policy prevents this."
  add_tags(content, ['security principles'])
  add_question(content, course, year, term, category, teacher, solution)

  content = "True or False: A site that implements and requires a hidden validation token in a form value for requests, in addition to authentication cookies, but is vulnerable to XSS attacks, is safe from CSRF attacks."
  solution = "False, You can use a XSS attack to learn the CSRF token and then mount a CSRF attack."
  add_tags(content, ['security principles'])
  add_question(content, course, year, term, category, teacher, solution)

  content = "When you pay for something online using PayPal, the PayPal checkout form that shows the price and asks for your PayPal login always appears on its own page, never embedded in an iframe on the seller s checkout page. What threat is this defending against? Circle the best answer. XSS, Integer overflow, CSRF, SQL injection, Clickjacking, Same-origin policy, Buffer overruns, Drive-by malware, None of the above"
  solution = "Clickjacking"
  add_tags(content, ['security principles'])
  add_question(content, course, year, term, category, teacher, solution)

  content = "NinjaCourses.com is written in Python. Sheryl decides to rewrite it in C, ensuring her re-implementation behaves the same. Assuming Sheryl tries to make her C implementation have the same functionality as the Python implementation, what new security threats might Sheryl s C code face that aren t equally applicable to the original Python code? Circle all that apply. XSS, CSRF, Clickjacking, Buffer overruns, Phishing, SQL injection, Separation of responsibility, Two-factor authentication, None of the above"
  solution = "Buffer overruns"
  add_tags(content, ['security principles'])
  add_question(content, course, year, term, category, teacher, solution)

  content = "After finishing her C code, Sheryl does CS 161 s project 1 and learns for the first time about the ret2esp technique. Which of the following provides a complete defense against ret2esp attacks? Circle all that apply. Non-executable Stack, Referer validation, Content Security Policy (CSP), Same-origin policy, Memory-safe programming languages, Least privilege, Prepared statements, Two-factor authentication, None of the above"
  solution = "Non-executable Stack, Memory-safe programming languages"
  add_tags(content, ['security principles'])
  add_question(content, course, year, term, category, teacher, solution)

add_exam()