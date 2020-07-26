import os
imsize=128
scsize=512
numside=4
numtotal=16
mar=4
assetdir='assets'
assetfile=[x for x in os.listdir(assetdir) if x[-3:].lower()=="png"]
assert len(assetfile)==8
#Rahul Choudhary
