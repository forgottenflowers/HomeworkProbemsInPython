# An experiment to assess cognitive abilities and reaction speed of User.

from __future__ import with_statement
import os
import sys
import datetime as dt
import random
import csv
from psychopy import visual,event,core,sound


# ############################ VP Info ########################################
vp_num=0
age=0
gender=0
handedness=0

while not vp_num:
    try:
        vp_num = int(input("VP number?: "))
    except ValueError:
        print("Number required")

while age not in range(18, 61):
    try:
        age = int(input("Age?: "))
    except ValueError:
        print("Number between 18 and 60 required!")

while gender not in ("m", "f"):
    gender = input("Gender (m/f)?: ").lower()

while handedness not in ("r", "l"):
    handedness = input("Handedness (r/l)?: ").lower()



# ######################### Files #############################################

files = {"dirname": os.getcwd(), "filename": __file__}
files["expname"] = os.path.basename(files["filename"])[:-3]
files["date"] = dt.datetime.today().strftime("%d/%m/%Y")
files["insdir"] = files["dirname"] + os.sep + "Instructions"
files["resdir"] = files["dirname"] + os.sep + "Results"

# create results directory if required
if not os.path.isdir(files["resdir"]):
    os.makedirs(files["resdir"])

tmpName = files["resdir"] + os.sep + files["expname"]
files["resfile"] = tmpName + "_" + str(vp_num) + ".res"

if os.path.isfile(files["resfile"]):
    askUser = None
    while askUser not in ["y", "n"]:
        askUser = input("File exists! Overwrite? (y, n): ").lower()
    if askUser == "y":
        os.remove(files["resfile"])
    elif askUser == "n":
        sys.exit()


# ############################## Defining Parameters #################################

#We need 4.2 cm rectangle, which is 158.74 pixels as per unitconverters.net. However, for our problem we need to round this number 
#to the nearest whole number that is divisible by 6 (by both 2 and 3). We call this parameter as 'rectsize' = 156.
rectsize=156
stop2=rectsize/2
stop1=stop2-rectsize/3
border=stop1
dim=rectsize+border

#defining times
fourdotdisp=0.1 #100 milliseconds
fullmatdisp=0.1
blackdisp=0.067 #this number was chosen upon rounding up time to closest possible resolution for the computer
#defining sounds
losound=sound.Sound(1000,fourdotdisp)
hisound=sound.Sound(1259,fourdotdisp)
soundz=[losound,hisound]




# ############################## Instructions #################################

win2=visual.Window(size=(600,600))
rect=visual.Rect(
    win=win2,
    units="pix",
    width=dim,
    height=dim,
    fillColor=[-1, -1, -1],
    lineWidth=0
)
dot1=visual.Rect(
    win=win2,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(-stop1,stop2)
)
dot2=visual.Rect(
    win=win2,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(stop1,stop2)
)
dot3=visual.Rect(
    win=win2,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(-stop1,stop1)
)
dot4=visual.Rect(
    win=win2,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(stop1,stop1)
)
dot5=visual.Rect(
    win=win2,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(stop2,stop1)
)
dot6=visual.Rect(
    win=win2,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(stop1,-stop1)
)
dot7=visual.Rect(
    win=win2,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(-stop1,-stop2)
)
dot8=visual.Rect(
    win=win2,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(stop2,-stop2)
)
inst_4dots=[dot1,dot4,dot7,dot8]
inst_target=[dot2,dot3,dot5,dot6]
def inst_stim(dotz):
    rect.draw()
    for dotiter in dotz:
        dotiter.draw()


txt=visual.TextStim(win2, text=" ",height=0.08,wrapWidth=1.75)
txt.setAutoDraw(True)

