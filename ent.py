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


# ENTITY TYPES
#-----------------------------------------------------------------------------------------
class motherShip(Entity):
    def __init__(self, engine, id, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'sphere.mesh'
        self.uiname = 'motherShip' + str(id)
        self.acceleration = 2
        self.turningRate  = 0.1
        self.maxSpeed = 25
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
#-----------------------------------------------------------------------------------------
class defender(Entity):
    def __init__(self, engine, id, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'cube.mesh'
        self.uiname = 'defender' + str(id)
        self.acceleration = 5
        self.turningRate  = 0.3
        self.maxSpeed = 55
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
#-----------------------------------------------------------------------------------------
class attacker(Entity):
    def __init__(self, engine, id, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'robot.mesh'
        self.uiname = 'attacker' + str(id)
        self.acceleration = 5
        self.turningRate  = 0.3
        self.maxSpeed = 55
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
#-----------------------------------------------------------------------------------------

