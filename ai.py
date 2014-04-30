from vector	 import Vector3
import math

def smallest(dist1, dist2):
    if dist1 > dist2:
        return dist2
    return dist1

def checkDist(distance, seperation):
	if distance <= seperation:
		return True
	else:
		return False

def diffDist(pos1, pos2):
	ret = 0
	ret += pow((pos2.x - pos1.x),2)
	ret += pow((pos2.z - pos1.z),2)
	return ret
	
class commandMgr:

    def __init__(self, Ent):
		self.Ent = Ent
		self.commands = []
		
    def tick(self, dTime):
		if len(self.commands) > 0:
			if self.commands[0].finished == True:
				self.comFinished()
			else:
				self.commands[0].tick(dTime)		
		
		
    def addCom(self, comType):
		self.commands.append(comType)
	
    def comFinished(self):
        if len(self.commands) > 0:
            self.commands.pop(0)
            self.Ent.desiredSpeed = 0
	
    def clearComs(self):
        self.commands[:] = []

class pathfinding(commandMgr):
    terrainList = []
    def __init__(self, Ent):
	    self.Ent = Ent
	    self.terrainList = self.Ent.engine.entityMgr.terrain
	    self.commands = []
	    self.commands.append(move(self.Ent, self.Ent.pos))
	    self.commands.append(flee(self.Ent, self.terrainList[0]))

    def clearComs(self):
	    pass

    def addCom(self, comType):
	    self.commands[0] = comType

    def comFinished(self):
	    self.commands[0] = move(self.Ent, self.Ent.pos)
	
    def tick(self, dTime):
    	
        fleeVectors = Vector3(0,0,0)
        objectiveVector = self.commands[0].findVector()
        collideDist = pow((self.Ent.radius + self.commands[1].target.radius),2)
        for TerrainObj in self.Ent.engine.entityMgr.terrain:
            if diffDist(self.Ent.pos, TerrainObj.pos) <= 2*collideDist:
                print "check flee"
                self.commands[1].changeTar(TerrainObj)
                diff = self.commands[1].findVector()
                fleeAngle = math.atan2(diff.z, -diff.x)
                fleeVectors.x += math.cos(fleeAngle)
                fleeVectors.z +=-math.sin(fleeAngle)	
        print fleeVectors
        fleeVectors = fleeVectors*self.Ent.speed
        objectiveVector += fleeVectors
        self.Ent.desiredHeading = math.atan2(-objectiveVector.z, objectiveVector.x)
        self.commands[0].checkStop()
        
class motherShipCommandMgr(commandMgr):

    def __init__(self, Ent):
        self.Ent = Ent
        self.commands = [move(self.Ent, Vector3(0,0,500)), move(self.Ent, Vector3(500,0,500)), move(self.Ent, Vector3(500,0,-500)), move(self.Ent, Vector3(0,0,-500)), move(self.Ent, Vector3(0,0,0)) ]

    def addCom(self, comType):
        pass

    def clearComs(self):
        pass

class attackerCmdMgr(commandMgr):
    
    def __init__(self, Ent):
        self.Ent = Ent
        self.target = self.Ent.engine.entityMgr.ents[0]
        self.commands = [intercept(self.Ent, self.target)]
        self.deathtimer = 0
    
    def addCom(self, comType):
        pass
    
    def clearComs(self):
        pass
          
    def tick(self, dTime):
        if len(self.commands) > 0:
            if self.commands[0].finished == True:
                self.comFinished()
            else:
            	self.checkTarget()
                self.commands[0].tick(dTime)
        elif len(self.commands) == 0:
            self.deathtimer +=1
            if self.deathtimer == 10:
                self.Ent.toRender == False
                  
    def checkTarget(self):
        dist = diffDist(self.Ent.pos, self.target.pos)
        if dist < 12000:
        	#Mothership struck
        	self.comFinished
        	self.commands[0].finished = True
        	self.target.health -= 10
        	self.Ent.engine.widgetMgr.healthLabel.setCaption(str(self.target.health))
        for defender in self.Ent.engine.entityMgr.defenders:
            currentDist = diffDist(self.Ent.pos, defender.pos)
            if currentDist < 4000:
            	#Defender struck
                self.comFinished
                self.commands[0].finished = True
class Commands:
	
	def __init__(self, Ent):
		self.Ent = Ent
		self.commands = []
		self.finished = False
		
		
	def tick(self, dTime):
		if len(self.commands) > 0:
			self.commands[0].tick(dTime)
			
class move(Commands):

    def __init__(self, currEnt, desiredPoint = Vector3(0,0,0)):
        Commands.__init__(self, currEnt)
        self.currEnt = currEnt
        self.desiredPoint = desiredPoint
    
    def findVector(self):
        return (self.desiredPoint - self.currEnt.pos)
    
    def checkStop(self):
        stopDist = 1000
        dist = diffDist(self.currEnt.pos, self.desiredPoint) #scalar distance
        if self.currEnt.speed > 0:
            stopDist = dist/self.currEnt.speed
        shipStop = self.currEnt.speed/self.currEnt.acceleration
        if checkDist(dist, 100):
            self.finished = True
        else:
            if stopDist <= shipStop + self.currEnt.speed:
                self.currEnt.desiredSpeed = 0
            else:
                self.currEnt.desiredSpeed = self.currEnt.maxSpeed
                
    def tick(self, dTime):
        diff = self.desiredPoint - self.currEnt.pos			#distance Vector
        self.currEnt.desiredHeading = math.atan2(-diff.z, diff.x)
    	self.checkStop()
    	
class intercept(Commands):

    def __init__(self, Ent, target):
        Commands.__init__(self, Ent)
        self.Ent    = Ent
        self.target = target
        return None
    def checkStop(self):
        pass
        
    def findVector(self):
        timeToTarget = 1
        dist = diffDist(self.Ent.pos, self.target.pos) #returns Squared Distance
        dist = math.sqrt(dist)
        relativeVel = self.target.vel - self.Ent.vel
        relativeSpeed = relativeVel.length()
        if relativeSpeed > 0:
            timeToTarget = dist/relativeSpeed
        elif self.Ent.speed > 0:
            timeToTarget = dist/self.Ent.speed
        targetLocation = self.target.pos + (relativeVel * timeToTarget)
        self.dist = dist
        return(targetLocation - self.Ent.pos)
	
    def tick(self, dTime):
        diff = self.findVector()
        self.Ent.desiredHeading = math.atan2(-diff.z, diff.x)
        if checkDist(self.dist, 100):
            self.Ent.desiredSpeed = 0
            self.finished = True
        else:
            self.Ent.desiredSpeed = self.Ent.maxSpeed
        
class flee(intercept):

    def __init__(self, Ent, target):
        intercept.__init__(self, Ent,target)
        
    def changeTar(self, newTarget):
	    self.target = newTarget
	            
    def tick(self, dTime):
        diff = self.findVector()
        self.Ent.desiredHeading = math.atan2(diff.z, -diff.x)
        self.Ent.desiredSpeed = self.Ent.maxSpeed
			
class follow(intercept):

    def __init__(self, Ent, chasedEnt):
        intercept.__init__(self, Ent, chasedEnt)
        self.ent = Ent		
        self.chasedEnt = chasedEnt

    def tick(self, dTime):
        diff = self.findVector()
        self.ent.desiredHeading = math.atan2(-diff.z, diff.x)
        if checkDist(self.dist, 10000):
            self.ent.desiredSpeed = self.chasedEnt.speed
        else:
            self.ent.desiredSpeed = self.ent.maxSpeed




