class Node:
    def __init__(self, value, next: 'Node' = None):
        self.value = value
        self.next_ = next if next != None else None

    def next(self):
        return self.next_

    def _get_chain(self):
        result = f"{self.value}"
        next_node = self.next_
        while next_node != None:
            result += f", {next_node.value}"
            next_node = next_node.next()
        return result

    def print_chain(self):
        print(self._get_chain())
    
    def __str__(self):
        return str(self.value)

class PrinterQueue:
    def __init__(self, element: Node = None):
        self.current = element if element != None else None
        self.queue = None

    def add_to_queue(self, element: Node = None):
        if self.current == None:
            self.current = element if element != None else None
            self.queue = None
        else:
            if self.queue == None:
                self.queue = element
                self.current.next_ = self.queue
            else: 
                self.queue.next_ = element
                self.queue = element

    def delete_from_queue(self):
        if self.current is None:
            return
        
        self.current = self.current.next_

        if self.current is None:
            self.queue = None

    def __str__(self):
        return self.current._get_chain()

    def print_document(self):
        result = self.current

        if self.current != None and self.current.next_ != None:
            self.current = self.current.next_
        else:
            self.current = None

        return result

node1 = Node(100)
node2 = Node(200)
node3 = Node(300)
node1.next_ = node2
node2.next_ = node3

node1.print_chain()
node2.print_chain()
print()

queue = PrinterQueue(node1)
queue.add_to_queue(node2)
queue.add_to_queue(node3)

print(queue)
print(queue.print_document())
print(queue.print_document())
print(queue.print_document())
print(queue.print_document())
print(queue.print_document())