# eXAmple problem 4.2
# Read in text file with some written text. What is the longest
# word in the text? What is the most frequent word in the text?

from string import punctuation

with open("someText1.txt", "r") as f:
    txt = f.read()

mydict = {}
for word in txt.split():
    word = "".join(ch.lower() for ch in word if ch not in punctuation)
    if word not in mydict:
        mydict[word] = 1
    else:
        mydict[word] += 1

longest_word = max(mydict, key=len)
mydict[longest_word]

most_freq = max(mydict, key=lambda x: mydict[x])
mydict[most_freq]

# alternative using Counter from collections
from collections import Counter

with open("someText1.txt", "r") as f:
    txt = f.read()

txt = "".join(ch.lower() for ch in txt if ch not in punctuation)

counter = Counter(txt.split())
most_frequent = counter.most_common(1)
longest_word = max(counter, key=len)
