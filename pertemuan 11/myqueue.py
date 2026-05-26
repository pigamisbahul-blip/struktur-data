# membuat queue dari linked list
# 1 buat kelas node
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
# membuat kelas myqueue
class myqueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
# membuat method enqueue
    def enqueue(self,data):
        new_node = node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        print(f"Enqueued: {data}")
# membuat method dequeue
    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
            return None
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        print(f"dequeue: {data}")
        return data
    def peek(self):
        if self.isEmpty():
            print("queue is empty")
            return None
        return self.head.data
    def isEmpty(self):
        return self.size == 0
    # method untuk mencetak queue
    def printQueue(self):
        if self.isEmpty():
            print("queue is empty")
            return
        current = self.head
        print("Queue: ", end="")
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

Antrian = myqueue()
Antrian.enqueue("Ahmad")
Antrian.enqueue("Budi") 
Antrian.enqueue("Cindy")
Antrian.printQueue()
print(Antrian.peek())