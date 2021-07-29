import random

# Setting up the player
class Human:

    def __init__(self,Name,Gender):
        self.Name = Name
        self.Gender = Gender
        self.Class = "Classless"
        # Attributes
        self.STR = 1
        self.VIT = 1
        self.END = 1
        self.LUK = 1
        # Basic Stats
        self.LVL = 1
        self.EXP = 0
        self.EXPCAP = 5
        self.POINTS = 0
        self.HP = 10 + self.VIT
        self.MAX_HP = 10
        self.STAMINA = 50 + self.END
        self.DMG = 1 + self.STR
        self.CRIT_CHANCE = 2 + self.LUK



        self.DAYS = 0
    def ATTACK(self,target):
        target.HP -= self.DMG
        print(self.Name + " has dealt " + str(self.DMG) + " damage to "+ target.Name +"!")

    def HEAL(self):
        if self.HP + 1 < self.MAX_HP:
            self.HP += 1
            return True
        else:
            print("You have full health!")
            return False
    def giveEXP(self,EXP):
        self.EXP += EXP
        #The player levels up
        while self.EXP > self.EXPCAP:
            self.EXP -= self.EXPCAP
            self.LVL += 1
            self.POINTS += 1
            self.EXPCAP *= 1.5
            self.EXPCAP = round(self.EXPCAP)
            print(self.Name + " has leveled up to level " + str(self.LVL) + "!")
        #Forcing the player to spend stat points
        while self.POINTS > 0:
            print("You have " + str(self.POINTS) + " stats points left.")
            while True:
                UPGRADE = input("Which attributes would you like to upgrade? STRENGTH, VITALITY, ENDURANCE, LUCK: ").upper()
                if UPGRADE == "STRENGTH" or UPGRADE == "VITALITY" or UPGRADE == "ENDURANCE" or UPGRADE == "LUCK":
                    break

            while True:
                AMOUNT = int(input("How much would you like to spend?: "))
                if AMOUNT <= self.POINTS:
                    self.POINTS -= AMOUNT
                    break
            if UPGRADE == "STRENGTH":
                self.STR += AMOUNT
            elif UPGRADE == "VITALITY":
                self.VIT += AMOUNT
            elif UPGRADE == "ENDURANCE":
                self.END += AMOUNT
            elif UPGRADE == "LUCK":
                self.LUK += AMOUNT
            print(self.Name + " has upgraded " + UPGRADE + " by " + str(AMOUNT) + " points!")






# Setting up mobs
class MOB:
    MOBS_NAME = {
        1 : ["SKELETON",1,2,5,1],
        2 : ["HOLLOW",2,4,9,1],
        3 : ["GIANT_SKELETON",10,50,50,5]
    }
    def __init__(self,Name,LVL,EXP,MAXHP,DMG):
        self.Name = Name
        self.LVL = LVL
        self.EXP = EXP
        self.MAXHP = MAXHP
        self.HP = MAXHP
        self.DMG = DMG

    def ATTACK(self,target):
        target.HP -= self.DMG
        print(self.Name + " has dealt " + str(self.DMG) + " damage to "+ target.Name +"!")
        print(target.Name + " has " + str(target.HP) + " left!")


#Creating a character
player_name = str(input("Enter your name: ")).upper()
player_gender = str(input("Are you a male or female?")).upper()
while True:
    if player_gender.upper() == "MALE" or player_gender.upper() == "FEMALE":
        break
    else:
        player_gender = str(input("Are you a male or female?"))

Player = Human(player_name,player_gender)

#-----

#Starting the game
MIN_ENEMYLVL = 1
MAX_ENEMYLVL = 2
while Player.HP > 0:
    TURN = "PLAYER"
    print("DAY " + str(Player.DAYS))
    #Spawing the mob
    MOB_SETUP = MOB.MOBS_NAME[random.randint(MIN_ENEMYLVL,MAX_ENEMYLVL)]
    ENEMY = MOB(MOB_SETUP[0],MOB_SETUP[1],MOB_SETUP[2],MOB_SETUP[3],MOB_SETUP[4])
    print("You have stumbled across " + ENEMY.Name + "!")
    #The Fight has Started!!
    while ENEMY.HP > 0 :
        if TURN == "PLAYER":
            ACTION = input("What are you going to do? ATTACK or HEAL: ").upper()
            #Checking the player action
            while True:
                if ACTION == "ATTACK":
                    Player.ATTACK(ENEMY)
                    print(ENEMY.Name + " has " + str(ENEMY.HP) + " HP left!")
                    break
                elif ACTION == "HEAL":
                    if Player.HEAL() == True:
                        break
                    else:
                        ACTION = input("What are you going to do? ATTACK or HEAL: ").upper()
                else:
                    ACTION = input("Please choose again. ATTACK or HEAL: ").upper()
        #Enemy turn
        elif TURN == "ENEMY":
            ENEMY.ATTACK(Player)
        if Player.HP <= 0:
            break
        if TURN == "PLAYER":
            TURN = "ENEMY"
        else:
            TURN = "PLAYER"
        print("-------------------------------------------------------------------------")
    #The Player Won
    if Player.HP > 0 and ENEMY.HP <= 0:
        print("You've defeated " + ENEMY.Name + "!")
        print("You've gained " + str(ENEMY.EXP) + " EXP!")
        Player.giveEXP(ENEMY.EXP)
        Player.DAYS += 1
        Player.HP = Player.MAX_HP
    if Player.HP <= 0:
        break

#The Adventure has ended :(
print("You lost!")
print("You've survived" + str(Player.DAYS) + " days!")






