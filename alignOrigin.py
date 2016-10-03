'''

written by Emily Pollacchi
  	file name alignOrigin
  	Copyright (C) 2016 by Emily Pollacchi
  	epollacchi@gmail.com

'''

import maya.cmds as mc

def alignOrigin():

    #Select objects
    selObjs = mc.ls(selection=True)
    
    #move pivot to the bottom
    for Objs in selObjs:
        bbox = mc.exactWorldBoundingBox(Objs)
        bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
        mc.xform(Objs, piv=bottom, ws=True)
    
    #move object to the origin
    for Objs in selObjs:
        mc.move(0,0,0, Objs, rpr=True, absolute=True)
        
    #freeze transformations
    for Objs in selObjs:
        mc.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        
    #delete non-deformer history
    for Objs in selObjs:
        mc.BakeNonDefHistory()

alignOrigin()