while True:
    txt.text="Hello! \n\nIn the following experiment you will see a series of rapidly-changing displays consisting of 4 dots which appear at different positions of the screen. \n\n\nPress any key to continue..."
    win2.flip()
    event.waitKeys()
    txt.text="An example 4-dot display can be seen below: \n\n\n\n\n\n\n\n\n\n\n\nPress any key to continue..."
    inst_stim(inst_4dots)
    win2.flip()
    event.waitKeys()
    txt.text="In some of those 4-dot displays, the 4 dots will take the shape of a diamond. An example can be seen below: \n\n\n\n\n\n\n\n\n\n\n\nPress any key to continue..."
    inst_stim(inst_target)
    win2.flip()
    event.waitKeys()
    txt.text="These displays in which the 4 dots take the shape of a diamond are the target displays that you should detect! The diamond in these target displays can appear at 4 different positions: in the lower left area, the upper left area, the upper right area or the lower right area of the screen. Your task is to indicate the position at which the diamond appeared on the screen by pressing the A, Q, W or S key, respectively (A=lower left, Q=upper left, W=upper right, S=lower right). Please keep your left-hand index finger throughout the experiment on the “A” key, your left-hand middle finger on the “Q” key, your right-hand index finger on the “S” key, and your right-hand middle finger on the “W” key. \n\n\nPress any key to continue..."
    win2.flip()
    event.waitKeys()
    txt.text="Every trial of this experiment consists of a sequence of four of the 4-dot displays which will be repeated until a key is pressed or a maximum of 10 repetitions of the sequence has been reached. The target display will always be the 3rd display in the sequence. Each sequence of 4-dot displays will be synchronized with a tone sequence of either 4 low tones (“LLLL”) or 3 low tones and 1 high tone at the 3rd position (“LLHL”). \n\n\nPress any key to continue..."
    win2.flip()
    event.waitKeys()
    txt.text="Moreover, you will hear a series of 4 to 8 warm-up sequences before the actual trial sequence is presented, in which you will hear the tone sequence for this trial, but in which you won’t see any 4-dot displays. These warm-up sequences are there to make you familiar with the tone sequence that will also be played along with the subsequent sequence of 4-dot displays.\n\n\nPress any key to continue..."
    win2.flip()
    event.waitKeys()
    txt.text="Before we really start, there will be 16 practice trials for you to make you familiar with the procedure of this experiment. The first 8 of these will be presented at half the speed of the experimental trials. The other 8 practice trials will be presented at the same speed as the experimental trials. \n\nPlease press the [space] bar if you are ready for the practice trials! \n\nOtherwise press any other key to repeat the instructions."
    win2.flip()
    kk=event.waitKeys()
    if "space" in kk:
        txt.text="Good Luck! \n\n\nPress the [escape] key any time to fast forward."
        win2.flip()
        core.wait(1.4)
        break
win2.close()




# ############################## Defining Stimuli Parameters #################################

win=visual.Window(size=(dim,dim),color=(-1,-1,-1))

#defining dot positions in mask
dot_1_1=visual.Rect(
    win=win,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(-stop2,stop2)
)
dot_1_2=visual.Rect(
    win=win,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(-stop1,stop2)
)
dot_1_3=visual.Rect(
    win=win,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(stop1,stop2)
)
dot_1_4=visual.Rect(
    win=win,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(stop2,stop2)
)
dot_2_1=visual.Rect(
    win=win,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(-stop2,stop1)
)
dot_2_2=visual.Rect(
    win=win,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(-stop1,stop1)
)
dot_2_3=visual.Rect(
    win=win,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(stop1,stop1)
)
dot_2_4=visual.Rect(
    win=win,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(stop2,stop1)
)
dot_3_1=visual.Rect(
    win=win,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(-stop2,-stop1)
)
dot_3_2=visual.Rect(
    win=win,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(-stop1,-stop1)
)
dot_3_3=visual.Rect(
    win=win,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(stop1,-stop1)
)
dot_3_4=visual.Rect(
    win=win,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(stop2,-stop1)
)
dot_4_1=visual.Rect(
    win=win,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(-stop2,-stop2)
)
dot_4_2=visual.Rect(
    win=win,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(-stop1,-stop2)
)
dot_4_3=visual.Rect(
    win=win,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(stop1,-stop2)
)
dot_4_4=visual.Rect(
    win=win,
    units="pix",
    width=4,
    height=4,
    fillColor=[1,1,1],
    pos=(stop2,-stop2)
)

mask=[dot_1_1,dot_1_2,dot_1_3,dot_1_4,dot_2_1,dot_2_2,dot_2_3,dot_2_4,dot_3_1,dot_3_2,dot_3_3,dot_3_4,dot_4_1,dot_4_2,dot_4_3,dot_4_4]

#defining 4-dot target patterns to choose from
#sounds can be high and low sounds
#Target positions can be: 5=Q=upper left, 6=W=upper right, 9=A=lower left, 10=S=lower right
#16 possibilities, where each combination of target position and sound occurs 2 times
choosefrom=[[5,hisound],[5,losound],[6,hisound],[6,losound],[9,hisound],[9,losound],[10,hisound],[10,losound],[5,hisound],[5,losound],[6,hisound],[6,losound],[9,hisound],[9,losound],[10,hisound],[10,losound]]




# ############################## Defining Common Functions #################################

def showmask(waitt):
    for dotiter in mask:
        dotiter.draw()
    win.flip()
    core.wait(waitt)

