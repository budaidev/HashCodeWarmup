from collections import namedtuple

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
            ingredients |=  like
            ingredients |=  dislike
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

clients, ingredients = readExample(filename)
mappings = getMapping(ingredients)
like, dislike = convertToVector(clients, mappings)