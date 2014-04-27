import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS

class WidgetMgr:

    def __init__(self,engine):
        self.engine = engine
        self.overlayManager = ogre.OverlayManager.getSingleton()
        self.pid         = "UIPanel" + str(0)
        self.panel       = self.overlayManager.createOverlayElement("Panel", self.pid)
        self.panel.setMetricsMode(ogre.GMM_PIXELS)#RELATIVE_ASPECT_ADJUSTED)
        self.panel.setPosition(0, 0)
        width  = self.engine.gfxMgr.renderWindow.getWidth()
        height = self.engine.gfxMgr.renderWindow.getHeight() # VERY IMPORTANT or rayscene queries fail
        self.panel.setDimensions(width, height)        
        self.panel.setMaterialName("CD/UI")
        self.panel.show()

        self.id = "MainUI"
        self.overlayName = "UIOverlay" + str(0)
        self.overlay     = self.overlayManager.create(self.overlayName)
        self.overlay.add2D(self.panel)
        self.overlay.show()
        self.panel.show()


    def init(self):
        pass

    def show(self):
        self.overlay.show()
        self.panel.show()

    def hide(self):
        self.panel.hide()
        self.overlay.hide()

    def render(self):
        pass

    def tick(self, dtime):
        pass

'''class FramerateWidget:

    def __init__(self, engine, name = "Framerate: ", pos = (1, 1), size = (100, 13)):
        self.engine = engine
        self.label = Label(engine, caption = name, pos = (0,0), size = size)
        self.addItem(self.label)
        self.show()
        self.label.show()
        
    def tick(self, dtime):
        stats = self.engine.gfxMgr.renderWindow.getStatistics()
        self.label.setCaption("Framerate: %5i" % stats.avgFPS)

    def render(self):
        #print "panel.show: ", self.posx, ", ", self.posy
        #self.show()
        #self.label.show()
        pass'''

