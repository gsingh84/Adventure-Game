#All functions call at the end of this program

import random

treasure = ['pieces of gold!', 'bars of silver!', 'Diamonds!', 'bottles of aged Rum!']

bag = ['Provisions']

#yorn function allow user to enter yes or no.
def yorn():
    yinput = ""
    while True:
        yinput = input("Please Enter Yes or No (Y/N): ")
        if yinput == 'Y' or yinput == 'y' or yinput == 'n' or yinput == 'N':
            return yinput
        

#find_treasure function find the random treasure from given list.
def find_treasure(ref):
    new = random.sample(set(treasure),1)
    from random import randint
    qty_tr = (randint(1,50), new[0], '%s.'%ref)
    print()
    print ('You Found', ' '.join(str(x) for x in qty_tr))
    print('---------------------------------')
    bag.append(qty_tr)
    show_treasure()
    print('---------------------------------')
    
            
#show_treasure function shows the items that available in the bag.
def show_treasure():
    print('your bag of holding contains:')
    for list in bag:
        print (' '.join(str(x) for x in list))
        
        
#This is strating point of program, this function gives the intro.
def intro():
    print("Time for a little adventure!")
    print()
    print("You're for a hike, you have a walking stick, backpack, and some provisions")
    print()
    print("You have been following a stream bed through a forest, when you see a")
    print("small stone building. Around you is a forest. A small stream flows out of the")
    print("building and down a gully.")
    print()
    print("Just outside of the small building, by a warm, inviting fire, is an old,")
    print("possibly ancient man, with long rather mangy beard. He sees you and says:")
    print()
    print("\t 'Hello my friend, stay a while and listen...'")
    print()
    print("You're not sure why, but you decide to stay and listen as he tells you stories")
    print("of strange and magical lands of adventure and Treasure!")
    print()
    print("After what seems like hours, the old man admits to being a bit hungry. He asks,")
    print("pointing at your backpack, if you have food in your 'bag of Holding', that")
    print("you might be willing to share.")
    print()
    print("Do you share your provisions?")
    print("-------------------------------------------------------------------------------")
    fun_input = yorn() #call the yorn function here to get input from user.
    if fun_input == "y" or fun_input == "Y": 
            print("The old man hungrily devours all of your provisions with barely a crumb in sight")
            print()
            print("He leans close to you and whispers 'Besides gold, silver, and diamonds, if you")
            print("chosse wisely, there could also be other valuable GEMS!'")
            print()
            print('He slips you something of great value...')
            treasure.insert(0, 'bags of GEMS!') #if user Enter 'y' then it will add (bags of GEMS!) into the treasure list other wise not.
            print()
            print("your possible treasures are:")
            bag.remove(bag[0]) #after sharing provison with old man, this statement will remove provisions from bag other wise provisions remain in the bag. 
            for list in treasure:
                ge = list.strip()
                print(ge)
            find_treasure("from old man")  #call the find_treasure function here and pass the argument for where the item found from and also show the items in the bag.
    elif fun_input == 'N' or fun_input == "n":
            print("He looks at you wistfully ... for a moment,")
            print(" then eats the last few crumbs.")
            print()
            print('your possible treasures are:')
            for list in treasure:
                ge = list.strip()
                print(ge)
   
 

#potion function allow user to choose between two potions.
def potion():
    print("-------------------------------------------------------------------------------")
    print("The old man stands up and waves his hand towards a rather ornate table close to")
    print("the building. you didn't notice the table before, but it's really quite out of")
    print("place in this forest.")
    print()
    print("On the ornate table is two bottles of potion, one is blue, and the other is red.")
    print()
    print("There is also a note, the note says,")
    print()
    print("\t Drink the BLUE potion and believe whatever you want to believe.")
    print()
    print("The rest of the note is destroyed and can't be read.")
    print()
    print("You turn to the old man, he seems to look much taller and a bit forbidding ...")
    print()
    print("\t He points at the table and says 'CHOOSE' ")
    print()
    red = ('RED')
    blue = ('BLUE')
    pinput = input('Do you choose the RED potion or the BLUE potion (R/B)? ')
    if pinput == "r" or pinput == "R":
        print()
        print('you guzzle the contents of the bottle with the red potion.')
        print()
        print("you feel like you're on fire! smoke is pouring out of your nose and ears!")
        print("when the thick red billowy smoke subsides, the old man is gone and there is a")
        print("narrow cobblestone trail leading from the small building.")
        print()
        print("you follow the cobblestone trail.")
        return (red)
        
    elif pinput == "b" or pinput == "B":
        print()
        print("you drink the BLUE potion. Nothing seems to happen ... at first. Then")
        print("strangely your body tingles , an old man bids you farewell as he leaves the park.")
        print("you wonder vaguely about something regarding a hike or a forest ...")
        return (blue)
    else:
        print()
        print("you fail to drink a potion, the old man leaves and you wonder aimlessly though")
        print("the forest, hopelessly lost!")






