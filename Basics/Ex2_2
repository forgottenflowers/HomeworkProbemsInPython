# Example problem 2
# Write a program to test your arithmetic skills. Each
#   trial will ask the set to answer an addition question.
#   Provide feedback regarding correct vs. incorrect. Use the
#   number set 1-100. Additionally, calculate a total score
#   and a total time for 10 trials.

import numpy as np
import time

# experimental parameters
num_trials = 4
num_range = range(1, 11)
wait_time = 0.5

# stimulus and data matrix
dat = np.zeros(shape=(num_trials, 5))
dat[:, 0:2] = np.random.randint(num_range[0], num_range[-1], size=(num_trials, 2))
dat[:, 2] = dat[:, 0] + dat[:, 1]

# trial loop
for trl in range(num_trials):

    # short pause between trials
    time.sleep(wait_time)
    print("Trial {} from {}.\n".format(trl + 1, num_trials))

    time_start = time.time()
    ans = None
    while ans is None:
        try:
            ans = int(
                input("{}+{} = ".format(str(int(dat[trl, 0])), str(int(dat[trl, 1]))))
            )
        except ValueError:
            ans = None

    # record RT
    dat[trl, 3] = time.time() - time_start

    # give feedback
    if ans == dat[trl, 2]:
        print("\nCORRECT")
        dat[trl, 4] = 1
    else:
        print("\nINCORRECT! The correct answer is {}".format((dat[trl, 2])))

# calculate number correct and mean RT
mean_rt = np.mean(dat[:, 3])
num_corr = np.sum(dat[:, 4])

print("Number correct: {0}\t Mean RT: {1:.3f} S".format(int(num_corr), mean_rt))
