from dbops27 import add_question, dump, clear

course = "cs186"
year = '2016'
term = 'spring'
category = 'midterm2'
teacher = 'hellerstein'

def add_exam():
  content = "Schedules that are conflict serializable are also view serializable."
  solution = "True."
  add_question(content, course, year, term, category, teacher, solution)

  content = "Under two-phase locking, once a transaction releases a lock, it can no longer acquire any new locks."
  solution = "True."
  add_question(content, course, year, term, category, teacher, solution)

  content = "Schedules that are conflict serializable have to be produced by two-phase locking."
  solution = "False, note that the converse is true - two-phase locking guarantees conflict serializability."
  add_question(content, course, year, term, category, teacher, solution)

  content = "Schedules produced by two-phase locking are guaranteed to prevent cascading aborts."
  solution = "False, strict two-phase locking is needed to guarantee this."
  add_question(content, course, year, term, category, teacher, solution)

  content = "Strict two-phase locking is both necessary and sufficient to guarantee conflict serializability."
  solution = "False, sufficient but not necessary."
  add_question(content, course, year, term, category, teacher, solution)

  content = "Wound-wait and wait-die algorithms are pessimistic deadlock avoidance algorithms and can cause more transaction aborts than needed."
  solution = "True."
  add_question(content, course, year, term, category, teacher, solution)

  content = "Under multi-granularity locking, locks should be acquired and released from the top level to the bottom level."
  solution = "False, locks are acquired top down but release bottom up."
  add_question(content, course, year, term, category, teacher, solution)

  content = "Under multi-granularity locking, when a transaction T1 is holding an 'IX' lock on page A, it is possible for transaction T2 to hold an 'S' lock on record B of page A."
  solution = "True."
  add_question(content, course, year, term, category, teacher, solution)

  content = "When evaluating potential query plans, the set of left deep join plans are always guaranteed to contain the best plan."
  solution = "False, this is a heuristic that System R uses to shrink the search space."
  add_question(content, course, year, term, category, teacher, solution)

  content = "As a heuristic, the System R optimizer avoids cross-products if possible."
  solution = "True."
  add_question(content, course, year, term, category, teacher, solution)

  content = "Considering all join orders and join methods, there are O(n!) ways to join n tables."
  solution = "False. (Question was thrown out)"
  add_question(content, course, year, term, category, teacher, solution)

  content = "A plan can result in an interesting order if it involves a sort-merge join."
  solution = "True."
  add_question(content, course, year, term, category, teacher, solution)

  content = "The System R algorithm is greedy because for each pass, it only keeps the lowest cost plan for each combination of tables."
  solution = "False, it is not greedy because it keeps track of interesting orders."
  add_question(content, course, year, term, category, teacher, solution)

  content = "If the statistics needed to compute the result size of a table are missing, the System R optimizer aborts."
  solution = "False, it uses 1/10 as a reduction factor if it cannot be computed."
  add_question(content, course, year, term, category, teacher, solution)

  content = "When a transaction commits, any modified buffer pages must be written to durable storage."
  solution = "False, ARIES uses a NO FORCE policy."
  add_question(content, course, year, term, category, teacher, solution)

  content = "When aborting a transaction, it may be necessary to modify pages on disk."
  solution = "True, ARIES uses a STEAL policy."
  add_question(content, course, year, term, category, teacher, solution)

  content = "During recovery, the ARIES protocol may redo aborted transactions."
  solution = "True, this is a key feature of ARIES and essential for the correctness of the protocol."
  add_question(content, course, year, term, category, teacher, solution)

  content = "The pageLSN contains the LSN of the last operation to modify the page."
  solution = "True."
  add_question(content, course, year, term, category, teacher, solution)

  content = "The tail of the log is always flushed after every update operation."
  solution = "False, we only require that the tail of the log be flushed on commit, remember that flushedLSN keeps track of the log tail."
  add_question(content, course, year, term, category, teacher, solution)

  content = "A system that uses a FORCE, STEAL policy does not need to undo any operations after a crash."
  solution = "False, a system with a STEAL policy needs UNDO logging to ensure atomicity."
  add_question(content, course, year, term, category, teacher, solution)