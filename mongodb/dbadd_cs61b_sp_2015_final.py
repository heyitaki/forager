from dbops27 import add_question, add_tags, dump, clear

course = "cs61b"
year = '2015'
term = 'spring'
category = 'final'
teacher = 'hug'

def add_exam():
    content = "Suppose we have the array [4, 1, 6, 2, 3, 7, 3, 4]. Give a valid partitioning of this array using the leftmost item as a pivot. Any partitioning scheme is fine."
    solution = "[1, 2, 3, 3, 4, 4, 6, 7]. We are partitioning based on the number 4. We put all of the numbers smaller than 4 to the left of the partitioned array and numbers greaters than 4 to the right."
    add_question(content, course, year, term, category, teacher, solution)

    content = "Give the array that results if we transform the array [1, 2, 4, 9, 3, 7, 5] into a max heap. Use the sinking based heapify process that we described in class (possibly helpful reminder: this process also happens to be the first step of heap sort)."
    solution = "[9, 3, 7, 2, 1, 4, 5]. Heapify is taking all of the nodes in the heap and from the bottom up, sinking those nodes to its correct position. Note that this is not the same as taking the elements of the array and adding them into an empty heap one by one."
    add_tags(content, ['data structures'])
    add_question(content, course, year, term, category, teacher, solution)

    content = "Find an input that results in worst case runtime for insertion sort. Give your answer as an array of 5 integers."
    solution = "[5, 4, 3, 2, 1]. Recall that insertion sort maintains two sections of the array: a sorted portion and an unsorted portion. The first element of the unsorted portion is swapped into place in the sorted portion by comparing its value with its left neighbor and swapping until the element we are sorting is larger than its left neighbor. Thus, to maximize the number of swaps, we want any array which is in purely descending order, because each element will have to be swapped to the very front."
    add_question(content, course, year, term, category, teacher, solution)

    content = "Given an initially empty BST, give an insertion order for A, B, C, D, E, F, G that minimizes height. Assume we are not performing any balancing operations."
    solution = "D, B, F, A, C, E, G. Recall a similar question from discussion: the ideal tree is constructed by recursively inserting the median of each subtree. There were many different possible correct insertion orders such as DBACFEG. The important thing was to represent the tree as a directed graph where each parent node has a directed edge to its children. Any valid topological sort order of this DAG (directed acyclic graph) would be a valid insertion order."
    add_question(content, course, year, term, category, teacher, solution)

    content = "What is the size of the largest binary min heap that is also a valid BST? Draw an example assuming all keys are letters from the English alphabet. Assume the heap has no duplicate elements."
    solution = "Recall that a heap must satisfy two properties: (1) Heap-Order Property: In a min-heap, this means that each node is smaller than each of its children. (2) Completeness: there are no  holes  in the heap as you go through the tree in a level-order traversal. Recall that a binary search tree (BST) satisfies the binary search invariant: all elements in the left subtree are less than the key in the root, and all elements in the right subtree are greater than the key in the root. Combining these facts, we know that we can only have elements in the right subtree, but this violates the completeness requirement for a heap. Thus, the maximum size is 1."
    add_question(content, course, year, term, category, teacher, solution)

    content = "Give an example of when you'd use Quicksort over Mergesort."
    solution = "There are many situations where we might use Quicksort: When we want faster overall runtime, better memory usage, when we don't care about stability, when we have many duplicates (can use 3-way quick sort (from textbook))."
    add_question(content, course, year, term, category, teacher, solution)

    content = "Give an example of when you d use a Trie-based map instead of a HashMap."
    solution = "Likewise, there are many cases where we might prefer a Trie: When we want to look for near misses (e.g. spell checking), for autocomplete or other string prefix operations, when we expect to have mismatches early on in a string, to save space for certain pathological inputs with large degrees of overlap at the front of the string, when we want to support ordered operations, to implement alphabet sort from proj3 (not a great answer since a map isn t the right abstraction, but technically correct)."
    add_question(content, course, year, term, category, teacher, solution)

    content = "In LSD radix sorting, we sort our inputs digit by digit, starting from the least significant digit and working our way leftwards. For each digit, we used counting sort. Conceptually, we can imagine that we used a subroutine countSort(Something[] a, int k), which sorts the array a of something based on the kth digit of each object in a. Suppose that we replaced counting sort with a special version of insertion sort insertionSort(Something[] a, int k) that insertion sorts based on only the kth digit of each Something. Would LSD radix sort still work? What would be the worst-case runtime in terms of N and W, where N is the number of keys and W is the width of the keys in digits? Justification is optional but may be considered for partial credit."
    solution = "Correct: yes, Insertion Sort is stable. Runtime, big O: O(W(N^2))."
    add_question(content, course, year, term, category, teacher, solution)

    content = "In LSD radix sorting, we sort our inputs digit by digit, starting from the least significant digit and working our way leftwards. For each digit, we used counting sort. Conceptually, we can imagine that we used a subroutine countSort(Something[] a, int k), which sorts the array a of something based on the kth digit of each object in a. Suppose that we replaced counting sort with a special version of heap sort heapSort(Something[] a, int k) to sort on each digit. Would this version of LSD radix sort yield the correct result? What would be the worst case runtime in terms of N and W? Justification is optional but may be considered for partial credit."
    solution = "Correct: no, Heap Sort is not stable. Runtime, big O: O(WN logN)."
    add_question(content, course, year, term, category, teacher, solution)

add_exam()