def dwarf():
    max  = 6
    for counter in range(max): 
        from random import randint
        dwarfappear = (randint(1,2)) 
        dwarf_r = (randint(1,2)) 
        if dwarfappear == 1: #Here you can see if dwarfappear variable or random number = 1 then dwarf will appear 
            print("-------------------------------------------------------------------------------")
            print("As you procees along the trail, you encounter a wicked looking")
            print("dwarf with a long black beard.")
            print()
            print("He has a large rusty knife in his hand!")
            print()
            print("He seems to be laughing at you as you're trying to decide to attack or to just")
            print("run away ...")
            print()
            print("Do you attack?")
            print("-------------------------------------------------------------------------------")
            dwarfinput = yorn() #Here I call the yorn function for asking "do you want to attack" on dwarf
        
            if dwarfinput == 'y' or dwarfinput == 'Y' and dwarf_r == 2: #Here I used another random number, you can see above with the name dwarf_r which is for mighty swing
                print("You take a mighty swing at the dwarf with your stick")
                print()
                print("C R A C K ! ! ... you hit the dwarf, it's dead")
                print()
                print("Do you want to loot the body?")
                loot = yorn() #call yorn() function to get input from user.
                if loot == 'y' or loot == 'Y':
                    find_treasure("from Dwarf")

            elif dwarfinput == 'y' or dwarfinput == 'Y' and dwarf_r == 1: #If dwarf_r variable or random number = 1 then you will miss the target other wise you hit the dwarf
                print()
                print("You take a mighty swing at the dwarf with your stick")
                print("Whoosh! ... you miss the dwarf, but he runs away")
            elif dwarfinput == 'n' or dwarfinput == 'N':
                print("You let out a blood curdling scream, and run very fast!")    
                       
        elif dwarfappear == 2: #Here you can see if dwarfappear variable = 2 then dwarf will not appear
            print("-------------------------------------------------------------------------------")
            print("You continue to follow the cobblestone trail.")
            print()




def elves():
    from random import randint
    elves_r = (randint(1,2))# Here again I used randint for elf. 
    print()
    print("You come to what looks like the end of the 'road'. The trail splits and")
    print("there appears to be two strange looking houses here.")
    print()
    print("The first one, the left, is a very large and elaborate house. There")
    print("is a very 'fancy' elf standing in front!")
    print()
    print("The second house is very small and looks like it's about to fall over. There")
    print("is a very short elf standing in front!")
    print()
    print("Both seem to be beckoning you closer. which elf do you approach? The one by")
    print("the first house or the one by the second house?")
    print()
    while True:
        try: 
            elves_input = int(input("Choose an elf to approach (1 or 2)? "))
            print()
            if elves_r == 1 and elves_input == 1 or elves_r == 2 and elves_input == 2: #if user enter 1 and random number also 1 or user enter 2 and random number also 2 then elf invites you in. 
                print("you have chosen wisely!")
                print("... The elf invites you in for a cup of tea (and a gift) ")
                print()
                find_treasure('from elf')
                print("You have had a great adventure and found some amazing treasure")

            elif elves_r == 1 and elves_input == 2 or elves_input == 1 and elves_r == 2: # other then that if you input value not matched with random number then you choosed the bad elf.
                print()
                print("The elf starts to cackle, and begins to incant a spell")
                print()
                print("P O O F ! ! he turns you into a giant TOAD!!")
                print()
                print("You have had a great adventure and found some amazing treasure")
                print("... if you're not a giant toad!")
            
            if elves_input == 1 or elves_input == 2: break
        except ValueError:
            print('Please Enter 1 or 2')


intro()
print()
input('Press Enter to continue..')
potion = potion()
print(potion)
print()
input('Press Enter to continue..')
dwarf()
print()
input('Press Enter to continue..')
elves()
print()
print('Thanks for playing')
                



    



    
    
            
            
    
        
