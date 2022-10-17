class DoubleNode:
    def __init__(self,item):
        self.data = item
        self.left, self.right = None, None


class Node:
    def __init__(self,item):
        self.data = item
        self.next = None


class NNode:
    def __init__(self,data):
        self.data = data
        self.nodes = []


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.pos = None

    def isEmpty(self):
        return self.head == None
        
    def pushFront(self,item):
        node = Node(item)
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            self.head = node

    def topFront(self):
        if(not self.isEmpty()):
            return self.head.data
        else:
            raise Exception("Empty Linked List")
    
    def popFront(self):
        if(not self.isEmpty()):
            data = self.head.data
            if self.head == self.tail:
                self.head = None
                self.tail = self.head
            else:
                self.head = self.head.next
            return data
        else:
            raise Exception("Empty Linked List")

    def pushBack(self,item):
        node = Node(item)
        if self.tail == None:
            self.tail = node
            self.head = self.tail
        else:
            self.tail.next = node
            self.tail = self.tail.next
    
    def topBack(self):
        if(not self.isEmpty()):
            return self.tail.data
        else:
            raise Exception("Empty Linked List")

    def popBack(self):
        if(not self.isEmpty()):
            data = self.tail.data
            if(self.tail == self.head):
                self.tail = None
                self.head = self.tail
            else:
                current = self.head
                while(current.next.next != None):
                    current = current.next
                self.tail = current
                self.tail.next = None
            return data
        else:
            raise Exception("Empty Linked List")

    def addBefore(self,node, key):
        current = self.head
        newNode = Node(key)
        while(current.next != node):
            current = current.next
        current.next = newNode
        newNode.next = node

    def addAfter(self, node, key):
        newNode = Node(key)
        newNode.next = node.next
        node.next = newNode

    def isInList(self, key):
        current = self.head
        self.pos = None
        while(current != None):
            if(current.data == key):
                return True
            current = current.next
            self.pos = current
        return False

    def find(self,key):
        if(self.isInList(key)):
            data = self.pos.data
            self.pos = None
            return data
        else:
            raise Exception(f"The element {key} is not in List")

    def erase(self):
        self.head = None
        self.tail = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.pos = None

    def isEmpty(self):
        return self.head == None
        
    def pushFront(self,item):
        node = DoubleNode(item)
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            node.right = self.head
            node.right.left = node
            self.head = node

    def topFront(self):
        if(not self.isEmpty()):
            return self.head.data
        else:
            raise Exception("Empty Double Linked List")
    
    def popFront(self):
        if(not self.isEmpty()):
            data = self.head.data
            if self.head == self.tail:
                self.head = None
                self.tail = self.head
            else:
                self.head = self.head.right
                self.head.left = None
            return data
        else:
            raise Exception("Empty Double Linked List")

    def pushBack(self,item):
        node = DoubleNode(item)
        if self.tail == None:
            self.tail = node
            self.head = self.tail
        else:
            self.tail.right = node
            self.tail.right.left = self.tail
            self.tail = self.tail.right
    
    def topBack(self):
        if(not self.isEmpty()):
            return self.tail.data
        else:
            raise Exception("Empty Double Linked List")

    def popBack(self):
        if(not self.isEmpty()):
            data = self.tail.data
            if(self.tail == self.head):
                self.tail = None
                self.head = self.tail
            else:
                self.tail = self.tail.left
                self.tail.left.right = self.tail
                self.tail.right = None
            return data
        else:
            raise Exception("Empty Double Linked List")

    def addBefore(self,node, key):
        newNode = Node(key)
        newNode.right = node
        newNode.left = node.left
        newNode.left.right = newNode
        newNode.right.left = newNode

    def addAfter(self, node, key):
        newNode = Node(key)
        newNode.next = node.next
        node.next = newNode

    def isInList(self, key):
        current = self.head
        self.pos = self.head
        while(current != None):
            if(current.data == key):
                return True
            current = current.right
            self.pos = current
        self.pos = None
        return False

    def getKey(self,key):
        if(self.isInList(key)):
            data = self.pos.data
            self.pos = None
            return data
        else:
            raise Exception(f"The element {key} is not in DoubleList")

    def getNode(self,key):
        if(self.isInList(key)):
            node = self.pos
            self.pos = None
            return node
        else:
            raise Exception(f"The element {key} is not in DoubleList")

    def erase(self):
        self.head = None
        self.tail = None


class Stack:
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top == None

    def push(self, item):
        if(self.isEmpty()):
            self.top = Node(item)
        else:
            node = Node(item)
            node.next  = self.top
            self.top = node
    
    def pop(self):
        if(not self.isEmpty()):
            data = self.top.data
            self.top = self.top.next
            return data
        else:
            raise Exception("Empty Stack")
    
    def clear(self):
        self.top = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.head == None

    def enqueue(self, item):
        if(self.isEmpty()):
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next
        
    def superEnqueue(self, *args):
        for i in args:
            self.enqueue(i)
    
    def dequeue(self):
        if(not self.isEmpty()):
            data = self.head.data
            if(self.head == self.tail):
                self.tail, self.head = None, None
            else:
                self.head = self.head.next
            return data
        else:
            raise Exception("Empty Stack")
    
    def clear(self):
        self.tail, self.head = None, None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.__path = Stack()

    def addKey(self,key):
        newNode = DoubleNode(key)
        if self.root == None:
            self.root = newNode
        else:
            queue = Queue()
            queue.enqueue(self.root)
            count = 0
            while(not queue.isEmpty()):
                current = queue.dequeue()
                if(current.left == None):
                    current.left = newNode
                    break
                elif(current.right == None):
                    current.right = newNode
                    break
                else: 
                    queue.superEnqueue(current.left, current.right)
                count += 1

    def preOrder(self):
        queue = Queue()
        queue.enqueue(self.root)
        while(not queue.isEmpty()):
            current = queue.dequeue()
            print(current.data)
            if(current.left != None):
                queue.enqueue(current.left)
            if(current.right != None):
                queue.enqueue(current.right)