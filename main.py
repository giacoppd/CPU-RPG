#TODO
#Make this happen. For now, dummy shit. Combat? Turns? That speed thing?
#Spells? A bloody interface?
from cpurpg import *
from characters import *
from copy import deepcopy

userparty = mainPartySetup(userparty)
reserveparty = reservePartySetup(userparty, reserveparty)


userParty.statquery(0)

def instance(userparty, baddyparty):
	x = 0
	q = Queue()
	allpeeps.partylist = deepcopy(userparty.partylist)
	allpeeps.partylist.append(baddyparty.partylist)
	sorted(allpeeps.partylist, key=spd, reverse=TRUE)
	while true:
		for person in allpeeps.partylist:
			if x % (60 / person.spd) == 0:
				q.put(person)
                while (q.empty() == false):
			person = q.get()
			if (person.stunD == 0 and person.HP > 0):
				action = int(raw_input("What do you want to do?"))
				person.takeaction(action, baddyparty, userparty)
			person.debuffdown()
			
def mainPartySetup(userparty):
    while len(userparty) < 4:
		newmeat = raw_input("Which character do you want to select? ")
		if partycheck(newmeat, userparty) == False:
		    break
		userparty = partyaddition(userparty, newmeat)
	return party(userparty)
	
def reservePartySetup(userparty, reserveparty):
    while len(reserveparty) < 4:
	    newmeat = raw_input("Which character do you want to select? ")
		if partycheck(newmeat, userparty) == False:
		    break
		if partycheck(newmeat, reserveparty) == False:
		    break
		reserveparty = partyaddition(reserveparty, newmeat)
	return reserveparty
		
def partyaddition(party, newmeat):
    if newmeat.lower().startswith("dom"):
		party.append(Dom())
    else if newmeat.lower().startswith("yong"):
	    party.append(Yong())
	else if newmeat.lower().startswith("hal"):
	    party.append(Haley())
	else if newmeat.lower().startswith("nic"):
	    party.append(Nick())
	else if newmeat.lower().startswith("kat"):
	    party.append(Kath())
	else if newmeat.lower().startswith("jenny k"):
	    party.append(JennyK())
	else if newmeat.lower().startswith("jenny c"):
	    party.append(JennyC())
	else if newmeat.lower().startswith("nat"):
	    party.append(Natasha())
	else if newmeat.lower().startswith("ulri"):
	    party.append(Ulri())
	else if newmeat.lower().startswith("mor"):
	    party.append(Morgan())
	else if newmeat.lower().startswith("rac"):
	    party.append(Rachel())
	else if newmeat.lower().startswith("chris"):
	    party.append(Chris())
	else if newmeat.lower().startswith("mat"):
	    party.append(Matt())
	else if newmeat.lower().startswith("joe"):
	    party.append(Joe())
	else if newmeat.lower().startswith("gal"):
	    party.append(Galen())
	else if newmeat.lower().startswith("jam"):
	    party.append(James())
	else if newmeat.lower().startswith("ash"):
	    party.append(Ashwin())
	else if newmeat.lower().startswith("ken"):
	    party.append(Kenji())
	else 
	    print("your spelling skills could use a little work")
	return party
	
#returns false if given player is already in a party, true otherwise
def partycheck(player, party)
    for member in userparty:
	    if member.name.lower().startswith(player):
		    print("Cloning technology ain't that advanced brother")
			return False
	return True