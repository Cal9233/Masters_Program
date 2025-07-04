"""
Queue Module

This module provides a Queue implementation using two lists to achieve 
FIFO (First In, First Out) behavior.

Author: Calvin Malagon
Version: 1.0.0.0
Date: 7/4/25
"""

class Queue:
    """
    A Queue implementation using two lists for efficient FIFO operations.
    
    Purpose:
    Implements a queue data structure that uses two internal lists (a_in and a_out)
    to optimize enqueue and dequeue operations. Elements are added to a_in and
    transferred to a_out only when needed for dequeue operations.
    
    Methods:
    - __init__: Constructor for initializing empty queue
    - enqueue: Adds element to the back of the queue
    - dequeue: Removes and returns element from front of queue
    
    Attributes:
    a_in (list): Input list for storing newly enqueued elements
    a_out (list): Output list for storing elements ready to be dequeued
    """
    
    def __init__(self):
        """
        Initialize an empty queue with two internal lists.
        
        Function:
        Constructor that creates two empty lists for queue operations
        """
        self.a_in = []  # Range: 0 to unlimited elements, stores incoming data
        self.a_out = []  # Range: 0 to unlimited elements, stores outgoing data
    
    def enqueue(self, d):
        """
        Add an element to the back of the queue.
        
        Function:
        Adds element to input list
        
        Parameters:
        d (any): The element to add to the queue
        """
        self.a_in.append(d)
    
    def dequeue(self):
        """
        Remove and return the element from the front of the queue.
        
        Function:
        Removes and returns the oldest element
        
        Return:
        Returns first element from a_out
        """
        # Check if a_out is empty
        if (self.a_out == []):
            # Transfer all elements from a_in to a_out
            for d in self.a_in:
                self.a_out.append(d)
            # Clear a_in after transfer
            self.a_in = [] 
        
        # Remove and return first element from a_out
        return self.a_out.pop(0)