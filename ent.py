# Entity class to hold information about entities for 38Engine
# Sushil Louis

from vector        import Vector3
from physics       import Physics
from render        import Renderer
import ai
from animation     import AnimationMgr
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
        self.comTypes = [ai.move, ai.intercept, ai.follow, ai.flee]
        self.isTerrain = False
        self.toRender = True
        self.isDefender = False
        self.isAttacker = False
        
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
        self.turningRate  = 0.7
        self.maxSpeed = 25
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
        self.aspectTypes = [Physics, Renderer, ai.motherShipCommandMgr]
        self.lightHeight = 1000
        self.radius = 100
        self.health = 100
#-----------------------------------------------------------------------------------------
class defender(Entity):
    def __init__(self, engine, id, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), yaw = 0, defenderNum = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'cube.mesh'
        self.uiname = 'defender' + str(id)
        self.acceleration = 55
        self.turningRate  = 1.7
        self.maxSpeed = 75
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
        self.isDefender = True
        self.defenderNum = defenderNum
        self.aspectTypes = [Physics, Renderer, ai.pathfinding]
        self.lightHeight = 500
        self.radius = 50
#-----------------------------------------------------------------------------------------
class attacker(Entity):
    Ogre_Ent = None
    animationState = None
    def __init__(self, engine, id, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'robot.mesh'
        self.uiname = 'attacker' + str(id)
        self.acceleration = 33
        self.turningRate  = 0.9
        self.maxSpeed = 50
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
        self.aspectTypes = [Physics, Renderer, ai.attackerCmdMgr, AnimationMgr]
        self.isAttacker = True
        self.radius = 20
#-----------------------------------------------------------------------------------------

class terrain(Entity):
    def __init__(self, engine, id, pos = Vector3(0,0,0), vel = Vector3(0, 0, 0), yaw = 0):
        Entity.__init__(self, engine, id, pos = pos, vel = vel, yaw = yaw)
        self.mesh = 'ogrehead.mesh'
        self.uiname = 'terrain' + str(id)
        self.acceleration = 0
        self.turningRate  = 0
        self.maxSpeed = 0
        self.desiredSpeed = 0
        self.desiredHeading = 0
        self.speed = 0
        self.heading = 0
        self.aspectTypes = [Renderer]
        self.isTerrain = True
        self.radius = 25
        

