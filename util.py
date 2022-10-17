import random as rand
from dataStructures import BinaryTree, Queue, DoubleNode
import matplotlib.pyplot as mp

def ROT(n,word):
    newWord=""
    lowerAbecedary = "abcdefghijklmnopqrstuvwxyz"
    upperAbecedary = lowerAbecedary.upper()
    for i in word:
        if i == ' ':
            newWord += i
        else:
            if(i==i.upper()):
                index = upperAbecedary.index(i)
                newWord += upperAbecedary[(index+n)%len(upperAbecedary)]
            else:
                index = lowerAbecedary.index(i)
                newWord += lowerAbecedary[(index+n)%len(upperAbecedary)]
    return newWord

def getRandomClasicBinaryTree(height,intMin=1,intMax=10):
    tree = BinaryTree()
    tree.addKey(0)
    queue = Queue()
    queue.enqueue(tree.root)
    for i in range(height):
        for j in range(2**(i)):
            current = queue.dequeue()
            current.left = DoubleNode(rand.randint(1,25))
            current.right = DoubleNode(rand.randint(1,25))
            queue.enqueue(current.left)
            queue.enqueue(current.right)
    return tree

def getNotRandomClasicBinaryTree(height,intLeft,intRight):
    tree = BinaryTree()
    tree.addKey(0)
    queue = Queue()
    queue.enqueue(tree.root)
    for i in range(height):
        for j in range(2**(i)):
            current = queue.dequeue()
            current.left = DoubleNode(intLeft)
            current.right = DoubleNode(intRight)
            queue.enqueue(current.left)
            queue.enqueue(current.right)
    return tree

def ROTTree(word,tree):
    newWord = ""
    path = []
    current = tree.root
    for i in word:
        current = rand.choice([current.left,current.right])
        path.append(current.data)
        newWord += ROT(current.data,i)
    return newWord,path