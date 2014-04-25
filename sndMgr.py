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
        self.engine = engine
        #self.engine.gfxMgr.root.loadPlugin("OgreOggSound")
        self.manager = OgreAL.SoundManager()
        print "Sound Manager Constructed "
        #self.init()
        
    def init(self):
        print "Initializing Sound manager"
        #self.sndMgr = OgreAL.SoundManager()
        self.bgm = self.manager.createSound("background", "Voyager.ogg")
        self.bgm.setGain(0.8)
        self.bgm.play()
        pass

    def stop(self):
        self.manager._releaseSource(self.bgm)
        self.manager.destroySound(self.bgm)

        pass
        
    def tick(self, dtime):
        pass

    def loadLevel(self, dtime):
        pass