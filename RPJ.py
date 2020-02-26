import random
import time

#Sprite Extra's
space = " " * 3
line = "-"+"=-" * 25
#Enemy Sprites
enemy_normal_n = ["         ",
                  "  ||_||  ",
                  "  ('_')  ",
                  "  !-|-   ",
                  "  _||_   "]
enemy_normal_b = ["O   M_M  ",
                  "|  ('_') ",
                  " |]=|O|=,",
                  " |  V|V  ",
                  " |_|| ||_"]
enemy_normal = enemy_normal_n
enemy_attack_n = ["         ",
                  "  ||_||  ",
                  "  (^O^)  ",
                  "  !-|-   ",
                  "  _||_   "]
enemy_attack_b = ["0   M_M  ",
                  "|* (YoY) ",
                  "*|]=|O|=,",
                  " |  V|V  ",
                  " |_|| ||_"]
enemy_attack = enemy_attack_n
enemy_dead_n =   ["         ",
                  "  ||_||  ",
                  "  (X-X)  ",
                  "   -|-   ",
                  "  _||_   "]
enemy_dead_b =   ["O   M_M  ",
                  "|  (X-X) ",
                  " |]=|O|=,",
                  " |  V|V  ",
                  " |_|| ||_"]
enemy_dead = enemy_dead_n
enemy_clear = ["     ","     ","     ","     "]
enemy_status = enemy_normal
#Boss Name List
enemy_name_list = ["Steve","Bend Over","Hugh Jass", "Crab Nest","Phill Greenwood","Indian Telephone","Morm","Gianormous Bulg","", "Dweeb Muffin", "Regigigas", "Travis Scott", "Tittenick", "Kidifidora", "Mrs. Koyanagi", "Geraldinestiegn", "Wallee", "Eeevvaaa", "The Wise Uncle", "The Enchanted Dragon Of Wisdom", "Dixie Normus", "Ryan Rim-licker", "Selina the Serperior", "Ibby-Vinon", "Gym Leader Elesa", "An Iceburg..."]

#Hero Sprites
hero_normal = ["  _      ",
               "_|^|_    ",
               "(*_*) O  ",
               ",-|-,|   ",
               "_||_|    "]
hero_attack = ["  _      ",
               "_|^|_ * $",
               "(*_*) 0* ",
               ",-|-,|   ",
               "_||_|    "]
hero_dead =   ["  _      ",
               "_|^|_    ",
               "(X_X)    ",
               ",-|-,    ",
               "_||_ ___o"]
hero_clear = ["         ","         ","         ","         ","         "]
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

#RPJ opening Sprite
opening_text = ["          ||||||      ||||||     ||||||||||        ", 
                " |       |||  ||     |||  ||         |||       |   ", 
                "|||     |||  ||     |||  ||         |||       |||  ", 
                " |     ||||||      ||||||          |||         |   ", 
                "      |||  ||     |||       |||  |||               ", 
                "     |||   |||   |||         ||||||                "]
opening_line = " !? - PRESS ENTER + PRESS ENTER + PRESS ENTER - ?! "
#Rip sprite
end_sprite = [line, " " * 12 + " ! - ENTER To Restart - !", line, "",
             "            ||||||         |||        |||||        ", 
             "   |       |||  ||        |||        |||  ||   |   ", 
             "  |||     |||  ||                   |||  ||   |||  ", 
             "   |     ||||||         |||        ||||||      |   ", 
             "        |||  ||        |||        |||              ", 
             "       |||   |||      |||        |||               ",
             "", line, " " * 12 + " ! - ENTER To Restart - !", line]
#Top of screen values
level = 1
lives = 1

#Basic health settings
enemy_max = 5
hero_max = 10
enemy_health = enemy_max
hero_health = hero_max

#Basic damage settings
amplify_1 = 0
amplify_2 = 0
enemy_amplify_1 = 0
enemy_amplify_2 = 0

#Boss Amplifier
boss_buff = 0

#Basic attack visual
attack_num = ""

#Item Sprites
shield_sprite = ["||=||", 
                 " |0| ", 
                 " '=' "]
hammer_sprite = ["[=o=]", 
                 "  I  ", 
                 "  |  "]
