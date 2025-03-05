# You have 4 different stimuli numbered 1 to 4. Create a random
# presentation order consisting of 100 trials in total.
import random
import numpy as np

stim = list(range(1, 5)) * 25
random.shuffle(stim)

# or via numpy
stim = np.arange(1, 5).repeat(25)
np.random.shuffle(stim)

# with non-repetition constraint
myStimuli = np.arange(1, 21).repeat(5)
while 0 in np.diff(myStimuli):
    np.random.shuffle(myStimuli)
