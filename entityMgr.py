from vector import Vector3

SPAWN_DISTANCE = 500

class EntityMgr:
    def __init__(self, engine):
        print "starting ent mgr"
        self.engine = engine
                
    def init(self):
        self.ents = {}
        self.nEnts = 0
        self.defenders = []
        self.nDefenders = 0
        import ent
        self.entTypes = [ent.motherShip, ent.defender, ent.attacker, ent.terrain]
        self.terrainTypes = []
        self.rEnts = []
        #self.entTypes = [ent.CIGARETTE, ent.CVN68, ent.DDG51, ent.BOAT, ent.BOAT2, ent.SLEEK,  ent.ALIENSHIP, ent.SAILBOAT, ent.MONTEREY]


    def createEnt(self, entType, pos = Vector3(0,0,0), yaw = 0):
        ent = entType(self.engine, self.nEnts, pos = pos, yaw = yaw)
        print "EntMgr created: ", ent.uiname, ent.eid, self.nEnts
        ent.init()
        self.ents[self.nEnts] = ent;
        self.nEnts = self.nEnts + 1
        return ent


    def createDefender(self, entType, pos = Vector3(0,0,0), defenderNum = 0):
        ent = entType(self.engine, self.nEnts, pos = pos, defenderNum = defenderNum)
        print "EntMgr created: ", ent.uiname, ent.eid, self.nEnts
        ent.init()
        self.ents[self.nEnts] = ent;
        self.nEnts = self.nEnts + 1
        return ent



    def createDefenders(self, entType):
        defender1 = self.createDefender(entType, pos = Vector3(0,0,-SPAWN_DISTANCE), defenderNum = 1)
        defender1.defenderNum = 0
        defender2 = self.createDefender(entType, pos = Vector3(SPAWN_DISTANCE,0,0) , defenderNum = 2)
        defender3 = self.createDefender(entType, pos = Vector3(0,0,SPAWN_DISTANCE) , defenderNum = 3)
        defender4 = self.createDefender(entType, pos = Vector3(-SPAWN_DISTANCE,0,0), defenderNum = 4)

        defender1.defenderNum = 1
        defender2.defenderNum = 2
        defender3.defenderNum = 3
        defender4.defenderNum = 4

        self.defenders.append(defender1)
        self.nDefenders = self.nDefenders + 1
        self.defenders.append(defender2)
        self.nDefenders = self.nDefenders + 1
        self.defenders.append(defender3)
        self.nDefenders = self.nDefenders + 1
        self.defenders.append(defender4)
        self.nDefenders = self.nDefenders + 1


    def tick(self, dt):
        for rement in self.rEnts:
            self.ents.remove(rement)
            #Ogre Forum link to remove ents and movable things
            #http://www.ogre3d.org/forums/viewtopic.php?f=2&t=53647&start=0
        self.rEnts = []
        for eid, ent in self.ents.iteritems():
            ent.tick(dt)
        

