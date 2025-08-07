"""Linked list implementation of queue
Time complexity : O(1) constant time"""


class Node:
    def __init__(self, k):
        self.key = k
        self.next = None


class Myqueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def size(self):
        return self.size

    def isempty(self):
        return self.size == 0

    def getfront(self):
        return self.front

    def getrear(self):
        return self.rear

    def enqueue(self, x):
        temp = Node(x)
        if self.rear is None:
            self.front = temp
        else:
            self.rear.next = temp
        # to point rear to the new added node
        self.rear = temp
        self.size = self.size + 1

    def deque(self):
        if self.front is None:
            return None
        else:
            # to return the removed key after deque operation
            res = self.front.key
            self.front = self.front.next
            # if queue have only one key then after removal of that set rear to none
            if self.front is None:
                self.rear = None
            self.size = self.size - 1
            return res
