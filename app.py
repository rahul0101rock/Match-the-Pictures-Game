import pygame
import game_config as gc 
from animal import Animal
from pygame import display,event,image
from time import sleep
def findin(x,y):
    row=y//gc.imsize
    col=x//gc.imsize
    index=row*gc.numside+col
    return(index)
pygame.init()
display.set_caption("Memory Game By Rahul")
screen=display.set_mode((512,512))
matched =image.load('assets/matched.png')
run=True
tiles=[Animal(i) for i in range(0,gc.numtotal)]
crimg=[]
while run:
    ev=event.get()
    for e in ev:
        if e.type==pygame.QUIT:
            run=False
        if e.type ==pygame.KEYDOWN:
            if e.key==pygame.K_ESCAPE:
                run=False
        if e.type==pygame.MOUSEBUTTONDOWN:
            mx,my=pygame.mouse.get_pos()
            index=findin(mx,my)
            if index not in crimg:
                crimg.append(index)
            if len(crimg)>2:
                crimg=crimg[1:]

    screen.fill((255,255,255))
    tskip=0
    for _,t in enumerate(tiles):
        img_i= t.image if t.index in crimg else t.box
        if not t.skip:
            screen.blit(img_i,(t.col*gc.imsize+gc.mar,t.row*gc.imsize+gc.mar))
        else:
            tskip+=1
    display.flip()
    if len(crimg)==2:
        img1, img2=crimg
        if tiles[img1].name==tiles[img2].name:
            tiles[img1].skip=True
            tiles[img2].skip=True
            sleep(0.4)
            screen.blit(matched,(0,0))
            display.flip()
            sleep(0.4)
            crimg=[]
    if tskip ==len(tiles):
        run=False
print("Game Ended")
