from vector import Vector3
import random
import ogre.renderer.OGRE as ogre
import time


class GameMgr:
    def __init__(self, engine):
        self.engine = engine
        
        print "starting Game mgr"
        pass

    def init(self):
        self.loadLevel()
        random.seed()
        self.updateTimer = 0
        self.spawnCount = 1
        self.spawnNum = 1
        self.levelFinished = [False]

    def loadLevel(self):
        '''if self.levelFinished[] == True
            self.game2()'''
        self.game1()
        
#level 1-------------------------------
    def game1(self):
        import ent
        x = 0
        self.spawnNum = 1
        self.spawnCount = 1
        self.updateTimer = 0
        for entType in self.engine.entityMgr.entTypes:
            print "GameMgr Creating", str(entType)
            if str(entType) == 'ent.defender':
                self.engine.entityMgr.createDefenders(entType)
                print "GameMgr Created: denfenders (1-4)"
            elif str(entType) == 'ent.attacker':
                pass
            else:
                ent = self.engine.entityMgr.createEnt(entType, pos = Vector3(x, 0, 0))
                print "GameMgr Created: ", ent.uiname, ent.eid
                x += 1000
            
#level 2--------------------------------           
    def game2(self):
        x = 0
        self.spawnNum = 2
        self.spawnCount = 2
#---------------------------------------
    def spawnEnemy(self):
        if self.spawnCount %10 == 0: 
            self.spawnNum += 1
        for index in range(0,self.spawnNum):
            x = random.randint(-10, 10)
            z = random.randint(-10, 10)
            randDist = random.randint(2000, 2500)
            randomVector = Vector3(x, 0, z)
            randomVector.normalise()
            randomVector = randomVector * randDist
            randomVector = randomVector + self.engine.entityMgr.ents[0].pos
            ent = self.engine.entityMgr.createEnt(self.engine.entityMgr.entTypes[2], randomVector)
        self.spawnCount += 1
#----------------------------------------        
    def tick(self, dt):
        self.updateTimer += 1
        if self.updateTimer % 500 == 0:
        #if self.updateTimer % (1000/self.spawnCount) == 0:
            self.spawnEnemy()

    def stop(self):
        pass
        