def showdark(waitti):
    win.flip()
    core.wait(waitti)

def stimulus(dotpositions,soundplay,waittime):
    for dotiter in dotpositions:
        dotiter.draw()
    win.callOnFlip(soundplay.play)
    win.flip()
    core.wait(waittime)
    soundplay.stop()

#generate pseudo-random patterns to be displayed based on target
def generate(target):
    t3=[mask[target-4],mask[target-1],mask[target+1],mask[target+4]]
    rest=[x for x in mask if x not in t3]
    t1=random.sample(rest,4)
    rest1=[x for x in rest if x not in t1]
    t2=random.sample(rest1,4)
    t4=[x for x in rest1 if x not in t2]
    return t1,t2,t3,t4

#displaying messages
#messg displayed on small screen
messg=visual.TextStim(win,text=" ",height=0.2)

def warmup(tone):
    messg.text="Warm-up!"
    messg.draw()
    win.flip()
    core.wait(0.2)
    ntimespossible=[4,5,6,7,8] #randomly 4-8 times
    ntimes=random.choice(ntimespossible)
    for nt in range(0,ntimes):
        
        keyresp=event.getKeys()
        
        win.callOnFlip(losound.play)
        for dotiter in mask:
            dotiter.draw()
        win.flip()
        core.wait(fullmatdisp*2)
        losound.stop()
        win.flip()
        core.wait(blackdisp)
        win.callOnFlip(losound.play)
        for dotiter in mask:
            dotiter.draw()
        win.flip()
        core.wait(fullmatdisp*2)
        losound.stop()
        win.flip()
        core.wait(blackdisp)
        win.callOnFlip(tone.play)
        for dotiter in mask:
            dotiter.draw()
        win.flip()
        core.wait(fullmatdisp*2)
        tone.stop()
        win.flip()
        core.wait(blackdisp)
        win.callOnFlip(losound.play)
        for dotiter in mask:
            dotiter.draw()
        win.flip()
        core.wait(fullmatdisp*2)
        losound.stop()
        win.flip()
        core.wait(blackdisp)
        
        if keyresp.count('escape')>0:
            break


def early():
    messg.text="too early!\n\ntry again"
    messg.draw()
    win.flip()
    core.wait(0.2)

def correct():
    messg.text="Correct!"
    messg.draw()
    win.flip()
    core.wait(0.2)

def incorrect():
    messg.text="Incorrect!"
    messg.draw()
    win.flip()
    core.wait(0.2)

def nokey():
    messg.text="No key press detected.\n\nStay focussed for next target."
    win.flip()
    messg.draw()
    core.wait(0.2)




# ############################## Practice Trials #################################

messg.text="Practice Trials\n\nPress any key to continue"
messg.draw()
win.flip()
event.waitKeys()

#choose a random permutation of the 16 possibilities in the 'choosefrom' variable
chosen=choosefrom
random.shuffle(chosen)
slow=chosen[0:8]
fast=chosen[8:16]
dummyscore=[0,0,0,0,0,['q'],['w'],0,0,['a'],['s']]

