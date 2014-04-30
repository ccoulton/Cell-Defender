import ogre.renderer.OGRE as ogre
import ogre.io.OIS as OIS
from label import Label
from panel import Panel

class WidgetMgr:

    def __init__(self,engine):
        self.engine = engine

        width  = self.engine.gfxMgr.renderWindow.getWidth()
        height = self.engine.gfxMgr.renderWindow.getHeight()

        self.UIpanel = Panel(name = "UIPanel1", pos = (0,0), dim = (width, height), material = "CD/UI")

        self.textPanel = Panel(name = "textPanel1", pos = (10,960))
        self.label = Label(caption = "Mothership Health:", color = (0,0,.5))
        self.textPanel.getPanel().addChild(self.label.getTextArea())
    
        self.textPanel = Panel(name = "textPanel2", pos = (500,960))
        self.label = Label(caption = "Robots Destroyed:", color = (0,0,.5), pos = (500,0))
        self.textPanel.getPanel().addChild(self.label.getTextArea())

        self.mothershipHealth = Panel(name = "textPanel3", pos = (100,960))
        self.label = Label(caption = "100", color = (0,0,.5), pos = (0,0))
        self.textPanel.getPanel().addChild(self.label.getTextArea())

        self.robotsDestroyed = Panel(name = "textPanel4", pos = (1000,960))
        self.label = Label(caption = "0", color = (0,0,.5), pos = (0,0))
        self.textPanel.getPanel().addChild(self.label.getTextArea())
        

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

