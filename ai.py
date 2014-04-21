from vector	 import Vector3
import math

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
				self.commands.pop(0)
			else:
				self.commands[0].tick(dTime)		
		
		
	def addCom(self, comType):
		self.commands.append(comType)
	
	def comFinished(self):
		if len(self.commmands) > 0:
			self.commands.pop(0)
	
	def clearComs(self):
		self.commands[:] = []
		
class Commands:
	
	def __init__(self, Ent):
		self.Ent = Ent
		self.commands = []
		
	def tick(self, dTime):
		if len(self.commands) > 0:
			self.commands[0].tick(dTime)
		
	'''def addCom(self, comType):
		self.commands.append(comType)
	
	def comFinished(self):
		if len(self.commmands) > 0:
			self.commands.pop(0)
	
	def clearComs(self):
		self.commands[:] = []'''
				
class move(Commands):

	def __init__(self, currEnt, desiredPoint = Vector3(0,0,0)):
		Commands.__init__(self, currEnt)
		self.currEnt = currEnt
		self.desiredPoint = desiredPoint
		#self.addCom(move)
		self.finished = False
		
	def tick(self, dTime):
		stopDist = 1000
		dist = diffDist(self.currEnt.pos, self.desiredPoint) #scalar distance
		diff = self.desiredPoint - self.currEnt.pos			#distance Vector
		self.currEnt.desiredHeading = math.atan2(-diff.z, diff.x)
		if self.currEnt.speed > 0:
			stopDist = dist/self.currEnt.speed
		shipStop = self.currEnt.speed/self.currEnt.acceleration
		if checkDist(dist, pow(10,2)):
			self.finished = True
		else:
			#ori = self.currEnt.node.getOrientation()* Vector3(1,0,0)#gets ogre unit orienation of node
			if stopDist <= shipStop:
				self.currEnt.desiredSpeed = 0
			else:
				self.currEnt.desiredSpeed = self.currEnt.maxSpeed
			
class intercept(move):

    def __init__(self, Ent, target):
        move.__init__(self, Ent)
        self.Ent    = Ent
        self.target = target
		
    def tick(self, dTime):
        timeToTarget = 1000
        dist = diffDist(self.Ent.pos, self.target.pos) #returns Squared Distance
        dist = math.sqrt(dist)
        relativeVel = self.target.vel - self.Ent.vel
        relativeSpeed = relativeVel.length()
        if relativeSpeed > 0:
	        timeToTarget = dist/relativeSpeed
        elif self.Ent.speed > 0:
	        timeToTarget = dist/self.Ent.speed
        targetLocation = self.target.pos + (relativeVel * timeToTarget)
        diff = targetLocation - self.Ent.pos
        self.Ent.desiredHeading = math.atan2(-diff.z, diff.x)
        if checkDist(dist, 10):
	        self.Ent.desiredSpeed = 0
	        self.finished = True
        else:
	        self.Ent.desiredSpeed = self.Ent.maxSpeed
			
class follow(move):

    def __init__(self, Ent, chasedEnt):
        move.__init__(self, Ent)
        self.ent = Ent		
        self.chasedEnt = chasedEnt

    def tick(self, dTime):
        timeToTarget = 1000
        dist = diffDist(self.ent.pos, self.chasedEnt.pos)
        dist = math.sqrt(dist)
        relativeVel   = self.chasedEnt.vel - self.Ent.vel
        relativeSpeed = relativeVel.length()
        if relativeSpeed > 0:
            timeToTarget = dist/relativeSpeed
        elif self.ent.speed > 0:
            timeToTarget = dist/self.ent.speed
        unitVelocity = self.chasedEnt.vel.normalisedCopy()
        targetLocation = self.chasedEnt.pos - (unitVelocity*100)
        diff = targetLocation - self.ent.pos
        self.ent.desiredHeading = math.atan2(-diff.z, diff.x)
        if checkDist(dist, 10000):
            self.ent.desiredSpeed = self.chasedEnt.speed
        else:
            self.ent.desiredSpeed = self.ent.maxSpeed




