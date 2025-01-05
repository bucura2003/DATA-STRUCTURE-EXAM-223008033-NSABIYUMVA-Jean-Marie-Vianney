class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return True
            current = current.next
        return False

    def display(self):
        properties = []
        current = self.head
        while current:
            properties.append(current.data)
            current = current.next
        return properties

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        return self.queue[0] if not self.is_empty() else None

    def display(self):
        return self.queue

# Example usage
if __name__ == "__main__":
    # Manage properties with Doubly Linked List
    properties = DoublyLinkedList()
    properties.append({"id": 1, "name": "Luxury Villa", "price": 1200000})
    properties.append({"id": 2, "name": "Modern Apartment", "price": 800000})
    properties.append({"id": 3, "name": "Cozy Cottage", "price": 500000})

    print("Properties:", properties.display())

    properties.remove({"id": 2, "name": "Modern Apartment", "price": 800000})
    print("Properties after removal:", properties.display())

    # Manage auction participants with Queue
    participants = Queue()
    participants.enqueue("Bidder A")
    participants.enqueue("Bidder B")
    participants.enqueue("Bidder C")

    print("Participants queue:", participants.display())

    print("Dequeued participant:", participants.dequeue())
    print("Participants queue after dequeue:", participants.display())