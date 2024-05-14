'''

written by Emily Pollacchi
  	file name alignOrigin
  	Copyright (C) 2024 by Emily Pollacchi
  	epollacchi@gmail.com

'''

import maya.cmds as cmds

def alignOrigin():

    #Select objects
    selObjs = cmds.ls(selection=True)
	
    #Check for selection
    if not selObjs:
        cmds.error("No objects selected.")
    
    #move pivot to the bottom
    for Objs in selObjs:
        bbox = cmds.exactWorldBoundingBox(Objs)
        bottom = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]
        cmds.xform(Objs, piv=bottom, ws=True)
    
    #move object to the origin
    for Objs in selObjs:
        cmds.move(0,0,0, Objs, rpr=True, absolute=True)
        
    #freeze transformations
    for Objs in selObjs:
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        
    #delete non-deformer history
    for Objs in selObjs:
        cmds.BakeNonDefHistory()

alignOrigin()