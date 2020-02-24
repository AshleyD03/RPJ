import random

#Enemy Sprites
enemy_normal = ["||_||","('_')"," -|- ","_||_ "]
enemy_attack = ["||_||","('O')"," -|- ","_||_ "]
enemy_dead = ["||_||","(X-X)"," -|- ","_||_ "]
enemy_clear = ["     ","     ","     ","     "]
enemy_status = []
enemy_status = enemy_normal
#Hero Sprites
hero_normal = ["  _      ","_|^|_    ","(*_*) O  ",",-|-,|   ","_||_|    "]
hero_attack = ["  _      ","_|^|_ * $","(*_*) 0* ",",-|-,|   ","_||_|    "]
hero_dead = ["  _      ","_|^|_    ","(X_X)    ",",-|-,    ","_||_ ___o"]
hero_clear = ["         ","         ","         ","         ","         "]
hero_status = []
hero_status = hero_normal
#Attack Sprites
fire_ball = ["  ,oO"," ,oO ",",oO  "]
pyro_blast = ["oO8  "," oO8 ","oO8 "]
miss_sprite = ["?    ","  ?  "," ?   "]
cut_sprite = ["   ||","  || "," ||  "]
assinate = ["  III"," III ","III  "]
heal_sprite = [" +   ","   + ","  +  "]
sneaky_sprite = [" ??? ","?  ??","  ?  "]
attack_clear = ["     ","     ","     "] 
attack_status = attack_clear

#Top of screen values
level = 1
lives = 1

#Basic health settings
enemy_health = 10
hero_health = 10
enemy_max = 10
hero_max = 10

#Basic damage settings
amplify_1 = 0
amplify_2 = 0

#Basic attack visual
attack_num = ""

#Basic screen state
text_original_1 = "  1 - Attack"+" "*21+"2 - Heavy Attack"
text_1 = text_original_1
text_original_2 = "  3 - Heal"+" "
text_2 = text_original_2
status = "original"

#Used in full screen sprite 
space=" "*3
line="-"+"=-"*25
enter_line=["Jordan Just Sent An Email", "Jamie X Brea","I don't remember much of it, but I went over to yours because you had a free house and such. And I wal real scared but you were gentle with me as you undressed me, sat me on your lap, kissed my neck etc. The next part I remember is being bent over your knee with my arse in the air, and you smacked me and then immediately slipped your fingers inside me, this continued till you... broke me so to speak. And then we fucked. (Side note, that was fucking embarrassing for me to write down so you better fucking appreciate it)","Okay, so we've just gotten out of school and we go to yours to play cuphead or something (???). So we walk into your room and before I can even speak, you've got me pinned against your wall with your mouth on my neck, between the moans and yelps, you eagerly undo my shirt and tie and bra, leaving my chest fully exposed. Your lips trail down my neck to my chest, as you do so I undo your belt and pull your trousers and boxers to your knees. Suddenly you wrap my legs around my waist and hike up my skirt, ripping off my underwear as you do so. Without a secound of warning you thrust yourself into me (wearing protection I might add), and fuck me with a brutal pace, my weak arms are clutching your neck for dear life as a cry out for you, finally I cum around your cock with a whimper and you finish and pull out. I fall to the floor the second you stop holding me, my shaking legs unable to hold me weight. Through my daze, I feel you pick me up and place me in your bed, my body shutting down as I succumb to the urge of sleep","Force = My Ass X Ferosity","Regi-kickass","Elly Wood Just Got Dropped","Put Down The Nut, Or I Will Make An Even Bigger Nut"]

#Prints sprite tab
def sprite_show():
    sprite=[line, "  LVL:  "+str(level)+" "*29+"LIVES:  "+str(lives), line," "*42+enemy_status[0]," "*42+enemy_status[1],"  HP: "+str(hero_health)+" "*(16-int(len(str(hero_health))))+attack_status[0]+" "*15+enemy_status[2],space+hero_status[0]+" "*10+attack_status[1]+" "*15+enemy_status[3],space+hero_status[1]+" "*10+attack_status[2],space+hero_status[2]+" "*25+"  HP: "+str(enemy_health),space+hero_status[3]+" "*6+str(attack_num),space+hero_status[4],line,text_1,text_2,line]
    print("\n"*30)
    for i in range (0,len(sprite)):
        print(str(sprite[i]))
    