shroom_sprite = [" oOo ", "oOOOo", " |_| "]
card_sprite =[" [|] ",
              " |?| ",
              " [|] "]
empty_sprite = ["     ", "  ?  ", "     "]
#Item names and sprites
item_names = [["SHIELD", shield_sprite, ""], ["HAMMER", hammer_sprite], ["SHROOM", shroom_sprite], ["TERO CARD", card_sprite], ["------", empty_sprite]]
#Basic Inventory 
inventory_items = ["TERO CARD", "------", "------"]
slots = [empty_sprite, empty_sprite, empty_sprite]
inventory_message = " Wellcome to Your Inventory"
inventory_question = " Whatcha Wanna Do?"
tero_card_random = 0

#Basic screen state
text_original_1 = "  1 - Attack" + " " * 21 + "2 - Heavy Attack"
text_1 = text_original_1
text_original_2 = "  3 - Heal" + " " * 23 + "4 - Inventory"
text_2 = text_original_2
status = "original"
introduction = True
reward_val = False

#Prints battle sprites
def sprite_show():
    sprite = [line, "  LVL:  "+str(level)+" "*29+"LIVES:  "+str(lives), line, " " * 40 + enemy_status[0], " " * 40 + enemy_status[1],"   HP: "+str(hero_health)+" "*(15-int(len(str(hero_health))))+attack_status[0]+" "*13+enemy_status[2],space+hero_status[0]+" "*10+attack_status[1]+" "*13+enemy_status[3],space+hero_status[1]+" "*10+attack_status[2]+" "*13+enemy_status[4],space+hero_status[2],space+hero_status[3]+" "*6+str(attack_num)+" "*(21-int(len(attack_num)))+"  HP: "+str(enemy_health),space+hero_status[4],line, str(text_1), str(text_2), line]
    print("\n" * 30)
    for i in range (0,len(sprite)):
        print(str(sprite[i]))

#Outputs inventory screen
def inventory_show():
    inventory_sprite = [line, "  LVL:  " + str(level) + " " * 29 + "LIVES:  " + str(lives), line,
                     "  1. " + inventory_items[0] + " " * (10 - int(len(inventory_items[0]))) + " ._=[1]=_.   ._=[2]=_.   ._=[3]=_.  ",
                     "     " +                      " " * 10                                  + " |       |   |       |   |       |  ",
                     "  2. " + inventory_items[1] + " " * (10 - int(len(inventory_items[1]))) + ".I " + slots[0][0] + " I. .I " + slots[1][0] +" I. .I " + slots[2][0] + " I. ",
                     "     " +                     " " * 10 +                                   " 8 " + slots[0][1] +" 8   8 " + slots[1][1] + " 8   8 " + slots[2][1] + " 8  ",
                     "  3. " + inventory_items[2] + " " * (10 - int(len(inventory_items[2]))) + "'I " + slots[0][2] + " I' 'I " + slots[1][2] + " I' 'I " + slots[2][2] + " I' ",
                     "     " +                     " " * 10 +                                   " |       |   |       |   |       |  ",
                     "  4. " + "Go Back" +               " " * 3 +                                 " =|||||||=   =|||||||=   =|||||||=  ",
                     line, inventory_message, inventory_question, line]                                                                                                                                                       
    print("\n" * 30)
    for i in range (0,len(inventory_sprite)):
        print(str(inventory_sprite[i]))        
        
#Game Start Up Image
for x in range (0,51):
    print("\n" * 50 + line + "\n" + opening_line + "\n" + line + "\n")
    for i in range (0,6):
        print(opening_text[i]) 
        bot_value = opening_text[i][0]        
        opening_text[i] = opening_text[i].replace(bot_value, "", 1) + bot_value
    print("\n" + line + "\n" + opening_line + "\n" + line + "\n" * 3)
    time.sleep(0.025)
input()        

