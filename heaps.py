# Python3 implementation of Max Heap
import sys

class MaxHeap:

	def __init__(self, maxsize):
		
		self.maxsize = maxsize
		self.size = 0
		self.Heap = [[]] * (self.maxsize + 1)
		self.Heap[0] = [None, sys.maxsize]
		self.FRONT = 1

	# Function to return the position of
	# parent for the node currently
	# at pos

	def empty(self):
		return self.size==0

	def parent(self, pos):
		
		return pos // 2

	# Function t	o return the position of
	# the left child for the node currently
	# at pos
	def leftChild(self, pos):
		
		return 2 * pos

	# Function to return the position of
	# the right child for the node currently
	# at pos
	def rightChild(self, pos):
		
		return (2 * pos) + 1

	# Function that returns true if the passed
	# node is a leaf node
	def isLeaf(self, pos):
		
		if pos >= (self.size//2) and pos <= self.size:
			return True
		return False

	# Function to swap two nodes of the heap
	def swap(self, fpos, spos):
		
		self.Heap[fpos], self.Heap[spos] = (self.Heap[spos],
											self.Heap[fpos])

	# Function to heapify the node at pos
	def maxHeapify(self, pos):
		# print(pos)
		# If the node is a non-leaf node and smaller
		# than any of its child
		if not self.isLeaf(pos):
			try:
				leftcheck=self.Heap[pos][1] < self.Heap[self.leftChild(pos)][1]
				leftc=self.Heap[self.leftChild(pos)][1]
			except:
				leftcheck=False
				leftc=-sys.maxsize
			
			try:
				rightcheck=self.Heap[pos][1] < self.Heap[self.rightChild(pos)][1]
				rightc=self.Heap[self.rightChild(pos)][1]
			except:
				rightcheck=False
				rightc=-sys.maxsize

			# print(self.Heap[pos], self.Heap[self.leftChild(pos)], self.Heap[self.rightChild(pos)])
			if (leftcheck or rightcheck):
				
				# Swap with the left child and heapify
				# the left child
				if (leftc > rightc):
					self.swap(pos, self.leftChild(pos))
					self.maxHeapify(self.leftChild(pos))

				# Swap with the right child and heapify
				# the right child
				else:
					self.swap(pos, self.rightChild(pos))
					self.maxHeapify(self.rightChild(pos))

	# Function to insert a node into the heap
	def insert(self, element):
		
		if self.size >= self.maxsize:
			return
		self.size += 1
		self.Heap[self.size] = element

		current = self.size
		# print(self.Heap[current])

		while (self.Heap[current][1] >
			self.Heap[self.parent(current)][1]):
			self.swap(current, self.parent(current))
			current = self.parent(current)

	# Function to print the contents of the heap
	def Print(self):
		
		for i in range(1, (self.size // 2) + 1):
			print("PARENT : " + str(self.Heap[i]) +
				"\nLEFT CHILD : " + str(self.Heap[2 * i]) +
				"\nRIGHT CHILD : " + str(self.Heap[2 * i + 1]))

	# Function to remove and return the maximum
	# element from the heap
	def extractMax(self):

		popped = self.Heap[self.FRONT]
		self.Heap[self.FRONT] = self.Heap[self.size]
		self.size -= 1
		self.maxHeapify(self.FRONT)
		
		return popped

# # Driver Code
# if __name__ == "__main__":
	
# 	print('The maxHeap is ')
	
# 	maxHeap = MaxHeap(15)
# 	maxHeap.insert(['a',5])
# 	maxHeap.insert(['b',3])
# 	maxHeap.insert(['c',17])
# 	maxHeap.insert(['d',10])
# 	maxHeap.insert(['e',84])
# 	maxHeap.insert(['f',19])
# 	maxHeap.insert(['g',6])
# 	maxHeap.insert(['h',22])
# 	maxHeap.insert(['i',9])

# 	maxHeap.Print()
	
# 	while not maxHeap.empty():
# 		print(f'Max: {maxHeap.extractMax()}')
# 		# maxHeap.Print()