from vector import Vector3


class EntityMgr:
    def __init__(self, engine):
        print "starting ent mgr"
        self.engine = engine
                
    def init(self):
        self.ents = {}
        self.nEnts = 0
        import ent
        self.entTypes = [ent.motherShip, ent.defender, ent.attacker, ent.terrain]
        self.terrainTypes = []
        #self.entTypes = [ent.CIGARETTE, ent.CVN68, ent.DDG51, ent.BOAT, ent.BOAT2, ent.SLEEK,  ent.ALIENSHIP, ent.SAILBOAT, ent.MONTEREY]



    def createEnt(self, entType, pos = Vector3(0,0,0), yaw = 0):
        ent = entType(self.engine, self.nEnts, pos = pos, yaw = yaw)
        print "EntMgr created: ", ent.uiname, ent.eid, self.nEnts
        ent.init()
        self.ents[self.nEnts] = ent;
        self.nEnts = self.nEnts + 1
        return ent


    def tick(self, dt):
        for eid, ent in self.ents.iteritems():
            ent.tick(dt)
        