#slow trial
messg.text="Slow Trials\n\nPress any key to continue"
messg.draw()
win.flip()
event.waitKeys()
for choice in slow:
    
    keyresp=event.getKeys()
    
    target=choice[0]
    sound3=choice[1]
    
    #warmup twice as slow
    messg.text="Warm-up!"
    messg.draw()
    win.flip()
    core.wait(0.2)
    ntimespossible=[4,5,6,7,8] #randomly 4-8 times
    ntimes=random.choice(ntimespossible)
    for nt in range(0,ntimes):
        
        keyresp=event.getKeys()
        
        win.callOnFlip(losound.play)
        for dotiter in mask:
            dotiter.draw()
        win.flip()
        core.wait(fullmatdisp*4)
        losound.stop()
        win.flip()
        core.wait(blackdisp*2)
        win.callOnFlip(losound.play)
        for dotiter in mask:
            dotiter.draw()
        win.flip()
        core.wait(fullmatdisp*4)
        losound.stop()
        win.flip()
        core.wait(blackdisp*2)
        win.callOnFlip(sound3.play)
        for dotiter in mask:
            dotiter.draw()
        win.flip()
        core.wait(fullmatdisp*4)
        sound3.stop()
        win.flip()
        core.wait(blackdisp*2)
        win.callOnFlip(losound.play)
        for dotiter in mask:
            dotiter.draw()
        win.flip()
        core.wait(fullmatdisp*4)
        losound.stop()
        win.flip()
        core.wait(blackdisp*2)
        
        if keyresp.count('escape')>0:
            break


    if keyresp.count('escape')>0:
        break

    #real trial starts here
    messg.text="START"
    messg.draw()
    win.flip()
    core.wait(0.2)
    
    #generating 4-dot patterns for current trial
    t1,t2,t3,t4=generate(target)
    
    keyresp=0
    #repeating this pattern 10 times
    for repeats in range(1,11):

        stimulus(t1,losound,fourdotdisp*2) #distractor
        showmask(fullmatdisp*2)
        showdark(blackdisp*2)
        keyresp=event.getKeys() #defining key press variable
        if keyresp: #checking key press condition
            if keyresp.count('escape')>0:
                break
            if repeats==1:
                keyresp=0
                early()
            elif keyresp==dummyscore[target]:
                correct()
                break
            else:
                incorrect()
                break
        
        stimulus(t2,losound,fourdotdisp*2) #distractor
        showmask(fullmatdisp*2)
        showdark(blackdisp*2)
        keyresp=event.getKeys() #defining key press variable
        if keyresp: #checking key press condition again
            if keyresp.count('escape')>0:
                break
            if repeats==1:
                keyresp=0
                early()
            elif keyresp==dummyscore[target]:
                correct()
                break
            else:
                incorrect()
                break
        
        stimulus(t3,sound3,fourdotdisp*2) #target pattern
        showmask(fullmatdisp*2)
        showdark(blackdisp*2)
        keyresp=event.getKeys() #defining key press variable
        if keyresp: #checking key press condition again
            if keyresp.count('escape')>0:
                break
            if keyresp==dummyscore[target]:
                correct()
                break
            else:
                incorrect()
                break
        
        stimulus(t4,losound,fourdotdisp*2) #distractor
        showmask(fullmatdisp*2)
        showdark(blackdisp*2)
        keyresp=event.getKeys() #defining key press variable
        if keyresp: #checking key press condition again
            if keyresp.count('escape')>0:
                break
            if keyresp==dummyscore[target]:
                correct()
                break
            else:
                incorrect()
                break
    
    if keyresp.count('escape')>0:
        break
    
    #if no key was pressed
    if keyresp==0:
        nokey()



#fast trial
messg.text="Fast Trials\n\nPress any key to continue"
messg.draw()
win.flip()
event.waitKeys()
for choice in fast:
    
    keyresp=event.getKeys()
    if keyresp.count('escape')>0:
        break
    
    target=choice[0]
    sound3=choice[1]
    
    #warmup
    warmup(sound3)
    
    #real trial starts here
    messg.text="START"
    messg.draw()
    win.flip()
    core.wait(0.2)
    target=choice[0]
    sound3=choice[1]
    
    #generating 4-dot patterns for current trial
    t1,t2,t3,t4=generate(target)
    
    keyresp=0
    #repeating this pattern 10 times
    for repeats in range(1,11):
    
        keyresp=event.getKeys()
        if keyresp.count('escape')>0:
            break
        
        stimulus(t1,losound,fourdotdisp) #distractor
        showmask(fullmatdisp)
        showdark(blackdisp)
        keyresp=event.getKeys() #defining key press variable
        if keyresp: #checking key press condition
            if repeats==1:
                keyresp=0
                early()
            elif keyresp==dummyscore[target]:
                correct()
                break
            else:
                incorrect()
                break
        
        stimulus(t2,losound,fourdotdisp) #distractor
        showmask(fullmatdisp)
        showdark(blackdisp)
        keyresp=event.getKeys() #defining key press variable
        if keyresp: #checking key press condition again
            if repeats==1:
                keyresp=0
                early()
            elif keyresp==dummyscore[target]:
                correct()
                break
            else:
                incorrect()
                break
        
        stimulus(t3,sound3,fourdotdisp) #target pattern
        showmask(fullmatdisp)
        showdark(blackdisp)
        keyresp=event.getKeys() #defining key press variable
        if keyresp: #checking key press condition again
            if keyresp==dummyscore[target]:
                correct()
                break
            else:
                incorrect()
                break
        
        stimulus(t4,losound,fourdotdisp) #distractor
        showmask(fullmatdisp)
        showdark(blackdisp)
        keyresp=event.getKeys() #defining key press variable
        if keyresp: #checking key press condition again
            if keyresp==dummyscore[target]:
                correct()
                break
            else:
                incorrect()
                break
        
        if keyresp.count('escape')>0:
            break
    
    if keyresp.count('escape')>0:
        break
    
    #if no key was pressed
    if keyresp==0:
        nokey()




