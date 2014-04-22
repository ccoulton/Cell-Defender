from vector import Vector3
import ogre.renderer.OGRE as ogre
import time


class GameMgr:
    def __init__(self, engine):
        self.engine = engine
        print "starting Game mgr"
        pass

    def init(self):
        self.titleScreen()
        self.loadLevel()

    def titleScreen(self):
        screen = ogre.Rectangle2D(True)
        screen.setCorners(-1.0,1.0,1.0,-1.0)
        screen.setMaterial('Examples/RustySteel')
        time.sleep(4)



    def loadLevel(self):
        self.game1()
        

    def game1(self):
        x = 0
        for entType in self.engine.entityMgr.entTypes:
            print "GameMgr Creating", str(entType)
            ent = self.engine.entityMgr.createEnt(entType, pos = Vector3(x, 0, 0))
            print "GameMgr Created: ", ent.uiname, ent.eid
            x += 300


    def tick(self, dt):
        pass

    def stop(self):
        pass
        

