#loads Images and boxes
import os
import random
import game_config as gc 
from pygame import image,transform
acount=dict((a,0) for a in gc.assetfile)
def avanimals():
    return [a for a,c in acount.items() if c<2]
class Animal:
    def __init__(self,index):
        self.index=index
        self.row=index//gc.numside
        self.col=index%gc.numside
        self.name=random.choice(avanimals())
        acount[self.name]+=1
        self.impath=os.path.join(gc.assetdir,self.name)
        self.image=image.load(self.impath)
        self.image=transform.scale(self.image,(gc.imsize-2*gc.mar,gc.imsize-2*gc.mar))
        self.box = self.image.copy()
        self.box.fill((200,200,200))
        self.skip=False

        
