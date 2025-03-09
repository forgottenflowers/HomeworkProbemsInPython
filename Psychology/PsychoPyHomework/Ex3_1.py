from psychopy import visual,event

win=visual.Window(size=(640,480))

img=visual.ImageStim(win,image="man.png")
imgflip1=visual.ImageStim(win,image="man.png",flipVert=True,units="pix",pos=(100,0))
imgflip2=visual.ImageStim(win,image="man.png",flipVert=True,units="pix",pos=(-100,0))

img.draw()
imgflip1.draw()
imgflip2.draw()
win.flip()

event.waitKeys()
win.close()
