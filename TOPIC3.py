class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.capacity = capacity

    def enqueue(self, data):
        if (self.rear + 1) % self.capacity == self.front:
            print("Queue is full")
            return False
        elif self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data
        return True

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return data

    def is_empty(self):
        return self.front == -1

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            return []
        if self.rear >= self.front:
            return self.queue[self.front : self.rear + 1]
        return self.queue[self.front :] + self.queue[: self.rear + 1]


if __name__ == "__main__":
    auction_queue = CircularQueue(5) 

    auction_queue.enqueue("jmv 1")
    auction_queue.enqueue("jmv 2")
    auction_queue.enqueue("jmv 3")

    print("Queue after enqueues:", auction_queue.display())

    print("Dequeued:", auction_queue.dequeue())
    print("Queue after dequeue:", auction_queue.display())

    auction_queue.enqueue("jmv 4")
    auction_queue.enqueue("jmv 5")
    auction_queue.enqueue("jmv 6")  

    print("Final queue state:", auction_queue.display())
