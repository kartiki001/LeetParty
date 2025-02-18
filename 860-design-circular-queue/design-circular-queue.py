class MyCircularQueue(object):

    def __init__(self, k):
        self.queue = []
        self.size = k

    def enQueue(self, value):
        self.val = value
        if len(self.queue)<self.size:
            self.queue.append(self.val)
            return True
        return False        

    def deQueue(self):
        if self.queue == []:
            return False
        self.queue.pop(0)
        return True
        

    def Front(self):
        if self.queue == []:
            return -1
        return self.queue[0]
        

    def Rear(self):
        if self.queue == []:
            return -1
        return self.queue[-1]

    def isEmpty(self):
        if len(self.queue)==0:
            return True
        return False        

    def isFull(self):
        if len(self.queue)==self.size:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()