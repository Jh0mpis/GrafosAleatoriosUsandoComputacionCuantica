import random as rand
from dataStructures import BinaryTree, Queue
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
    numOfElements = -(1-2**(height+1))
    tree = BinaryTree()
    for i in range(numOfElements):
        tree.addKey(rand.randint(intMin,intMax))
    return tree

def getNotRandomClasicBinaryTree(height,intLeft,intRight):
    numOfElements = -(1-2**(height+1))
    tree = BinaryTree()
    tree.addKey(0)
    for i in range(int((numOfElements-1)/2)):
        tree.addKey(intLeft)
        tree.addKey(intRight)
    return tree

def ROTTree(word,tree):
    newWord = ""
    path = ""
    current = tree.root
    for i in word:
        current = rand.choice([current.left,current.right])
        path += str(current.data)
        newWord += ROT(current.data,i)
    return newWord,path