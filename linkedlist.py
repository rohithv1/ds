"""
Class for creating LinkedList

@author: Rohith
"""

class LinkedList(object):
    """ This LinkedList is created using recurssions.
    It will be updated in the future for more generalised
    approach.
    """

    def __init__(self, head, next=None):
        self.head = head
        self.next = next

    def add_element(self, obj):
        if self.next:
            self.next.add_element(obj)
        else:
            self.next = LinkedList(obj)
    
    def print_elements(self):
        if self.next:
            print("{} ->".format(self.head), end=" ")
            self.next.print_elements()
        else:
            print("{}".format(self.head))
    
    def get_ll(self, output=[]):
        output.append(self.head)
        if self.next:
            self.next.get_ll(output)
        return output

if __name__ == '__main__':
    new_ll = LinkedList(5)
    new_ll.add_element(3)
    new_ll.add_element(7)
    new_ll.add_element(4)
    new_ll.print_elements()
    print(new_ll.get_ll())
