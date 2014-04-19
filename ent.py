# Entity class to hold information about entities for 38Engine
# Sushil Louis

from vector        import Vector3
from physics       import Physics
from render        import Renderer
import ai

#-----------------------------------------------------------------------------------------
class Entity:
    pos  = Vector3(0, 0, 0)
    vel  = Vector3(0, 0, 0)
    yaw  = 0

    aspectTypes = [Physics, Renderer, ai.commandMgr]
    
    def __init__(self, engine, id, pos = Vector3(0,0,0), mesh = 'robot.mesh', vel = Vector3(0, 0, 0), yaw = 0):
        self.engine = engine
        self.uiname = "Robot" + str(id)
        self.eid = id
        self.pos = pos
        self.vel = vel
        self.mesh = mesh
        self.deltaSpeed = 10
        self.deltaYaw   = 0.3
        self.speed = 0.0
        self.heading = 0.0
        self.aspects = []
        self.isSelected = False
        self.comTypes = [ai.move, ai.intercept, ai.follow]

    def init(self):
        self.initAspects()

    def initAspects(self):
        for aspType in self.aspectTypes:
            self.aspects.append(aspType(self))
        
    def tick(self, dtime):
        for aspect in self.aspects:
            aspect.tick(dtime)

    def __str__(self):
        x = "--------------------\nEntity: %s \nPos: %s, Vel: %s,  mesh = %s\nSpeed: %f, Heading: %f, desiredSpeed: %f, desiredHeading: %f" % (self.uiname, str(self.pos), str(self.vel), self.mesh, self.speed, self.heading, self.desiredSpeed, self.desiredHeading)
        return x
#-----------------------------------------------------------------------------------------
class CVN68(Entity):
    def __init__(self, engine, id, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'cvn68.mesh'
        self.uiname = 'CVN68' + str(id)
        self.acceleration = 2
        self.turningRate  = 0.1
        self.maxSpeed = 40
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
#-----------------------------------------------------------------------------------------
class CIGARETTE(Entity):
    def __init__(self, engine, id, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'cigarette.mesh'
        self.uiname = 'CIGARETTE' + str(id)
        self.acceleration  = 10
        self.turningRate   = 0.25
        self.maxSpeed = 40
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
#-----------------------------------------------------------------------------------------
class MONTEREY(Entity):
    def __init__(self, engine, id, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = '3699_Monterey_189_92.mesh'
        self.uiname = 'MONTEREY' + str(id)
        self.acceleration = 5
        self.turningRate = 0.2
        self.maxSpeed = 35
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
#-----------------------------------------------------------------------------------------
class JETSKI(Entity):
    def __init__(self, engine, id, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = '4685_Personal_Watercr.mesh'
        self.uiname = 'JETSKI' + str(id)
        self.acceleration = 7
        self.turningRate = 0.35
        self.maxSpeed = 20
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
#-----------------------------------------------------------------------------------------
class SAILBOAT(Entity):
    def __init__(self, engine, id, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'sailboat.mesh'
        self.uiname = 'SAILBOAT' + str(id)
        self.acceleration = 3
        self.turningRate = 0.2
        self.maxSpeed = 10
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
#-----------------------------------------------------------------------------------------
class SLEEK(Entity):
    def __init__(self, engine, id, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'sleek.mesh'
        self.uiname = 'SLEEK' + str(id)
        self.acceleration = 4
        self.turningRate = 0.2
        self.maxSpeed = 30
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
#-----------------------------------------------------------------------------------------
class BOAT(Entity):
    def __init__(self, engine, id, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'boat.mesh'
        self.uiname = 'BOAT' + str(id)
        self.acceleration = 5
        self.turningRate = 0.2
        self.maxSpeed = 30
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
#-----------------------------------------------------------------------------------------
class DDG51(Entity):
    def __init__(self, engine, id, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'ddg51.mesh'
        self.uiname = 'DDG51' + str(id)
        self.acceleration = 5
        self.turningRate = 0.2
        self.maxSpeed = 32
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
#-----------------------------------------------------------------------------------------
class ALIENSHIP(Entity):
    def __init__(self, engine, id, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'alienship.mesh'
        self.uiname = 'ALIEN' + str(id)
        self.acceleration  = 10
        self.turningRate   = 0.3
        self.maxSpeed = 60
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
#-----------------------------------------------------------------------------------------
class BOAT2(Entity):
    def __init__(self, engine, id, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = '5086_Boat.mesh'
        self.uiname = 'BOAT2' + str(id)
        self.acceleration = 5
        self.turningRate = 0.25
        self.maxSpeed = 30
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
#-----------------------------------------------------------------------------------------