#Loop game
while True:
  #Level up
  if enemy_health <= 0:
    #Edit Level and Health
    level += 1
    introduction = True
    if level % 5 == 0:
        #Boss level sprites
        boss_buff = random.randint(int(level / 5),int(level / 5) * 2 - 1)
        enemy_normal = enemy_normal_b 
        enemy_attack = enemy_attack_b
        enemy_dead = enemy_dead_b
        enemy_status = enemy_normal
        enemy_name = "Somebody..."
    else:
        #Lowers max health after boss level
        if level % 5 == 4:
            enemy_max -= boss_buff        
        #Normal enemy sprites and name
        boss_buff = 0
        enemy_normal = enemy_normal_n
        enemy_attack = enemy_attack_n
        enemy_dead = enemy_dead_n
        enemy_status = enemy_normal
        enemy_name = random.choice(enemy_name_list)
        
    #Enemy Buffs
    enemy_max += random.randint(2,4) + boss_buff
    enemy_health = enemy_max
    #Hero Buffs
    hero_orig = hero_max #Might not be needed, please look into
    hero_max += random.randint(2,6)
    hero_health = hero_max 
    
    #Edit Damage
    damage_1 = random.randint(0,2)
    damage_2 = random.randint(1,3) 
    if amplify_1 + damage_1 >= amplify_2 + 2 + damage_2:
        damage_1 -= 1 
    amplify_1 += damage_1
    amplify_2 += damage_2
    amp = random.randint(1,4)
    enemy_amplify_1 += amp
    enemy_amplify_2 += amp
    
    #Play Lvl Up sprite
    lvl_sprite = [line, "  LVL:  " + str(level) + " " * 29 + "LIVES:  " + str(lives), line, "",
                 "           ||   ||   || ||     || || ||[]          ",
                 "    []     ||    || ||  ||     || || ||[]    []    ",
                 "           ||||   |||   |||     |||  ||            ",
                 "",
                 "             HP +" + str(hero_max - hero_orig) + " " * 10 + "DMG +" + str(damage_1) + "-" + str(damage_2 + damage_1) + "     ", "", line, "      !  - Congratulations Hero Ya Did It - !", " " * 10 + " ! - ENTER To Continue - !", line]
    print("\n" * 30)
    for i in range (0,len(lvl_sprite)):
      print(str(lvl_sprite[i]))
    input("\n" * 3)
    
    if (level - 1) % 5 == 0:
      reward_val = True
    
    #Chest Reward  
  if reward_val == True:
      reward_val = False
      #Chooses Reward
      reward_random = random.randint(0,len(item_names) - 1)
      reward_sprite = item_names[reward_random][1]
      reward_name = item_names[reward_random][0]
      
      #Sprites for chest opening
      chest_sprite_top_line = line + "\n  LVL:  " + str(level) + " " * 29 + "LIVES:  " + str(lives) + "\n" + line
      chest_sprite_clear_bot = line + "\n\n\n" + line      
      chest_sprite = [[chest_sprite_top_line,
                     "    *           ?                   *        ?     ",
                     "             *     |||||||||||||||     ?        *  ",
                     "  ?      *        @=||===[@]===||=@         *      ",
                     "     *       ?    ||     ^ ^     ||   *         ?  ",
                     " *       ?      [=||      U      ||=]      *       ",
                     "   *          *   ||             ||      ?      *  ",
                     "      ?     *     *|||||||||||||||*   *       *    ",
                    #"                          I                        "
                     line, " " * 6 + "! - Woah Dude, It's A Chest - !", " " * 10 + " ! - ENTER To Continue - !", line],
                     [chest_sprite_top_line, 
                     "    *           ?   _||||   ||||_   *        ?     ",
                     "             *     |||         |||    ?         *  ",
                     "  ?      *        @=||===[@]===||=@         *      ",
                     "     *       ?    ||     o o     ||   *         ?  ",
                     " *       ?      [=||      O      ||=]      *       ",
                     "   *          *   ||             ||      ?      *  ",
                     "      ?     *     *|||||||||||||||*   *       *    ",
                     chest_sprite_clear_bot],
                     [chest_sprite_top_line, 
                     "    *           ?   _||       ||_   *        ?     ",
                     "             *     ||   " + reward_sprite[0] + "   ||    ?         *  ",
                     "  ?      *        @=||===[@]===||=@         *      ",
                     "     *       ?    ||     U U     ||   *         ?  ",
                     " *       ?      [=||      W      ||=]      *       ",
                     "   *          *   ||             ||      ?      *  ",
                     "      ?     *     *|||||||||||||||*   *       *    ",
                     chest_sprite_clear_bot],
                     [chest_sprite_top_line, 
                     "       *   ?                            *      *   ",
                     "    *           ?   ||  " + reward_sprite[0] + "  ||   *        ?     ",
                     "             *     ||   " + reward_sprite[1] + "   ||    ?         *  ",
                     "  ?      *        @=||===[@]===||=@         *      ",
                     "     *       ?    ||     U U     ||   *         ?  ",
                     " *       ?      [=||      W      ||=]      *       ",
                     "   *          *   ||             ||      ?      *  ",                     
                     chest_sprite_clear_bot],
                     [chest_sprite_top_line, 
                     " ?               *                    *      ?       ",
                     "       *   ?            " + reward_sprite[0] + "           *      *   ",
                     "    *           ?  ||   " + reward_sprite[1] + "   ||  *        ?     ",
                     "             *     ||   " + reward_sprite[2] + "   ||    ?         *  ",
                     "  ?      *        @=||===[@]===||=@         *      ",
                     "     *       ?    ||     U U     ||   *         ?  ",
                     " *       ?      [=||      W      ||=]      *       ",                     
                     chest_sprite_clear_bot],
                     [chest_sprite_top_line,
                     "    *         *                    ?             * ",
                     " ?               *      " + reward_sprite[0] + "        *      ?      ",
                     "       *   ?            " + reward_sprite[1] + "           *      *   ",
                     "    *           ? ||    " + reward_sprite[2] + "   || *        ?     ",
                     "             *     ||          ||    ?         *   ",
                     "  ?      *        @=||===[@]===||=@         *      ",
                     "     *       ?    ||     U U     ||   *         ?  ",                     
                     chest_sprite_clear_bot],
                     [chest_sprite_top_line,
                     "  ?       ?                             *     *    ",
                     "    *         *         " + reward_sprite[0] + "      ?             * ",
                     " ?               *      " + reward_sprite[1] + "        *      ?      ",
                     "       *   ?            " + reward_sprite[2] + "           *      *   ",
                     "    *           ? ||            || *        ?      ",
                     "             *     ||          ||    ?         *   ",
                     "  ?      *        @=||===[@]===||=@         *      ",                     
                     chest_sprite_clear_bot],
                     [chest_sprite_top_line,
                     "      *           *                *     *         ",
                     "  ?       ?             " + reward_sprite[0] + "           *     *    ",
                     "    *         *         " + reward_sprite[1] + "      ?             * ",
                     " ?               *      " + reward_sprite[2] + "        *      ?      ",
                     "       *   ?                            *      *   ",
                     "    *           ? ||            || *        ?      ",
                     "             *     ||          ||    ?         *   ",                     
                     chest_sprite_clear_bot],
                     [chest_sprite_top_line,
                     " *           ?                       *          ?  ",
                     "      *           *     " + reward_sprite[0] + "      *     *         ",
                     "  ?       ?             " + reward_sprite[1] + "           *     *    ",
                     "    *         *         " + reward_sprite[2] + "      ?             * ",
                     " ?               *                   *      ?      ",
                     "       *   ?                            *      *   ",
                     "    *           ? ||            || *        ?      ",                     
                     chest_sprite_clear_bot],
                     [chest_sprite_top_line,
                     "    *          ?                       ?   *       ",
                     " *           ?          " + reward_sprite[0] + "        *          ?  ",
                     "      *           *     " + reward_sprite[1] + "      *     *         ",
                     "  ?       ?             " + reward_sprite[2] + "           *     *    ",
                     "    *         *                    ?             * ",
                     " ?               *                   *      ?      ",
                     "       *   ?                            *      *   ",                    
                     chest_sprite_clear_bot],
                     [chest_sprite_top_line,
                     "    *          ?      *       *        ?   *       ",
                     " *           ?          " + reward_sprite[0] + "        *          ?  ",
                     "      *           *     " + reward_sprite[1] + "      *     *         ",
                     "  ?       ?             " + reward_sprite[2] + "           *     *    ",
                     "    *         *                    ?             * ",
                     " ?               *    - " + reward_name + " -" + " " * (11 - len(reward_name)) + "*      ?      ",
                     "       *   ?                            *      *   ",                    
                     line + "\n" + " " * 10 + "! - You Found a " + reward_name + " - !\n" + " " * 10 + " ! - ENTER To Continue - !\n" + line]
                     ]
      
      #Print sprite animation
      print("\n" * 30)
      for i in range (0,len(chest_sprite[0])):
        print(chest_sprite[0][i])
      input("\n" * 3)
      
      for x in range (1, len(chest_sprite)):
        time.sleep(0.5)
        print("\n" * 30)
        for i in range (0,len(chest_sprite[x])):            
            print(chest_sprite[x][i])
        print("\n" * 3)
      time.sleep(0.5)
      input()
      
      #Check Space in Inventory
      bag_check = 0
      for i in range (0,3):
        if inventory_items[i] != "------":
          bag_check += 1 
                    
      #If there is space for item
      if bag_check != 3:
        #Find space for item
        bag_space = 0
        inventory_check = True
        while inventory_check == True:
          if inventory_items[bag_space] == "------":
            inventory_check = False
          else:
            bag_space += 1        
        #Add item to inventory
        inventory_items[bag_space] = reward_name
        
        #Add to inventory sprite
        inventory_add_sprite = [chest_sprite_top_line,
                                "  -=====-              ||   ||            -=====-  ",
                                "             -=====-    [===]  -=====-             ",
                                "    -=====-             |||||           -=====-    ",
                                "            -====-    |||| ||||   -====-           ",
                                " -=====-            ,||| ^ ^ |||,          -=====- ",
                                "           -====-  ||     U     ||  -====-         ",
                                "    -====-         |||         |||        -====-   ",
                                "            -====- '|||||||||||||' -====-          ",
                                line + "\n" + " " * 7 + "! - Let's Put That Guy In Safe Keeping - !\n" + " " * 10 + " ! - ENTER To Continue - !\n" + line
                               ]        
          
      #If inventory is full
      else:
        inventory_add_sprite = [chest_sprite_top_line,
                                "  -=====-              ||   ||            -=====-  ",
                                "             -=====-    [===]  -=====-             ",
                                "    -=====-             |||||           -=====-    ",
                                "            -====-    |||| ||||   -====-           ",
                                " -=====-            ,||| ; ; |||,          -=====- ",
                                "           -====-  ||     W     ||  -====-         ",
                                "    -====-         |||         |||        -====-   ",
                                "            -====- '|||||||||||||' -====-          ",
                                line + "\n" + " " * 7 + "! - Oh no, your inventorys full... Guess your stuffed - !\n" + " " * 10 + " ! - ENTER To Continue - !\n" + line
                                ]
      print("\n" * 30)
      for i in range (0,len(inventory_add_sprite)):
        print(inventory_add_sprite[i])
      input("\n" * 3)
      
  #Introduce New Enemy
  if introduction == True:            
      #Play Enemy Intro sprite
      enemy_name = random.choice(enemy_name_list)
      intro_sprite = [line, "  LVL:  " + str(level) + " " * 29 + "LIVES:  " + str(lives), line, 
                          "                    .|||||||.",
                          "        _==_      .||   "    +       "    ||.      _==_        ",
                          "   $   ||  ||   $ ||" + enemy_status[0] + "|| $   ||  ||   $   ",
                          "   I  ||    ||  I ||" + enemy_status[1] + "|| I  ||    ||  I   ",
                          "      ||    ||    ||" + enemy_status[2] + "||    ||    ||      ",
                          "      *||||||*    ||" + enemy_status[3] + "||    *||||||*      ",
                          "..................||" + enemy_status[4] + "||..................",
                          line,  " " * 5 + "! - " + enemy_name + " is Approuching - !", " " * 10 + " ! - ENTER To Continue - !", line]
      print("\n" * 30)
      for i in range (0,len(intro_sprite)):
        print(str(intro_sprite[i]))
      input("\n" * 3)
      introduction = False
      
  #To End Game
  if hero_health <= 0:
    lives -= 1
    if lives == 0:
      #Play Game Ending Sprite
      print("\n" * 30)
      for i in range (0,len(end_sprite)):
          print(str(end_sprite[i]))
      input("\n" * 3)

      #Resets Game Values
      level = 1
      lives = 1
      enemy_max = 10
      enemy_health = enemy_max
      hero_max = 10
      hero_health = hero_max
      amplify_1 = 0
      amplify_2 = 0
      enemy_amplify_1 = 0
      enemy_amplify_2 = 0
      boss_buff = 0    
      enemy_normal = enemy_normal_n
      enemy_attack = enemy_attack_n
      enemy_dead = enemy_dead_n
      enemy_status = enemy_normal
    else:
      #####################################################################################################################Add Animation
      enemy_health = enemy_max
      hero_health = hero_max
  #Game then begins  
  #Chosen from Option Original Screen
  if status == "original":
    #Full screen sprites
    sprite_show()     
    option = input("\n" * 3) + " "
    if option[0] == "1" or option[0] == "2" or option[0] == "3":
        enemy_choice = int(random.randint(1,4))
        
        if option[0] == "1":
            miss = random.randint(1,10)
            if miss == 1:
                #Miss normal attack
                damage = 0
                text_1 = " You Missed"
                attack_status = miss_sprite
                hero_status = hero_dead
            else:
                #Normal Attack
                damage = random.randint(2 + amplify_1, 5 + amplify_2)
                text_1 = " You Cast A Magical Spooky Wave , For " + str(damage) + " Damage"
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
            text_1 = " You Take A Smoke Break For " + str(damage) + " Health"
            attack_status = heal_sprite
            hero_status = hero_attack
            damage = damage * -1             
            
        else:
            miss = random.randint(1,5)
            if miss == 2 or miss == 1:
                #Miss massive attack
                damage = 0              

                text_1 = " You Missed"
                attack_status = miss_sprite
                hero_status = hero_dead
            else:
                #Hit massive attack
                damage = random.randint(5 + amplify_1, 9 + amplify_2)
                text_1 = " You BLAAASST Them For " + str(damage) + " Damage"
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
        if random.randint(1,6) == 1:
            text_2 = " Don't Leave Me..."
        else:
            text_2 = " Press ENTER To Continue"
        sprite_show()                
        input("\n" * 3)
        fail = False
               
        #Only attacks if still above 0 HP
        if enemy_health > 0:
            #Resets hero sprites
            hero_status = hero_normal
            enemy_status = enemy_normal

            #Enemies turn to attack/heavy attack/heal/counter
            if enemy_choice == 1:
                #Normal Enemy Attack
                damage = random.randint(1 + enemy_amplify_1 + boss_buff, 4 + enemy_amplify_2 + boss_buff)
                text_1 = " They Slice Ur Side Burns For " + str(damage) + " Damage"
                attack_status = cut_sprite
                enemy_status = enemy_attack
                hero_status = hero_dead
                
            elif enemy_choice == 2:
                #Enemy Heals
                heal = random.randint(2 + enemy_amplify_1 + boss_buff, 6 + enemy_amplify_2 + boss_buff) 
                if enemy_health + heal > enemy_max:
                      damage = enemy_max - enemy_health
                else:
                      damage = heal
                text_1 = " The Enemy Stares At Your... Angrily... "
                attack_status = heal_sprite
                enemy_status = enemy_attack
                damage = damage * -1
                
            elif enemy_choice == 3:
                #Enemy uses counter attack
                if damage > 0:
                    #Counter attack occurs
                    damage = int((damage + (damage % 2)) / 2 + random.randint(1 + enemy_amplify_1 + boss_buff, 2 + enemy_amplify_2 + boss_buff))
                    text_1 = " The Enemy Did This Cool Thing With His Hands, For " + str(damage) + " Damage"
                    attack_status = sneaky_sprite
                    enemy_status = enemy_attack
                    hero_status = hero_dead
                else: 
                    #Counter attack fails
                    damage = random.randint(1 + enemy_amplify_1 + boss_buff, 2 + enemy_amplify_2 + boss_buff) * -1
                    text_1 = " The Enemy May, or May Not, Have Hurt Himself... For " + str(damage * -1) + " Damage"
                    attack_status = miss_sprite 
                    fail = True
                    
            else:
                miss = random.randint(0,1)
                if miss == 1:
                    #Miss enemy massive attack
                    damage = 0
                    text_1 = " The Enemy Chooses Paper"
                    attack_status = miss_sprite
                    enemy_satus = enemy_dead
                else:
                    #Hit enemy massive attack
                    damage = random.randint(4 + enemy_amplify_1 + boss_buff, 6 + enemy_amplify_2 + boss_buff)
                    text_1 = " The Enemy Used The Sharp Side Of The Knife For " + str(damage) + " Damage"
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
            input("\n" * 3)
                                                          
        #Resets all combat sprites changes
        text_1 = text_original_1
        text_2 = text_original_2
        hero_status = hero_normal
        enemy_status = enemy_normal
        attack_status = attack_clear
        attack_num = ""
    
    #Inventory Option
    elif option[0] == "4":
        status = "bag"
        
  #Inventory Option Screen     
  elif status == "bag":
    #Changes slot sprites for inventory
    for i in range (0,int(len(inventory_items))):
      for x in range (0,int(len(item_names))):
        if inventory_items[i] == item_names[x][0]:
          for z in range (0,2):
            slots[i] = item_names[x][1] 
            
    #Outputs inventory screen
    inventory_show()
    inventory_choice = input("\n" * 3) + " "
    
    #Choose to leave Inventory
    if inventory_choice[0] == "4":
        status = "original"
    
    #Choose to use item 1-3
    elif inventory_choice[0] == "1" or inventory_choice[0] == "2" or inventory_choice[0] == "3":
        #If Inventory is Empty
        if inventory_items[int(inventory_choice[0]) - 1] == "------":
            inventory_message = " Sorry, But That Slot's Empty..."
            inventory_question = " Press ENTER To Continue"
            inventory_show()
            inventory_choice = input("\n" * 3) + " "
            inventory_message = " Wellcome to Your Inventory"
            inventory_question = " Whatcha Wanna Do?"
            
        else:
            #Clears item from inventory and stores under new item_use variables
            item_use_name = inventory_items[int(inventory_choice) - 1]
            inventory_items[int(inventory_choice) - 1] = "------"
            slots[int(inventory_choice) - 1] = empty_sprite
            inventory_message = " You Use Your " + item_use_name 
            inventory_question = " Press ENTER To Continue"
            #Outputs Inventory Change
            inventory_show()
            input("\n" * 3)            
            
            if item_use_name == "TERO CARD":
                #Effect for Tero Card Use
                hero_status = hero_dead
                enemy_status = enemy_dead
                attack_status = card_sprite
                text_1 = " You Play Your Tero Card... What mystery will happen?"
                text_2 = " Press ENTER To Continue" 
                tero_card_random = random.randint(1,3)
                
                #Extra Screen for Tero Card
                sprite_show()
                input("\n" * 3)               
            
            if item_use_name == "HAMMER" or tero_card_random == 1 :
                #Effect for Hammer Use
                damage = enemy_health - random.randint(1, 1 + amplify_1)
                hero_status = hero_attack
                enemy_status = enemy_dead 
                attack_status = hammer_sprite
                enemy_health -= damage                
                text_1 = " You Use Your Hammer, And Whack Them Hard For " + str(damage) + " Damage"
                attack_num = " ?! " + str(damage * -1) + " ?!"

            
            elif item_use_name == "SHIELD" or tero_card_random == 2 :
                #Effect for Shield
                damage = int((hero_max + (hero_max % 2)) / 2)
                hero_status = hero_attack
                attack_status = shield_sprite
                hero_health += damage
                hero_max += damage
                text_1 = " You Hold the Shield... Max Health Buff for +" + str(damage) 
                attack_num = " ?! +" + str(damage) + " ?!"
            
            elif item_use_name == "SHROOM" or tero_card_random == 3:
                #Effect for Shroom
                lives += 1
                damage = 1
                hero_status = hero_attack
                attack_status = shroom_sprite
                text_1 = " You Ate the Shroom and Gained a Life ?"
                attack_num = " ?! +" + str(damage) + " ?!"
                
            #Display of Item being Used    
            text_2 = " Press ENTER To Continue"                            
            sprite_show()    
            input("\n" * 3)
            inventory_message = " Wellcome to Your Inventory"
            inventory_question = " Whatcha Wanna Do?"
            
            #Resets all combat sprites changes
            text_1 = text_original_1
            text_2 = text_original_2
            hero_status = hero_normal
            enemy_status = enemy_normal
            attack_status = attack_clear
            attack_num = ""
            tero_card_random = 0
    