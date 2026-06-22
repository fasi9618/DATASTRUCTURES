class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None  
        
    def del_end(self):
        if self.head is None:
            return

        # If only one node, remove head
        if self.head.next is None:
            self.head = None
            return

        # Find second-to-last node
        itr = self.head
        while itr.next and itr.next.next:
            itr = itr.next

        # Unlink last node
        itr.next = None

    def add_end(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = new
    def add_beg(self,data):
        obj = Node(data)
        if self.head is None:
            self.head = obj
            return
        obj.next = self.head
        self.head = obj
    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        while itr:
            print(itr.data, end=" -> ")
            itr = itr.next

        print("None")


ll = LinkedList()

ll.add_end(10)
ll.add_end(20)
ll.add_end(30)
ll.add_beg(40)
ll.del_end()
ll.display()