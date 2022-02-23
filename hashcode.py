from collections import namedtuple
import numpy as np

filename = './GoogleExample/b_basic.in.txt'
Client = namedtuple('Client', ['like', 'dislike'])

def readExample(filename):
    clients = list()
    ingredients = set()
    with open(filename, 'r') as reader:
        # Read and print the entire file line by line
        num = int(reader.readline())
        for i in range(0,num):
            like = set(reader.readline().strip().split(" ")[1:])
            dislike = set(reader.readline().strip().split(" ")[1:])
            ingredients |= like
            ingredients |= dislike
            c = Client(like, dislike,)
            clients.append(c)
    return clients, ingredients

def getMapping(ingredients):
    mapping = {}
    cnt = 0
    for ing in ingredients:
        mapping[ing]=cnt
        cnt+=1
    return mapping

def toVector(ings, mappings):
    l = [0] * len(mappings)
    for i in ings:
        l[mappings[i]] = 1
    return l

def convertToVector(clients, mappings):
    likeMatrix = list()
    dislikeMatrix = list()
    for c in clients:
        l1 = toVector(c.like, mappings)
        likeMatrix.append(l1)
        l2 = toVector(c.dislike, mappings)
        dislikeMatrix.append(l2)
    return likeMatrix, dislikeMatrix

def calculateScore(np_like, np_dislike, np_ing):
    dislike_score = np_dislike.dot(np_ing)
    dislike_vec = 1 - np.where(dislike_score>0.5, 1, dislike_score)
    like_score = np_like - np_ing
    like_vec = 1- np.any(like_score>0.5, axis=1).astype(int)
    return np.sum(like_vec.dot(dislike_vec))

clients, ingredients = readExample(filename)
mappings = getMapping(ingredients)
like, dislike = convertToVector(clients, mappings)

np_like = np.array(like)
np_dislike = np.array(dislike)

vec = np.array([1,1,1,1,1,1])
calculateScore(np_like, np_dislike, vec)