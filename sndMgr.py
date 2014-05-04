# Simple Keyboard arrows based manual Control Aspect for 38Engine
# Sushil Louis

#from vector import Vector3
import utils
import math
import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
import ogre.sound.OgreAL as OgreAL


class SndMgr:

    def __init__(self, engine):
        self.index = 0
        self.engine = engine
        #self.engine.gfxMgr.root.loadPlugin("OgreOggSound")
        self.manager = OgreAL.SoundManager()
        print "Sound Manager Constructed "
        #self.init()
        
    def init(self):
        print "Initializing Sound manager"
        #self.sndMgr = OgreAL.SoundManager()
        self.bgm = self.manager.createSound("background", "Voyager.ogg", loop = True)
        self.bgm.setGain(0.9)
        self.bgm.play()
        pass

    def stop(self):
        self.manager._releaseSource(self.bgm)
        self.manager.destroySound(self.bgm)

        pass
        
    def tick(self, dtime):
        pass

    def playRobotDeath(self):
        newSound = self.manager.createSound('death' + str(self.index), 
                                            'explosion.ogg', loop = False)
        self.index += 1
        newSound.setGain(0.7)
        newSound.play()

    def loadLevel(self, dtime):
        pass
