"""
Node class for creating various Datastructures

@author: Rohith
"""

class Node(object):
    """
    Node class with curr and nexr values
    """

    def __init__(self, curr):
        """
        Args:
            curr: current value the node is handling
            next: next value
        """
        self.curr = curr
        self.next = None