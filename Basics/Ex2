# Example problem 2
# Write a program to test your arithmetic skills. Each
#   trial will ask the set to answer an addition question.
#   Provide feedback regarding correct vs. incorrect. Use the
#   number set 1-100. Additionally, calculate a total score
#   and a total time for 10 trials.

import random
import time

# experimental parameters
num_trials = 10
num_range = [1, 100]

score = 0
startTime = time.time()

# trial loop
for trl in range(num_trials):

    num1 = random.randint(num_range[0], num_range[1])
    num2 = random.randint(num_range[0], num_range[1])

    question = "{} + {} = ? ".format(num1, num2)
    ans = None
    while ans is None:
        try:
            ans = int(input(question))
        except ValueError:
            ans = None

    # give feedback
    if ans == num1 + num2:
        print("CORRECT\n")
        score += 1
    else:
        print("INCORRECT! The correct answer is {}\t".format(num1 + num2))

print("Score:{0}\tTime:{1:.3f} S".format(score, time.time() - startTime))
