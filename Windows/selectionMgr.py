# Selection Manager tracks currently selected ent, selected group of ents, ...
import ogre.io.OIS as OIS # needed to check keyboard

class SelectionMgr:
    def __init__(self, engine):
        self.engine = engine
        pass

    def init(self):
        self.selectedEnts = []
        self.selectedEntIndex = self.engine.entityMgr.nEnts;
        self.selectedDefenderIndex = self.engine.entityMgr.nDefenders;
        self.selectedEnt = None
        self.keyboard = self.engine.inputMgr.keyboard
        self.toggle = 0.1

    def tick(self, dtime):
        self.keyboard.capture()
        if self.toggle >= 0:
            self.toggle -= dtime

        if self.toggle < 0 and self.keyboard.isKeyDown(OIS.KC_TAB):
            # Update the toggle timer.
            self.toggle = 0.1
            if self.keyboard.isKeyDown(OIS.KC_LSHIFT):
                self.addNextDefender()
            else:
                self.selectNextDefender()
            #print "Selected Ent : ", self.selectedEnt.uiname, self.selectedEntIndex

    def stop(self):
        self.selectedEnt = None
        self.selectedEnts = []
        self.selectedEntIndex = -1
        pass

#------------------------------------------------------------------------------------------

    def updateCurrentSelection(self, isSelected):
        for ent in self.selectedEnts:
            ent.isSelected = isSelected
        if not isSelected:
            self.selectedEnts = []

    def selectEnt(self, ent):
        self.updateCurrentSelection(False) #First clear currentSelection
        self.selectedEnts = []             #also clear list
        self.addSelectedEnt(ent)           #Now add ent


    def addSelectedEnt(self, ent):
        self.selectedEnt = ent
        self.selectedEnts.append(ent)
        self.selectedEntIndex = ent.eid
        self.selectedEnt.isSelected = True
        
    def killSelection(self):
        self.updateCurrentSelection(False)

    def selectNextEnt(self):
        self.selectedEntIndex = self.getNextSelectedEntIndex(self.selectedEntIndex)
        self.selectEnt(self.engine.entityMgr.ents[self.selectedEntIndex])
        return 

    def addNextEnt(self):
        self.selectedEntIndex = self.getNextSelectedEntIndex(self.selectedEntIndex)
        self.addSelectedEnt(self.engine.entityMgr.ents[self.selectedEntIndex])
        return 

###########################################################
    def selectNextDefender(self):
        self.selectedDefenderIndex = self.getNextSelectedDefenderIndex(self.selectedDefenderIndex)
        self.selectEnt(self.engine.entityMgr.defenders[self.selectedDefenderIndex])
        return 

    def addNextDefender(self):
        self.selectedDefenderIndex = self.getNextSelectedDefenderIndex(self.selectedDefenderIndex)
        self.addSelectedEnt(self.engine.entityMgr.defenders[self.selectedDefenderIndex])
        return 

    def getNextSelectedDefenderIndex(self, index):
        if index >= self.engine.entityMgr.nDefenders - 1:
            index = 0
        else:
            index = index + 1
        return index

###########################################################
    def getNextSelectedEntIndex(self, index):
        if index >= self.engine.entityMgr.nEnts - 1:
            index = 0
        else:
            index = index + 1
        return index

    def getPrimarySelection(self):
        return self.selectedEnts[0]

#------------------------------------------------------------------------------------------
