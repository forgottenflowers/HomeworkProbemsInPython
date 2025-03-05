import numpy as np

dat = [[3, 5, 7], [2, 9, 3], [1, 9, 4]]

###############################################
# Calculate the mean of each list
# for loop
means = []
for d in dat:
    means.append(sum(d) / len(d))

# list comprehension
means = [sum(d) / len(d) for d in dat]

# lambda expression
means = list(map(lambda x: sum(x) / len(x), dat))

# numpy
means = np.array(dat).mean(1)

###############################################
# Calculate the mean of the numbers in the same position within each list
# for loop
means = []
for d in zip(*dat):
    means.append(sum(d) / len(d))

# list comprehension
means = [sum(d) / len(d) for d in zip(*dat)]

# lambda expression
means = list(map(lambda x: sum(x) / len(x), zip(*dat)))

# numpy
means = np.array(dat).mean(0)

###############################################
# Find the maximum value in each list
# for loop
maxVals = []
for d in dat:
    maxVals.append(max(d))

# list comprehension
maxVals = [max(x) for x in dat]

# lambda
maxVals = list(map(lambda x: max(x), dat))

# numpy
maxVals = np.array(dat).max(1)

###############################################
#  Find the minimum value in the same position within each list
# for loop
minVals = []
for x in zip(*dat):
    minVals.append(min(x))

# list comprehension
minVals = [min(x) for x in zip(*dat)]

# lambda expression
minVals = list(map(lambda x: min(x), zip(*dat)))

# numpy
minVals = np.array(dat).min(0)

###############################################
# Change all 9’s in each list to 99
# python for loop
for x in dat:
    for idx, item in enumerate(x):
        if item == 9:
            x[idx] = 99

# list comprehension
dat1 = [[99 if y == 9 else y for y in x] for x in dat]

# lambda (nested)
dat1 = list(map(lambda x: list(map(lambda y: 99 if y == 9 else y, x)), dat))

# numpy
dat = np.array(dat)
dat[dat == 9] = 99
dat = dat.tolist()
