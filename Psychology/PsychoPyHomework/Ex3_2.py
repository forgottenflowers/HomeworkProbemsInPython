from psychopy import visual,event

win=visual.Window(size=(640,480))

xpos=0
isflip=0
center=0
right=640/2-50
left=-640/2+50
direction=1


while True:
        img=visual.ImageStim(win,image="man.png",flipVert=isflip,units="pix",pos=(xpos,0))
        img.draw()
        win.flip()
        if xpos==right:
            direction=-1
        if xpos==left:
            direction=1
        if direction==1:
            xpos+=1
        else:
            xpos-=1
        keys=event.getKeys()
        if keys:
            if "escape" in keys:
                break
            if "f" in keys:
                if isflip==0:
                    isflip=1
                else:
                    isflip=0
