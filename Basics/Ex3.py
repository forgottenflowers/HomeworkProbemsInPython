# example problem 3: VP information
# vp number

from datetime import datetime

vp_num = None
while not vp_num:
    try:
        vp_num = int(input("VP number?: "))
    except ValueError:
        print("Number required")

# vp details
gender = None
while gender not in ("m", "f", "d"):
    gender = input("Gender (m/f/d)?: ").lower()

# age
age = None
while age not in range(18, 61):
    try:
        age = int(input("Age?: "))
    except ValueError:
        print("Number between 18 and 60 required!")

# handedness
handedness = None
while handedness not in ("r", "l"):
    handedness = input("Handedness (r/l)?: ").lower()

# print to txt file
with open("vpInfo.txt", "w") as f:
    f.write("vpInfo\n")
    f.write("vpNum: {}\n".format(vp_num))
    f.write("Gender: {}\n".format(gender))
    f.write("Age: {}\n".format(age))
    f.write("Handedness: {}\n".format(handedness))
    f.write("Date: {}".format(datetime.now().strftime("%d/%m/%Y-%H:%M")))
