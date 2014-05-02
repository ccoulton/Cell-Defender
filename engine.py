# 381 main engine
import threading

class Engine(object):
    '''
    The root of the global manager tree
    '''

    def __init__(self):
        self.delay = 1000
        self.studioName = "../media/materials/textures/wankershimStartScreen.gif"
        self.gameTitleScreen = 'TextureStuff/green.gif'

    def init(self):
        import splashScreen
        self.splash = splashScreen.SplashScreen(self.delay, self.studioName)
        self.splash.start()

        import entityMgr
        self.entityMgr = entityMgr.EntityMgr(self)
        self.entityMgr.init()
        self.keepRunning = True;

        import gfxMgr
        self.gfxMgr = gfxMgr.GfxMgr(self)
        self.gfxMgr.init()

        import widgetMgr
        self.widgetMgr = widgetMgr.WidgetMgr(self)
        self.widgetMgr.init()
        
        import sndMgr
        self.sndMgr = sndMgr.SndMgr(self)
        self.sndMgr.init()

        import netMgr
        self.netMgr = netMgr.NetMgr(self)
        self.netMgr.init()

        import inputMgr
        self.inputMgr = inputMgr.InputMgr(self)
        self.inputMgr.init()

        import selectionMgr
        self.selectionMgr = selectionMgr.SelectionMgr(self)
        self.selectionMgr.init()

        import controlMgr
        self.controlMgr = controlMgr.ControlMgr(self)
        self.controlMgr.init()

        import gameMgr
        self.gameMgr = gameMgr.GameMgr(self)
        self.gameMgr.init()
        self.Endgame = False

    def stop(self):
        self.inputMgr.stop()
        self.gfxMgr.stop()
        self.selectionMgr.stop()
        self.gameMgr.stop()
        self.controlMgr.stop()
        self.keepRunning = False

    def run(self):
        import time
        import ogre.renderer.OGRE as ogre
        weu = ogre.WindowEventUtilities() # Needed for linux/mac
        weu.messagePump()                 # Needed for linux/mac

        self.splash.join()

        import titleSplash
        self.titleSplashScreen = titleSplash.TitleSplashScreen(self.gameTitleScreen)        
        
        self.oldTime = time.time()        
        self.runTime = 0
        while (self.keepRunning):
            now = time.time() # Change to time.clock() for windows
            dtime = now - self.oldTime
            self.oldTime = now

            self.entityMgr.tick(dtime)
            self.gfxMgr.tick(dtime)
            self.widgetMgr.tick(dtime)
            self.sndMgr.tick(dtime)
            self.netMgr.tick(dtime)
            self.inputMgr.tick(dtime)
            self.selectionMgr.tick(dtime)
            self.controlMgr.tick(dtime)
            self.gameMgr.tick(dtime)
            
            self.runTime += dtime
        
            weu.messagePump()             # Needed for linux/mac
            time.sleep(0.001)
            if self.Endgame == True:
                self.stop()
        print "381 Engine exiting..."
        thing = True
        self.endScreen = titleSplash.EndScreen(self.gameTitleScreen, thing)

        #time.sleep(5) # game ended, wait for a few seconds
    
