from psychopy import visual,event,core

timer=core.Clock()

win=visual.Window()
txt=visual.TextStim(win, text="Key:{}".format(" "))
txt.setAutoDraw(True)

while True:
        keys=event.getKeys()
        temp=timer.getTime()
        if keys:
            if "escape" in keys:
                break
            else:
                txt.text="Key:{}".format(keys[0])
                lastkey=temp
        win.flip()

print("total time:",timer.getTime())
print("time since last key press:",timer.getTime()-lastkey)
win.close()