while True:
  #Change occurs when enemy dead/lvl over
  if enemy_health <= 0:
    #Edit Level and Health
    level += 1 
    enemy_max += random.randint(1,4)
    enemy_health = enemy_max
    hero_max += random.randint(1,3)
    hero_health = hero_max 
  
    #Edit Damage  
    amplify_1 += random.randint(1,2)
    amplify_2 += random.randint(1,3)
    if amplify_1 >= amplify_2 + 2:
        amplify_1 -= 1 
              
  #To End Game
  if hero_health <= 0:
    break
  
  #Chosen from Option Original Screen
  if status == "original":
    #Full screen sprites
    sprite_show()     
    option = input() + " "
    if option[0] == "1" or option[0] == "2" or option[0] == "3":
        enemy_choice = int(random.randint(1,4))
        
        if option[0] == "1":
            miss = random.randint(1,10)
            if miss == 1:
                #Miss normal attack
                damage = 0
                text_1 = "  ! - Your Fire Ball Misses Somehow... - !"
                attack_status = miss_sprite
                hero_status = hero_dead
            else:
                #Normal Attack
                damage = random.randint(2 + amplify_1, 4 + amplify_2)
                text_1 = "  ! - You Blast The Enemy For " + str(damage) + " Damage - !"
                attack_status = fire_ball
                hero_status = hero_attack
                enemy_status = enemy_dead                     
        elif option[0] == "3":
            #Heal Hero
            heal = random.randint(3 + amplify_1, 7 + amplify_2)
            if hero_health + heal > hero_max:
                damage = hero_max - hero_health
            else:
                damage = heal
            text_1 = "  ! - You Used A Heal Spell And Restored " + str(damage) + " Health - !"
            attack_status = heal_sprite
            hero_status = hero_attack
            damage = damage * -1 
        elif option[0] == "4":
            print("Fix this")
        else:
            miss = random.randint(0,1)
            if miss == 1:
                #Miss massive attack
                damage = 0
                text_1 = "  ! - You Miss Your Pyro-Blast And Deal No Damage - !"
                attack_status = miss_sprite
                hero_status = hero_dead
            else:
                #Hit massive attack
                damage = random.randint(5 + amplify_1, 7 + amplify_2)
                text_1 = "  ! - You Pyro-Blast The Enemy For " + str(damage) + " Damage - !"
                attack_status = pyro_blast
                hero_status = hero_attack
                enemy_status = enemy_dead
                      
        #Remaining changes and then sprite print for Heroes turn
        attack_num = " ?! " + str(damage * -1) + " ?!"  
        if damage > 0:
            enemy_health -= damage
        else:
            hero_health -= damage
        health = False
        #Easter Eggs For ENTER To Continue  
        if random.randint(1,4) == 1:
            text_2 = " " * 10 + "! - " + random.choice(enter_line)+" - !"
        else:
            text_2 = " " * 10 + "! - ENTER To Continue - !"
        sprite_show()                
        input()
        fail = False
               
        #Only attacks if still above 0 HP
        if enemy_health > 0:
            #Resets hero sprites
            hero_status = hero_normal
            enemy_status = enemy_normal

            #Enemies turn to attack/heavy attack/heal/counter
            if enemy_choice == 1:
                #Normal Enemy Attack
                damage = random.randint(2 + amplify_1, 4 + amplify_2)
                text_1 = "  ! - The Enemy Cuts You For " + str(damage) + " Damage - !"
                attack_status = cut_sprite
                enemy_status = enemy_attack
                hero_status = hero_dead
            elif enemy_choice == 2:
                #Enemy Heals
                heal = random.randint(3 + amplify_1, 7 + amplify_2)
                if enemy_health + heal > enemy_max:
                      damage = enemy_max - enemy_health
                else:
                      damage = heal
                text_1 = "  ! - The Enemy Used A Potion to Restore " + str(damage) + " Health - !"
                attack_status = heal_sprite
                enemy_status = enemy_attack
                damage = damage * -1
            elif enemy_choice == 3:
                #Enemy uses counter attack
                if damage > 0:
                    #Counter attack occurs
                    damage = int((damage + (damage % 2)) / 2 + random.randint(2 + amplify_1, 3 + amplify_2))
                    text_1 = "  ! - The Enemies Sneaky Biz Does " + str(damage) + " Damage - !"
                    attack_status = sneaky_sprite
                    enemy_status = enemy_attack
                    hero_status = hero_dead
                else: 
                    #Counter attack fails
                    damage = random.randint(1 + amplify_1, 2 + amplify_2) * -1
                    text_1 = "  ! - The Enemy Hurty Himself For " + str(damage * -1) + " Damage - !"
                    attack_status = miss_sprite 
                    fail = True
            else:
                miss = random.randint(0,1)
                if miss == 1:
                    #Miss enemy massive attack
                    damage = 0
                    text_1 = "  ! - The Enemy Misses There Assinate - !"
                    attack_status = miss_sprite
                    enemy_satus = enemy_dead
                else:
                    #Hit enemy massive attack
                    damage = random.randint(5 + amplify_1, 7 + amplify_2)
                    text_1 = "  ! - The Enemy Assinates You For " + str(damage) + " Damage - !"
                    attack_status = assinate
                    enemy_status = enemy_attack
                    hero_status = hero_dead
                    fail = True
            attack_num = " ?! " + str(damage * -1) + " ?!"
            if damage > 0:
                hero_health -= damage
            elif fail == True:
                enemy_health += damage
                fail = False
            else:
                enemy_health -= damage
            sprite_show() 
            input()
                                                          
        #Resets all sprites changes
        text_1 = text_original_1
        text_2 = text_original_2
        hero_status = hero_normal
        enemy_status = enemy_normal
        attack_status = attack_clear
        attack_num = ""
    
    
    
    
