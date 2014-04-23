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

        if self.ent.isDefender == True:
            if self.ent.defenderNum == 1:
                self.gent.setMaterialName('Examples/oneDefender')
            elif self.ent.defenderNum == 2:
                self.gent.setMaterialName('Examples/twoDefender')
            elif self.ent.defenderNum == 3:
                self.gent.setMaterialName('Examples/threeDefender')
            elif self.ent.defenderNum == 4:
                self.gent.setMaterialName('Examples/fourDefender')
        elif self.ent.uiname == 'motherShip0':
                self.gent.setMaterialName('Examples/mothership')

        self.node.attachObject(self.gent)
    
    def checkPos(self):
        raySceneQuery = self.ent.engine.gfxMgr.sceneManager.createRayQuery(ogre.Ray())
        updateRay = ogre.Ray()
        updateRay.setOrigin(self.ent.pos + ogre.Vector3(0,5,0))
        updateRay.setDirection(ogre.Vector3().NEGATIVE_UNIT_Y)
        raySceneQuery.Ray = updateRay
        for queryResult in raySceneQuery.execute():
            if queryResult.worldFragment is not None:
                self.ent.y = self.ent.y - queryResult.distance + 40
                break
        
        
    def tick(self, dtime):
        #----------update scene node position and orientation-----------------------------------
        if self.ent.toRender == True:
            #self.checkPos()
            self.node.setPosition(self.ent.pos)
            self.node.resetOrientation()
            self.node.yaw(ogre.Radian(self.ent.heading))
            if self.ent.isSelected:
                self.node.showBoundingBox(True)
            else:
                self.node.showBoundingBox(False)
        
        elif self.ent.aspects[2].deathtimer >= 20:
            pass
        
        else:
            pass
