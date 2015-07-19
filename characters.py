from cpurpg import *

class Dom(unit):

    def __init__(self):
        #self, name, level, xp, VIT, STR, INT, DEF, STAM, SPD, VITup, STRup, INTup, DEFup
        super(Dom, self).__init__(self, "Dominic", 1, 0, 90, 5, 5, 5, 10, 4, 10, 2, 2, 2)    
        self.charge = 1
    def stunPurge(self):
        self.stunD = 0
    
    def focus(self):
        charge += 1
        super(Dom, self).useSTAM(6)
    
    def gattle(enemyParty, pos):
        if (pos == 1):
             enemyParty[0].HP -= 50*charge
             enemyParty[1].HP -= 30*charge
             enemyParty[2].HP -= 30*charge
             enemyParty[3].HP -= 30*charge
        elif (pos == 2):
             enemyParty[1].HP -= 50*charge
             enemyParty[2].HP -= 30*charge
             enemyParty[3].HP -= 30*charge
        else:
             print "How did this happen to me???? Dom gattle"
        charge = 1
        super(Dom, self).useSTAM(8)

    def chen(self, userParty):
        for p in userParty:
            p.heal(50 + self.STR + self.INT)
        self.drainD = 3
        super(Dom, self).useSTAM(10)
        

class Yong(unit):
    
    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(Yong, self).__init__(self, "Yongwoon", 1, 0, 150, 10, 6, 0, 10, 5, 30, 3, 1, 0)
    
    def graniteKick(target):
        target.HP -= (5*self.STR - target.DEF)
        super(Yong, self).useSTAM(10)

    def bloodTrans(partyList):
        for p in partyList:
            p.gainSTAM(3)
        super(Yong, self).useSTAM(13)
    
    def bodyTrans(target):
        self.HP -= 50
        target.heal(5*self.STR)
        super(Yong, self).useSTAM(5)

class Haley(unit): 
    
    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(Haley, self).__init__(self, "Haley", 1, 0, 55, 5, 7, 9, 10, 5, 10, 1, 1, 2)
    
    def drainPurge(self):
        self.drainD = 0
    
    def unravel(self):
        self.bindD = 0
        super(Haley, self).useSTAM(3)
    
    def dash(self, enemyParty):
        for e in enemyParty:
            e.HP -= (2*self.STR + 10 - e.DEF)    
        super(Haley, self).useSTAM(5)
    
    def mountainChisel(self, target):
        target.HP -= (4*(3*self.STR + 15) - target.DEF)
        super(Haley, self).useSTAM(10)
    
    def whirlKick(self, enemyParty):
        enemyParty[0].HP -= (2*self.STR + 15 - enemyParty[0].DEF)    
        enemyParty[1].HP -= (2*self.STR + 15 - enemyParty[1].DEF)    
        super(Haley, self).useSTAM(3)

class Nick(unit):
   
    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(Nick, self).__init__(self, "Nick", 1, 0, 60, 5, 6, 5, 10, 6, 10, 1, 1, 1)
    
    def takeaction(self, i): #nick has double move, is self even needed idk I wish I could compile
            super(Nick, self).takeaction(i)
            #TODO reprompt for input here
            #i = input()
            super(Nick, self).takeaction(i)
    
    def blitz(self, target):
        target.HP -= ((self.STR + 30) - target.DEF)
        super(Nick, self).useSTAM(4)
    
    def rally(self, target):
        target.gainSTAM(4)
        super(Nick, self).useSTAM(4)
    
    def stretch(self):
        self.stunD = 0
        self.bindD = 0
        self.drainD = 0
        self.muteD = 0
        super(Nick, self).useSTAM(10)

class Kath(unit):

    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(Kath, self).__init__(self, "Katherine", 1, 0, 70, 7, 7, 7, 10, 4, 10, 2, 2, 2)
        self.fort = False

    def totem(self, enemyParty):
        for e in enemyParty:
            e.stunD = 2
        self.stunD = 2
        self.drainD = 2
        super(Kath, self).useSTAM(10)

    def obliteration(self, enemyParty):
        DMG = (self.HP // 2) #damage is floored with the //
        for e in enemyParty:
            e.HP -= DMG
        self.HP -= DMG
        super(Kath, self).useSTAM(10)
    
    def uniPurge(self, userParty):
        for u in userParty:
            u.stunD = 0
            u.bindD = 0
            u.muteD = 0
            u.drainD = 0
        self.drainD = 9999
        self.stunD = 9999 #big numbers so she's down for the count
        super(Kath, self).useSTAM(10)
   
   def fortressT(self): #TODO ask joe about how to toggle and if can be purged
        super(Kath, self).useSTAM(6)
        if(self.fort == False):
           self.fort == True
           self.bindD = 9999
           self.DEF = (self.DEF*2)
        elif(self.fort == True):
           self.fort == False
           self.DEF = (self.DEF / 2)

class JennyK(unit):

    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(JennyK, self).__init__(self, "Jenny Kim", 1, 0, 85, 7, 6, 6, 10, 3, 10, 2, 2, 1)
        self.block = False
    def blockT(self):
        self.block = True
        super(JennyK, self).useSTAM(3)
    
    def piercingKick(self, target):
        target.HP -= ((2*self.STR + 2*self.INT) - target.DEF) #Row reduction?
        super(JennyK, self).useSTAM(4)

    def ROTCDrill(self, tiarget):
        target.gainSTAM(5)
        super(JennyK, self).useSTAM(5)
    
    def artOfDeath(self, target):
        target.HP -= (target.VIT - target.HP)
        super(JennyK, self).useSTAM(10)

class JennyC(unit):
    
    def __init__(self):
        #self, name,  level, xp,VIT,STR,INT,DEF,STAM,SPD,VITup, STRup, INTup, DEFup
        super(JennyC, self).__init__(self, "Jenny Chang", 1, 0, 60, 5, 6, 7, 10, 5, 10, 1, 2, 1)
        self.embossD = 0

    def vitalize(self, userParty):
        for u in userParty:
            u.heal(self.INT + 5)
        super(JennyC, self).useSTAM(2)

    def invigorate(self, userParty):
        for u in userParty:
            u.gainSTAM(1)
        super(JennyC, self).useSTAM(3)

    def remove(self, target, choice):
        super(JennyC, self).useSTAM(7)
        if(choice == 1):
            target.stunD = 0
        if(choice == 2):
            target.drainD = 0
        if(choice == 3):
            target.muteD = 0
        if(choice == 4):
            target.bindD = 0
        else:
            print "How did this happen to me? jennyC remove"

    def emboss(self, userParty, toggle): #0 = on, 1 = off
        if(toggle == 0):
            amount = self.DEF
        elif(toggle == 1):
            amount = -self.DEF
        for u in userParty:
            u.DEF += amount
        super(JennyC, self).useSTAM(10)


