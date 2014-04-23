class AnimationMgr:
    def __init__(self, Ent):
        self.Ent = Ent
        print "Animation Setup for: ", str(self.Ent)
        self.gent = self.Ent.engine.gfxMgr.sceneManager.getEntity(self.Ent.uiname +"_ogreEnt")
        self.node = self.Ent.aspects[1].node
        self.animationState = self.gent.getAnimationState('Idle')
        self.animationState.setLoop(True)
        self.animationState.setEnabled(True)
        self.dead = False
        
    def tick(self, dTime):
        self.animationState.addTime(dTime)
        if self.Ent.speed > 0:
            self.AnimateWalk()
        elif self.Ent.aspects[2].deathtimer >0:
            if self.Ent.aspects[2].deathtimer >= 10:
                self.AnimateDie()
            elif self.Ent.aspects[2].deathtimer == 20:
                self.Ent.engine.entityMgr.rEnts.append(self.Ent)
            else:
                self.AnimateIdle()
        else:
            self.AnimateIdle()
    
    def AnimateWalk(self):
        self.animationState = self.gent.getAnimationState('Walk')
        self.animationState.setLoop(True)
        self.animationState.setEnabled(True)
    
    def AnimateIdle(self):
        self.animationState = self.gent.getAnimationState('Idle')
        self.animationState.setLoop(True)
        self.animationState.setEnabled(True)
        
    def AnimateDie(self):
        if self.dead == False:
            self.animationState = self.gent.getAnimationState('Die')
            self.dead = True
        self.animationState.setLoop(False)
        self.animationState.setEnabled(True)
