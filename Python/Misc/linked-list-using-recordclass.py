# 2023-08

"""
A linked list is a linear data structure where each element
is the data and reference to next element. The last element
reference to None and an empty linked list has a None head.
"""

from recordclass import recordclass

# recordclass is a mutable namedtuple
Element = recordclass("Element", ["value", "next"])

class LinkedList:
    # linked list constructor
    def __init__(self): self.head = None
    # string representation of linked list
    def __str__(self):
        if self.head is None: return "[]"
        current = self.head
        values = []
        while current is not None:
            values.append(current.value)
            current = current.next
        return str(values)
    # insert element at tail
    def insert(self, value):
        # insert at head
        if self.head is None: self.head = Element(value, None)
        else:
            current = self.head
            # iterate until last element
            while current.next is not None: current = current.next
            # insert element
            current.next = Element(value, None)
    # remove element
    def remove(self, value):
        # remove head
        if self.head.value == value: self.head = self.head.next
        else:
            current = self.head
            # iterate until last element
            while current.next is not None:
                # remove element if found
                if current.next.value == value:
                    current.next = current.next.next
                    return
                current = current.next

ll = LinkedList()
ll.insert(5)
ll.insert(10)
ll.insert(15)
ll.insert(20)
ll.insert(25)
ll.insert(30)

print(ll)
# [5, 10, 15, 20, 25, 30]

ll.remove(15)
ll.remove(30)

print(ll)
# [5, 10, 20, 25]
