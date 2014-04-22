from vector import Vector3
<<<<<<< .mine
import random
=======
import ogre.renderer.OGRE as ogre
import time
>>>>>>> .r7

class GameMgr:
    def __init__(self, engine):
        self.engine = engine
        
        print "starting Game mgr"
        pass

    def init(self):
        self.titleScreen()
        self.loadLevel()
<<<<<<< .mine
        random.seed()
        updateTimer = 0
        
=======

    def titleScreen(self):
        screen = ogre.Rectangle2D(True)
        screen.setCorners(-1.0,1.0,1.0,-1.0)
        screen.setMaterial('Examples/RustySteel')
        time.sleep(4)

>>>>>>> .r7


    def loadLevel(self):
        self.game1()
        

    def game1(self):
        x = 0
        for entType in self.engine.entityMgr.entTypes:
            print "GameMgr Creating", str(entType)
            ent = self.engine.entityMgr.createEnt(entType, pos = Vector3(x, 0, 0))
            print "GameMgr Created: ", ent.uiname, ent.eid
            x += 300

    def spawnEnemy(self):
        x = random.randint(-10, 10)
        z = random.randint(-10, 10)
        randomVector = Vector3(x, 0, z)
        randomVector.normalise()
        randomVector = randomVector * 1000
        randomVector = randomVector + self.engine.entityMgr.ents[0].pos
        ent = self.engine.entityMgr.createEnt(ent.attacker, randomVector)
        
    def tick(self, dt):
        updateTimer += 1
        if updateTimer %500 == 0
            self.spawnEnemy()

    def stop(self):
        pass
        

