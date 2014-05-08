# Simple Keyboard arrows based manual Control Aspect for 38Engine
# Sushil Louis

#from vector import Vector3
import utils
import math
import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
import ogre.sound.ogreoggsound as OgreOggSound


class SndMgr:

    def __init__(self, engine):
        self.index = 0
        self.sounds = []
        self.engine = engine
        self.engine.gfxMgr.root.loadPlugin("OgreOggSound")
        self.manager = OgreOggSound.OgreOggSoundManager.getSingletonPtr()
        self.manager.init()
        #self.manager = OgreAL.SoundManager()
        print "Sound Manager Constructed "
        #self.init()
        
    def init(self):
        print "Initializing Sound manager"
        #self.sndMgr = OgreAL.SoundManager()
        self.bgm = self.manager.createSound("background", "Voyager.ogg", True, True, False)
        #self.bgm.setGain(0.9)
        self.bgm.play()
        pass

    def stop(self):
        self.manager._releaseSource(self.bgm)
        self.manager.destroySound(self.bgm)

        pass

    def stopBackGround(self):
        self.bgm.pause()

    def playGameOver(self):
        self.bgm = self.manager.createSound("gameOver", "gameover.ogg", False, False, False)
        #self.bgm.setGain(0.9)
        self.bgm.play()
        
    def tick(self, dtime):
        self.manager.update(dtime)

    def playRobotDeath(self):
        self.sounds.insert(0, self.manager.createSound('death' + str(self.index), 
                                            'explosion.ogg', False, False, True))
        self.index += 1
        #self.sounds[0].setGain(0.7)
        self.sounds[0].play()

    def playRobotDeathDefender(self):
        self.sounds.insert(0, self.manager.createSound('death' + str(self.index), 
                                            'Powerup.ogg', loop = False))
        self.index += 1
        #self.sounds[0].setGain(0.7)
        self.sounds[0].play()

    def loadLevel(self, dtime):
        pass
