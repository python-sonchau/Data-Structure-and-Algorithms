class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        # if empty, we create a head node first
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else: 
            new_data = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_data
            new_data.next = self.head

    def print_list(self):
        cur = self.head

        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break
    
    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def remove(self, key):
        if self.head:
            if self.head.data == key:
                cur = self.head 
                while cur.next != self.head:
                    cur = cur.next 
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur.next = self.head.next
                    self.head = self.head.next
            else:
                cur = self.head 
                prev = None 
                while cur.next != self.head:
                    prev = cur 
                    cur = cur.next
                    if cur.data == key:
                        prev.next = cur.next 
                        cur = cur.next
    def __len__(self):
        cur = self.head
        count = 0
        while cur:  
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count     

    def remove_node(self, node):
        if self.head == node:
            cur = self.head 
            while cur.next != self.head:
                cur = cur.next
            if self.head == self.head.next:
                self.head = None
            else:
                cur.next = self.head.next 
                self.head = self.head.next
        else:
            cur = self.head 
            prev = None
            while cur.next != self.head:
                prev = cur 
                cur = cur.next 
                if cur == node:
                    prev.next = cur.next
                    cur = cur.next

# cllist = CircularLinkedList()
# cllist.append("A")
# cllist.append("B")
# cllist.append("C")
# cllist.append("D")

# cllist.remove("A")
# cllist.remove("C")
# cllist.print_list()