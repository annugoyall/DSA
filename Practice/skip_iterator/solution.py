"""
Design a SkipIterator that supports a method skip(int val). 
When it is called the next element equals val in iterator sequence should be skipped. 
"""
from collections import defaultdict

class SkipIterator:
    def __init__(self, l) -> None:
        self.iterator = l
        self.elements_to_be_skipped = defaultdict ()
        self.num_elements_to_be_skipped = 0
        self.curr_index = 0

    def has_next(self):
        return self.curr_index + self.num_elements_to_be_skipped < len(self.iterator)
    
    def next(self):
        val = self.iterator[self.curr_index]
        while self.elements_to_be_skipped.get(val, 0) > 0:
            self.elements_to_be_skipped[val] -= 1
            self.num_elements_to_be_skipped -= 1
            self.curr_index += 1
            val = self.iterator[self.curr_index]
        self.curr_index += 1
        return val
    
    def skip(self, val):
        self.elements_to_be_skipped[val] = self.elements_to_be_skipped.get(val, 0) + 1
        self.num_elements_to_be_skipped += 1

itr = SkipIterator([2, 3, 5, 6, 5, 7, 5, -1, 5, 10])
print(itr.has_next())  # true
print(itr.next())  # returns 2
print(itr.skip(5))
print(itr.next()) #  returns 3
print(itr.next()) #  returns 6 because 5 should be skipped
print(itr.next()) #  returns 5
print(itr.skip(5)) #
print(itr.skip(5)) #
print(itr.next()) #  returns 7
print(itr.next()) #  returns -1
print(itr.next()) #  returns 10
print(itr.has_next()) #  false
print(itr.next()) #  error