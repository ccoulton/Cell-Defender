# Graphics manager
import ogre.renderer.OGRE as ogre

# Manages graphics. Creates graphics, scene, scene nodes, renders scene
class GfxMgr:
    def __init__(self, engine):
        self.engine = engine
        pass

    def init(self):
        self.createRoot()
        self.defineResources()
        self.setupRenderSystem()
        self.createRenderWindow()
        self.initializeResourceGroups()
        self.setupScene()


    def tick(self, dtime):
        self.root.renderOneFrame()

    # The Root constructor for the ogre
    def createRoot(self):
        self.root = ogre.Root()
 
    # Here the resources are read from the resources.cfg
    def defineResources(self):
        cf = ogre.ConfigFile()
        cf.load("resources.cfg")
 
        seci = cf.getSectionIterator()
        while seci.hasMoreElements():
            secName = seci.peekNextKey()
            settings = seci.getNext()
 
            for item in settings:
                typeName = item.key
                archName = item.value
                ogre.ResourceGroupManager.getSingleton().addResourceLocation(archName, typeName, secName)
 
    # Create and configure the rendering system (either DirectX or OpenGL) here
    def setupRenderSystem(self):
        self.root.showConfigDialog()
        if not self.root.restoreConfig() and not self.root.showConfigDialog():
            raise Exception("User canceled the config dialog -> Application.setupRenderSystem()")
 
 
    # Create the render window
    def createRenderWindow(self):
        self.root.initialise(True, "Its always been Wankershim Games Engine")
 
    # Initialize the resources here (which were read from resources.cfg in defineResources()
    def initializeResourceGroups(self):
        ogre.TextureManager.getSingleton().setDefaultNumMipmaps(5)
        ogre.ResourceGroupManager.getSingleton().initialiseAllResourceGroups()
 
    # Now, create a scene here. Three things that MUST BE done are sceneManager, camera and
    # viewport initializations
    def setupScene(self):
        self.sceneManager = self.root.createSceneManager(ogre.ST_GENERIC, "Default SceneManager")

        self.camera = self.sceneManager.createCamera("Camera")
        self.camera.nearClipDistance = 5

        self.viewPort = self.root.getAutoCreatedWindow().addViewport(self.camera)
        self.sceneManager.ambientLight = .8, .8, .8
 
        # Setup a ground plane.
        #plane = ogre.Plane ((0, 1, 0), -100)
        self.groundPlane = ogre.Plane ((0, 1, 0), -7)
        meshManager = ogre.MeshManager.getSingleton ()
        meshManager.createPlane ('Ground', 'General', self.groundPlane,
                                     10000, 10000, 50, 50, True, 1, 50, 50, (0, 0, 1))
        ent = self.sceneManager.createEntity('GroundEntity', 'Ground')
        self.sceneManager.getRootSceneNode().createChildSceneNode ().attachObject (ent)
        ent.setMaterialName ('Examples/BeachStones') #OceanCg
        ent.castShadows = False
        self.sceneManager.setSkyBox (True, "Examples/SpaceSkyBox", 50000, False)
        self.camYawNode = self.sceneManager.getRootSceneNode().createChildSceneNode('CamNode1',
                                                                    #(-400, 200, 400))
                                                                    (0, 1000, 1000))
        #node.yaw(ogre.Degree(-45))
        self.camYawNode.yaw(ogre.Degree(0))
        self.camera.lookAt((0,-50,0))
        self.camPitchNode = self.camYawNode.createChildSceneNode('PitchNode1')
        self.camPitchNode.attachObject(self.camera)
 
 
     # In the end, clean everything up (= delete)
    #def cleanUp(self):
    def stop(self):
        del self.root

