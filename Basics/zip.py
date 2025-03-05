import random

mylists = [random.sample(range(1, 100), 5) for x in range(4)]

newlist = list(zip(mylists[0], mylists[1], mylists[2], mylists[3]))
newlist = list(zip(*mylists))
