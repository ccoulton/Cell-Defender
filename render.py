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
        if self.ent.mesh == 'sphere.mesh':
            self.gent.setMaterialName ('Examples/chrome')
        self.node.attachObject(self.gent)
        """self.animationState = ent.getAnimationState('Idle')
        self.animationState.setLoop(True)
        self.animationState.setEnabled(True)"""
        
    def tick(self, dtime):
        #----------update scene node position and orientation-----------------------------------
        self.node.setPosition(self.ent.pos)
        self.node.resetOrientation()
        self.node.yaw(ogre.Radian(self.ent.heading))
        if self.isMoving():
            pass
            #self.animationState = self.ent.getAnimationState('Walk')
        else:
            pass
            #self.animationState = self.ent.getAnimationState('Idle')
            
        if self.ent.isSelected:
            self.node.showBoundingBox(True)
        else:
            self.node.showBoundingBox(False)
        #self.animationState.addTime(dtime)
        
    def isMoving(self):
        if self.ent.speed > 0:
            return True
        else:
            return False
