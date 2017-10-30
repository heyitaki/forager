from dbops27 import add_question, add_tags, dump, clear

course = "cs161"
year = '2011'
term = 'spring'
category = 'midterm 1'
teacher = 'paxson'

def add_exam():
  content = "The Soda Hall elevator requires card key access to go to the 4th floor. The door connecting the west stairwell and the 4th floor opens without cardkey. What security principle is missing in this design? Write the best answer, and briefly explain. (i) Fail-safe defaults. (ii) Complete mediation. (iii) Separation of responsibilities. (iv) Least privilege. (v) Human factors matter."
  solution = "The best answer is (ii). Complete mediation refers to ensuring that all accesses to a protected resource go through the intended mechanism for access control."
  add_tags(content, ['security principles'])
  add_question(content, course, year, term, category, teacher, solution)

  content = "Agree or disagree, and briefly explain: It s better to use library calls with rich functionality, like system(), than those with more narrow functionality, like execve(), because then your code that uses the library is simpler, and so more likely to be correct."
  solution = "Disagree. A  feature-rich API  such as that provided by system() presents many possibilities for an attacker to exploit functionality provided by the API, even though that functionality is not needed by your code."
  add_tags(content, ['security principles'])
  add_question(content, course, year, term, category, teacher, solution)

  content = "Agree or disagree, and briefly explain: When sanitizing inputs to avoid injection attacks, it s better to use a white-list approach than a black-list approach."
  solution = "Agree. With black-listing, you have to identify all of the ways that an attacker might construct a problematic input. This is harder, and fails in an unsafe manner, compared to identifying only the sorts of inputs that you want to allow."
  add_tags(content, ['security principles'])
  add_question(content, course, year, term, category, teacher, solution)

  content = "Agree or disagree, and briefly explain: You can tell whether a web page your browser displays represents a phishing attack on mybank.com by checking whether the URL in the address bar starts with http://mybank.com."
  solution = " Disagree. Phishing attacks can be based on URLs that start with a legitimate-looking prefix, but the actual domain name in the URL continues further, leading to a different host. A simple example is http://mybank.com.badguy.com. A more complex example is the use of non-ASCII characters that look like  / , but in fact are not separators."
  add_tags(content, ['security principles'])
  add_question(content, course, year, term, category, teacher, solution)

  content = "Suppose you have both the source code and a binary corresponding to a 5,000,000-line C program. Explain a technique you could use to try to discover whether it has a memory-safety vulnerability."
  solution = "One technique you could use is fuzz testing, where you supply random inputs to the program to see if you can induce a crash. Another technique would be to search the source code for the use of unsafe functions such as gets(). Approaches such as inspecting each pointer/array access, or proving invariants, are less viable, given the large code size."
  add_tags(content, ['security principles'])
  add_question(content, course, year, term, category, teacher, solution)

  content = "List three problems with using CAPTCHAs."
  solution = "Problems include:   The  arms race  driven by increasingly powerful automated techniques for solving CAPTCHAs.   Related to this, usability issues as CAPTCHAs become hard for humans to solve.   Denial-of-service vulnerabilities for CAPTCHAs that require significant computation to generate.    Out-sourcing  attacks whereby attackers get humans to solve CAPTCHAs for them.   Accessibility issues, such as for blind users who are asked to solve visual CAPTCHAs.   The inability for CAPTCHAs to discriminate between malicious automated activity versus benign automated activity (such as legitimate web crawlers)."
  add_tags(content, ['security principles'])
  add_question(content, course, year, term, category, teacher, solution)

add_exam()