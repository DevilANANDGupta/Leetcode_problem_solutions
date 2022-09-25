'''Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language. 

 

Example 1:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4'''


class MyCircularQueue:
	def __init__(self, k: int):
		"""
		Initialize your data structure here. Set the size of the queue to be k.
		"""
		self.queue = []
		self.capacity = k

	def enQueue(self, value: int) -> bool:
		"""
		Insert an element into the circular queue. Return true if the operation is successful.
		"""
		if self.isFull():
			return False
		self.queue.append(value)
		# print(self.queue)
		return True
			
	def deQueue(self) -> bool:
		"""
		Delete an element from the circular queue. Return true if the operation is successful.
		"""
		if self.isEmpty():
			return False
		self.queue.pop(0)
		return True
			
	def Front(self) -> int:
		"""
		Get the front item from the queue.
		"""

		return -1 if self.isEmpty() else self.queue[0]
			
	def Rear(self) -> int:
		"""
		Get the last item from the queue.
		"""

		return -1 if self.isEmpty() else self.queue[-1]

	def isEmpty(self) -> bool:
		"""
		Checks whether the circular queue is empty or not.
		"""
		return len(self.queue) <= 0

	def isFull(self) -> bool:
		"""
		Checks whether the circular queue is full or not.
		"""
		return len(self.queue) == self.capacity

class MyCircularQueue:
	def __init__(self, k: int):
		"""
		Initialize your data structure here. Set the size of the queue to be k.
		"""
		self.queue = [ None ] * k
		self.size = 0
		self.capacity = k
		self.head, self.tail = 0, -1

	def enQueue(self, value: int) -> bool:
		"""
		Insert an element into the circular queue. Return true if the operation is successful.
		"""
		if self.isFull():
			return False

		self.tail = (self.tail + 1) % self.capacity
		self.queue[self.tail] = value
		self.size += 1
		return True
			
	def deQueue(self) -> bool:
		"""
		Delete an element from the circular queue. Return true if the operation is successful.
		"""
		if self.isEmpty():
			return False

		self.head = (self.head + 1) % self.capacity
		self.size -= 1
		return True
			
	def Front(self) -> int:
		"""
		Get the front item from the queue.
		"""

		return -1 if self.isEmpty() else self.queue[self.head]
			
	def Rear(self) -> int:
		"""
		Get the last item from the queue.
		"""

		return -1 if self.isEmpty() else self.queue[self.tail]

	def isEmpty(self) -> bool:
		"""
		Checks whether the circular queue is empty or not.
		"""
		return self.size <= 0

	def isFull(self) -> bool:
		"""
		Checks whether the circular queue is full or not.
		"""
		return self.size == self.capacity
			

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