# ######################### Experiment begins: Stimulus Sequence #################################

messg.text="Begin Experiment\n\nPress any key to continue"
messg.draw()
win.flip()
event.waitKeys()

#defining column lengths to be printed to output file
trials=160
trialnum=range(0,trials) #trial number-1
targetpos=[0]*trials #target position
keypress=[0]*trials #key press response
score=[0]*trials #score = 0 if response was incorrect, score=1 if response was correct
NTS=[0]*trials #number of times target was shown before key press response (<10)


rows=-1
for shuff in range(0,10): #this is executed 10 times
    
    keyresp=event.getKeys()
    if keyresp.count('escape')>0:
        break

    #choose a random permutation of the 16 possibilities in the 'choosefrom' variable
    chosen=choosefrom
    random.shuffle(chosen)

    for choice in chosen: #this is executed 16 times (16*10=160)
        
        keyresp=event.getKeys()
        if keyresp.count('escape')>0:
            break
        
        #warmup
        warmup(sound3)
        
        #real trial starts here
        messg.text="START TRIAL"+str(rows+1)
        messg.draw()
        win.flip()
        core.wait(0.2)
        rows+=1
        target=choice[0]
        targetpos[rows]=target
        sound3=choice[1]
        
        #generating 4-dot patterns for current trial
        t1,t2,t3,t4=generate(target)
        
        #repeating this pattern 10 times
        for repeats in range(1,11):
            
            stimulus(t1,losound,fourdotdisp) #distractor
            showmask(fullmatdisp)
            showdark(blackdisp)
            keyresp=event.getKeys() #defining key press variable
            if keyresp: #checking key press condition
                if repeats==1:
                    keyresp=0
                    early()
                else:
                    keypress[rows]=keyresp #storing the key press response for current trial
                    NTS[rows]=repeats-1 #storing the number of times the pattern was repeated before (or at) key press
                    break
            
            stimulus(t2,losound,fourdotdisp) #distractor
            showmask(fullmatdisp)
            showdark(blackdisp)
            keyresp=event.getKeys() #defining key press variable
            if keyresp: #checking key press condition again
                if repeats==1:
                    keyresp=0
                    early()
                else:
                    keypress[rows]=keyresp
                    NTS[rows]=repeats-1   
                    break
            
            stimulus(t3,sound3,fourdotdisp) #distractor
            showmask(fullmatdisp)
            showdark(blackdisp)
            keyresp=event.getKeys() #defining key press variable
            if keyresp: #checking key press condition again
                keypress[rows]=keyresp
                NTS[rows]=repeats
                break
            
            stimulus(t4,losound,fourdotdisp) #distractor
            showmask(fullmatdisp)
            showdark(blackdisp)
            keyresp=event.getKeys() #defining key press variable
            if keyresp: #checking key press condition again
                keypress[rows]=keyresp
                NTS[rows]=repeats
                break
        
            if keyresp.count('escape')>0:
                break
        
        if keyresp.count('escape')>0:
            break
        
        #if no key was pressed
        if keypress[rows]==0:
            nokey()
            
    if keyresp.count('escape')>0:
        break

messg.text="Thank You!"
messg.draw()
win.flip()
core.wait(0.5)
win.close()




# ############################## Save Results #################################

expname = "flickerdots"
date = dt.datetime.today().strftime("%d/%m/%Y")

#changing the way target position is to be displayed in words and simultaneously scoring the response
for change in trialnum:
    if targetpos[change]==5:
        targetpos[change]="upper left"
        if keypress[change]==['q']:
            score[change]+=1
    elif targetpos[change]==6:
        targetpos[change]="upper right"
        if keypress[change]==['w']:
            score[change]+=1
    elif targetpos[change]==9:
        targetpos[change]="lower left"
        if keypress[change]==['a']:
            score[change]+=1
    else:
        targetpos[change]="lower right"
        if keypress[change]==['s']:
            score[change]+=1

#update trial numbers to start from 1 instead of 0
trialnum=[x+1 for x in trialnum]

#writing results to output file
total=[[expname]*trials,[date]*trials,[vp_num]*trials,[age]*trials,[gender]*trials,[handedness]*trials,trialnum,targetpos,keypress,score,NTS]
total=list(map(list, zip(*total)))
final=[["Exp name","dd/mm/yyyy","vp_num","age","gender","handed","Trial#","Target pos","Keypress","Score","NTS"]]
final.extend(total)
with open(files["resfile"], "w", newline="") as f:
    writer = csv.writer(f,delimiter='\t')
    writer.writerows(final)

core.quit()
