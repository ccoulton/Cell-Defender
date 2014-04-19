# Simple Rendering Aspect for 38Engine
# Sushil Louis

#from vector import Vector3
import utils
import math
import ogre.renderer.OGRE as ogre

class Renderer:
    def __init__(self, ent):
        self.ent = ent
        print "Rendering seting up for: ", str(self.ent)
        self.gent =  self.ent.engine.gfxMgr.sceneManager.createEntity(self.ent.uiname + "_ogreEnt", self.ent.mesh)
        self.node =  self.ent.engine.gfxMgr.sceneManager.getRootSceneNode().createChildSceneNode(self.ent.uiname + 'node', ent.pos)
        self.node.attachObject(self.gent)
        
        
    def tick(self, dtime):
        #----------update scene node position and orientation-----------------------------------
        self.node.setPosition(self.ent.pos)
        self.node.resetOrientation()
        self.node.yaw(ogre.Radian(self.ent.heading))
        if self.ent.isSelected:
            self.node.showBoundingBox(True)
        else:
            self.node.showBoundingBox(False)

