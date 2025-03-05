# Example problem 4.1
# Read in a text file, convert all vowels to upper case then write
# out a new text file. Write two versions:
# 1) Standard for loop
# 2) List comprehension

# part 1
with open("someText1.txt", "r") as f:
    txt = f.read()

# loops
new_str = ""
for let in txt:
    if let in ("aeiou"):
        new_str += let.upper()
    else:
        new_str += let

# list comprehensions
new_str = "".join([let.upper() if let in ("aeiou") else let for let in txt])

with open("someText1_new.txt", "w") as f:
    f.write(new_str)
