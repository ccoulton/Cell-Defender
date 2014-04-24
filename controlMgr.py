# Simple Keyboard arrows based manual Control Aspect for 38Engine
# Sushil Louis

#from vector import Vector3
import utils
import math
import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
import ai

class ControlMgr:
    toggleMax = 0.1
    def __init__(self, engine):
        self.engine = engine
        print "Control Manager Constructed "
        
    def init(self):
        self.keyboard = self.engine.inputMgr.keyboard
        self.toggle = self.toggleMax
        pass

    def stop(self):
        pass
        
    def addInter(self, target):
   	    for selectedEnt in self.engine.selectionMgr.selectedEnts:
   	        selectedEnt.aspects[2].addCom(ai.intercept(selectedEnt, target))
   	        
    def addFlee(self, target):
        for selectedEnt in self.engine.selectionMgr.selectedEnts:
            selectedEnt.aspects[2].addCom(ai.flee(selectedEnt, target))
            
    def addFollow(self, target):
        for selectedEnt in self.engine.selectionMgr.selectedEnts:
            selectedEnt.aspects[2].addCom(ai.follow(selectedEnt, target))
   			
    def addMove(self, position):
        for selectedEnt in self.engine.selectionMgr.selectedEnts:
            selectedEnt.aspects[2].addCom(ai.move(selectedEnt, position))
   			
    def clearComs(self): #clears command list and sets speed and turning to 0
        for selectedEnt in self.engine.selectionMgr.selectedEnts:
            selectedEnt.aspects[2].clearComs()
            selectedEnt.desiredSpeed = 0
            selectedEnt.desiredHeading = selectedEnt.heading
   			
    def tick(self, dtime):
        #----------make selected ent respond to keyboard controls-----------------------------------
        if self.toggle >= 0:
            self.toggle = self.toggle - dtime

        if  self.toggle < 0:
            self.keyboard.capture()
            for selectedEnt in self.engine.selectionMgr.selectedEnts:
            # Speed Up
                if self.keyboard.isKeyDown(OIS.KC_UP):
                    self.toggle = self.toggleMax
                    selectedEnt.desiredSpeed = utils.clamp(selectedEnt.desiredSpeed + selectedEnt.deltaSpeed, 0, selectedEnt.maxSpeed)
                    print "Speeding UP", str(selectedEnt), selectedEnt.desiredSpeed
            # Slow down
                if  self.keyboard.isKeyDown(OIS.KC_DOWN):
                    self.toggle = self.toggleMax
                    selectedEnt.desiredSpeed = utils.clamp(selectedEnt.desiredSpeed - selectedEnt.deltaSpeed, 0, selectedEnt.maxSpeed)
                    print "Slowing down", str(selectedEnt), selectedEnt.desiredSpeed
            # Turn Left.
                if  self.keyboard.isKeyDown(OIS.KC_LEFT):
                    self.toggle = self.toggleMax
                    selectedEnt.desiredHeading += selectedEnt.deltaYaw
                    selectedEnt.desiredHeading = utils.fixAngle(selectedEnt.desiredHeading)
                    print "Turn left", str(selectedEnt), selectedEnt.desiredHeading
            # Turn Right.
                if  self.keyboard.isKeyDown(OIS.KC_RIGHT):
                    self.toggle = self.toggleMax
                    selectedEnt.desiredHeading -= selectedEnt.deltaYaw
                    selectedEnt.desiredHeading = utils.fixAngle(selectedEnt.desiredHeading)
                    print "Turn right", str(selectedEnt), selectedEnt.desiredHeading
				
				
