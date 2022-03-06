import random
import time
import sys
repeated_scenario=[""]
games=1
path=0
endgame=0
# --------------------------------------------------------------------------------------------------------------------------------------
def intro():
    global path
    global repeated_scenario
    print("You wake up due to your friend texting you and about 20 missed calls\nYou are groggy and tired from a long shift at work\nWhat will you do?")
    answer = input("Type '1' to Get Up or '2' to go back to Sleep.\n>> ")
    print("\033c", end="")
    if answer == "1":
        print("You decide to get up and venture out to meet your friends")
        print("You start walking towards town.")
        print("")
        time.sleep(0.75)
        random_scenario()
    elif answer == "2":
        print("You decide to have a lie in.\nYou fall back asleep. \nI'm sorry but it is the END of your night out. You can try again tomorrow.")
        end_function()
    else:
        print("")
        intro()
# --------------------------------------------------------------------------------------------------------------------------------------
def scenariob1():
    global path
    global repeated_scenario
    if "b1" in repeated_scenario:
        random_scenario()
    else:
        repeated_scenario.append("b1")
    print("You are walking down the road when a loud noise attracts your attention.\nIt is a Religious Preacher praising his deity and condemning you to suffering\nfor being out and not worshipping his deity at home.")
    print("Do you?\n ")
    answer=input("1- Engage in healthy debate to challenge his beliefs.\n2- Walk on by and pretend not to listen.\n3- Listen as you walk by\n")
    print("\033c", end="")
    if answer=="1":
        print("You engage him in debate and time pass before you realise you have argued for too long and won't make it to the club before closing. \nI'm sorry but it is the END of your night out. You can try again tomorrow.")
        end_function()
    elif answer=="2":
        answer=random.randint(0,1)
        if answer==0:
            print("You pretend not to listen but he makes a compelling argument. You have converted to his faith and go home to pray. \nI'm sorry but it is the END of your night out. You can try again tomorrow.")
            end_function()
        else:
            print("You are focused on the great night out and barely hear his condemnation.\nYou carry on towards the club...")
            path+=1
            time.sleep(1)
            random_scenario()
    elif answer=="3":
        print("You walk past listening to his arguments and realise he is an idiot.\nYou carry on towards the club...")
        path+=1
        time.sleep(1)
        random_scenario()
    else:
        repeated_scenario.pop()
        print("You need to make a decision quickly before he stops you for a discussion...")
        scenariob1()
# --------------------------------------------------------------------------------------------------------------------------------------
def scenariob2():
    global path
    global repeated_scenario
    if "b2" in repeated_scenario:
        random_scenario()
    else:
        repeated_scenario.append("b2")
    print("You are walking down the road when a loud noise attracts your attention.\nIt is group of hooded youths on bikes.")
    print("Do you?\n ")
    answer=input("1- Run as fast as you can.\n2- Approach them and ask for directions.\n3- Calmly keep walking and ignore them.\n")
    print("\033c", end="")
    if answer=="1":
        print("They chase you on their bikes and catch up to you, they attack and rob you before leaving you at the side of the road.\nYou wake up in A&E three days later. \nI'm sorry but it is the END of your night out. You can try again tomorrow.")
        end_function()
    elif answer=="2":
        answer=random.randint(0,1)
        if answer==0:
            print("They attack and rob you before leaving you in the alley.\nYou wake up in A&E three days later. \nI'm sorry but it is the END of your night out. You can try again tomorrow.")
            end_function()
        else:
            print("They helpfully give you directions to make your journey faster.\nYou carry on towards the club...")
            path+=2
            time.sleep(1)
            random_scenario()
    elif answer=="3":
        print("You walk past not glancing over and they ignore you.\nYou carry on towards the club...")
        path+=1
        time.sleep(1)
        random_scenario()
    else:
        repeated_scenario.pop()
        print("You need to make a decision quickly or they will smell your fear and attack...")
        scenariob2()
# --------------------------------------------------------------------------------------------------------------------------------------
def scenariob3():
    global path
    global repeated_scenario
    if "b3" in repeated_scenario:
        random_scenario()
    else:
        repeated_scenario.append("b3")
    print("You are walking down the road when a loud noise and flashing blue lights attract your attention.\nIt is a couple having an argument and a police officer trying to sort it out.\nThey are on both sides of the road and it could erupt into a fight any second.")
    print("Do you?\n ")
    answer=input("1- Help out the police officer.\n2- Walk on by and pretend not to listen.\n3- Try to walk down the center of the road.\n")
    print("\033c", end="")
    if answer=="2":
        print("As you try to walk by, the lady grabs you and explains her long situation to you,\nWhile you try to unentangle yourself you trip and fall ending up in A&E. \nI'm sorry but it is the END of your night out. You can try again tomorrow.")
        end_function()
    elif answer=="1":
        answer=random.randint(0,1)
        if answer==0:
            print("You help the police officer defuse the situation but it ends up taking you to the early morning to make a statement. You won't reach the club in time. \nI'm sorry but it is the END of your night out. You can try again tomorrow.")
            end_function()
        else:
            print("You help out the police officer and the couple acrimoniously depart in different directions,\nthe police officer drives off leaving you alone.\nYou carry on towards the club...")
            path+=1
            time.sleep(1)
            random_scenario()
    elif answer=="3":
        print("You walk past as they shout around you.\nYou carry on towards the club...")
        path+=1
        time.sleep(1)
        random_scenario()
    else:
        repeated_scenario.pop()
        print("You need to make a decision quickly before you get caught up in this...")
        scenariob3()
# --------------------------------------------------------------------------------------------------------------------------------------
def scenariob4():
    global path
    global repeated_scenario
    if "b4" in repeated_scenario:
        random_scenario()
    else:
        repeated_scenario.append("b4")
    print("You are walking down the road but come to a police cordon across the road; you see no police cars.")
    print("Do you?\n ")
    answer=input("1- wait for a police officer.\n2- duck under the police cordon.\n3- head back on yourself and try another route.\n")
    print("\033c", end="")
    if answer=="1" or answer=="2":
        ranswer=random.randint(0,5)
        if ranswer>0 and answer=="1":
            print("You are waiting a long time and end up reaching the club too late. \nI'm sorry but it is the END of your night out. You can try again tomorrow.")
            end_function()
        elif ranswer>0 and answer=="2":
            print("You duck quickly under the cordon and sprint for the other side, a police officer emerges from a building and chases you down, you are taken to the station and miss your mates at the club. \nI'm sorry but it is the END of your night out. You can try again tomorrow.")
            end_function()
        elif ranswer==0 and answer=="1":
            print("A police officer emerges and helpfully gives you directions to make your journey faster but you have to go back on yourself.\nYou carry on towards the club...")
            path+=1
            time.sleep(1)
            random_scenario()
        elif ranswer==0 and answer=="2":
            print("You duck under the police cordon and sprint for the other side, you make it just as a police officer emerges from one of the buildings. You carry on towards the club.")
            path+=1
            time.sleep(1)
            random_scenario()
        else:
            print("error!!!!")
    elif answer=="3":
        print("You begrudgingly turn around and head back the way you came, a quick two turns later and\nYou carry on towards the club...")
        time.sleep(1)
        random_scenario()
    else:
        repeated_scenario.pop()
        print("You need to make a decision quickly or they will smell your fear and attack...")
        scenariob4()
# --------------------------------------------------------------------------------------------------------------------------------------
def scenariob5():
    global path
    global repeated_scenario
    if "b5" in repeated_scenario:
        random_scenario()
    else:
        repeated_scenario.append("b5")
    print("You are walking down the road but see a stranger walking the opposite way; he smiles at you.")
    print("Do you?\n ")
    answer=input("1- Smile back.\n2- Try to avoid eye contact and walk faster.\n3- Cross over the road and keep walking\n")
    print("\033c", end="")
    if answer=="1":
        print("The stranger nods and keeps walking, you glance back but he has kept walking.\nYou carry on towards the club...")
        path+=1
        time.sleep(1)
        random_scenario()
    elif answer=="2":
        print("The stranger looks disappointed but keeps walking.\nYou carry on towards the club...")
        path+=1
        time.sleep(1)
        random_scenario()
    elif answer=="3":
        print("The stranger seems disappointed but keeps walking.\nYou carry on towards the club...")
        path+=1
        time.sleep(1)
        random_scenario()
    else:
        repeated_scenario.pop()
        print("You need to make a decision quickly or they will smell your fear and attack...")
        scenariob5()
# --------------------------------------------------------------------------------------------------------------------------------------
def jan():
    global repeated_scenario
    if "Jan" in repeated_scenario:
        random_scenario()
    else:
        repeated_scenario.append("Jan")
    # Intro
    def first():
        print("\nYou walked a bit and found yourself in the Baltic Market.\nFew people come out from behind the corner.")
        print("They all wear masks. \nLead by a guy in a mask of Donald Trump.")
        print("One of them wears a mask of a bat, an other wears mask of a snake.")
        print("Next person wears mask of a mouse.\nThey all come runnning after you!\n\n")
        input("Press ENTER to continue...>\n\n")
        print("\033c", end="")
        print("While the group surround you so you can't escape,")
        print('the Bat, Snake and the Mouse shout at you: "Yo, yo. You\'re gonna get sick, laaa!!!"')
        print("You get scared, but you can't run away, because closed gate and tall fence is behind you!")
        print("However, Donald Trump offers you a vaccine!\n\n")
        choice()
    # Initial 2 Choices - positive + neutral than negative
    def choice():
        print("\nWhat will you do??? \nType 1 to speak to Trump or 2 to deal with the mouse, the snake and the bat.\n\n")
        answer = input("Your choice is?...> ")
        print("\033c", end="")
        if answer == "1":
            print("\n")
            print("Trump pulls out a syringe with the vaccine and puts a needle on.")
            print('Are you a doctor?... you ask...\n"No", replies Trump.\nYou: So what\'s in the syringe?')
            print('"It\'s a nice surprise!!! Don\'t worry, we tested it." Replies Trump.')
            print('"...and apart from that it is mandatory laa." adding to that and laughs.\n')
            vaccine()
        elif answer == "2":
            fightSMB()
        else:
            choice()
    #Choice of getting vaccine or not - sub choice positive + neutral outcome
    def vaccine():
        global path
        print("\nIf you want to take the vaccine type 1, if you want to refuse, type 2.\n\n")
        vaccine_answer = input("Make choice...> ")
        print("\033c", end="")
        if vaccine_answer == "1": #positive outcome
            print("\n\nYou have rolled up your sleeve up and Trump applied the vaccine.")
            print("You have been injected with a dose of not further specified class A drug.")
            print('"You go out and enjoy your night pal!", says Trump.')
            input("You ask: Who the hell are you?\n\n...hit ENTER to get answer...>\n")
            print("\033c", end="")
            print('"I do this gig for charity lad...and my re-election campaign!" Replies Trump.')
            print('"If you like it, give me a buzz" he adds and the Snake passed you a business card')
            print("However the drug has started to kick in and you feel ecstatic!")
            print("You thank Trump and get on your way despite mild but pleasant halucinations.\n\n")
            print("\n\nYou shug and slowly carry on towards the club...")
            input("Hit ENTER to Continue...")
            print("\033c", end="")
            path+=1
            random_scenario()
        elif vaccine_answer == "2": #neutral outcome
            print("\033c", end="")
            print("Bat, Mouse and Snake approach you and all start spitting on you.")
            print("You have problems to deflect their attack!\nYou open your mouth and shout \"Stop it!!!\"")
            print("In that moment spit from the Snake landed in your mounth.")
            print("You have swallowed the spit. \nThis made you terribly sick and you started to projectile vomit.")
            print("You have vomited all over the attackers.")
            print("You now deflected the attack but you feel really under the weather.")
            print("\n\n\nBut you carry on slowly towards the club...")
            input("Hit ENTER to Continue...")
            print("\033c", end="")
            path+=1
            random_scenario()
        else:
            vaccine()
    # fighting snake, mouse and bat scene  - negative outcome
    def fightSMB():
        print("\n\nSnake grabs you around your body and squeezes your belly with force!")
        print("You can\'t move and the mouse started to nibble on your arm!")
        print("Bat takes down the mask. \nIt's a very pretty scouse girl and she smiles at you and winks.")
        print('"It was just for a laugh!" she says and passes you a bottle of fine Czech lager.')
        print("You all start laughing.\n\n")
        input("Hit ENTER to continue...>\n\n")
        print("\033c", end="")
        print("They all take of their masks and you start chatting. They offer you a spare mask of Boris Johnson.")
        print("Bat, the pretty girl, asks you to come with them.")
        print("You decide to stick with them and put the mask of Boris on.")
        print("You laugh at the situation, but suddenly, a drunk scouser spotted you.")
        print("The scouser comes running after you and smashes a bottle of Stella againt your head...")
        print("...shouting \"Stitch it up you tory scum!!!\"...unaware it's just a mask.\n\n")
        print("You manage to withstand the blast but your face is covered by blood.\n\n")
        brawl()
    def brawl():
        global path
        print("Do you keep cool or fight with the scouser??? Press 1 to keep your cool or 2 to fight.\n\n")
        fight_answer = input("Enter a 1 or 2 to continue...> \n\n")
        print("\033c", end="")
        if fight_answer == "2": #positive outcome - leading back to the streets
            print("\n\nScouser looks next to you and punches Trump as a next logical step.\nTrump drops the syringe.")
            print("Scouser, still confused who is who, notices the syringe, stops fighting and grabs the syringe.")
            print("He rolls up his black hoodie and stubs the syringe in his arm")
            print("His face comes up with terrible grin and drops on the floor")
            print("Trump gets up looking at the body of the scouser on the floor saying,")
            print('"Hope he had covid, because he just wasted all my bleach in one go!!!"')
            print("You run away to the streets before the police arrives\n\n")
            path+=1
            random_scenario()
        elif fight_answer == "1": #negative outcome - mission fail
            print("\033c", end="")
            print("You stay in the brawl with the scouser, till the police arrives at the scene.")
            print("You are all arrested for possession of a class A drug that was in the syringe and an assault.")
            print("They put you all in a cage with the Bat, Mouse, Snake and the scouser")
            print("Your mission has failed!\n")
            print("Later you will catch covid.")
            print("Surprisingly, not from the Bat, the Snake or the Mouse from the Baltic Market...")
            print("...but from the scouser.\n")
            end_scenario()
        else:
            brawl()
        end_function()
    first()
# --------------------------------------------------------------------------------------------------------------------------------------
def john():
    global path
    global repeated_scenario
    global endgame
    if "john" in repeated_scenario:
        random_scenario()
    else:
        repeated_scenario.append("john")
    print("Taking the side street you see a group of lads on bikes.\nWill you find another way around them or walk through?")
    # Choices
    print("Type '1' to walk through them,\n'2' to find a way around them on the left side or\n'3' for another way around them on the right side\n\nthere is a 4th option by typing in '4'.")
    answer = input(">> ")
    print("\033c", end="")
    if answer == "1":
        print("You decide to walk through the group of lads and get harrassed by them and get battered by them for not giving them a ciggy or money.")
        print("BAD END")
        end_function()
    elif answer == "2":
        print("You decide to find another way around the group of lads to another street.\nYou carry on towards the club...")
        path+=1
        random_scenario()
    elif answer == "3":
        print("The noise fades as you make your way down the road to the right nothing bizarrely happens until you reach the mainstreet,\nwhere traffic is at a standstill and something strange is happening, a velociraptor is looking confused as to what is going on,\nyou decide to help the velociraptor find its way but first you ask it to tag along. \nYou and the Velociraptor decide to go to the nearest pub and get a takeaway and become friends over a pint.\n\nMe and my Dino friend Ending")
        endgame=1
        end_function()
    elif answer == "4":
        print("After walking a good while you come to several pubs you vaguely hear your friends?\nAs you move closer you can tell that by the terrible singing, you meet up with your mates and they seem to be happy to see you and wondering why you aint drinking.\n\nBest End?")
        endgame=1
        end_function()
    else:
        repeated_scenario.pop()
        print("You typed the wrong input. FissionMailed\n\n")
        john()
# --------------------------------------------------------------------------------------------------------------------------------------
def matt():
    #scenario intro
    global path
    global repeated_scenario
    if "matt" in repeated_scenario:
        random_scenario()
    else:
        repeated_scenario.append("matt")
    print("100 meters along the street you hear a group of voices eminating from an alley you have just walked past.\nThe voices sound agitated and agressive and from the increasing volume you deduce they are getting closer.\nJust ahead of you there is a bright red electric scooter, parked on its stand outside an ajar door.\n ")
    time.sleep(1.5)
    print("Do you?\n1. Choose to just keep walking.\n2. Jump on the scooter and speed away.\n3. Dart into the open door and hide inside.\n")
    time.sleep(1.5)
    answer = input("Enter your choice 1,2 or 3.\n")
    print("\033c", end="")
    #option 1 positive outcome
    if answer == "1":
        print("You keep walking, maybe unconciuosly picking up your pace slightly. The voices behind you materialise on\nthe street and turn to head in your direction, but the shiny red scooter is too much for them to resist and they\ndisappear into the shadows with their haul. You continue on your way in peace.\nYou carry on towards the club...")
        path+=1
        random_scenario()
    #option 2
    elif answer == "2":
        print("You jump on the scooter, click on the power and get ready to try your first ever ride on an electric scooter.")
        time.sleep(1.0)
        print("As you figure out that is has a twist throttle just like a motorbike, one of the voices roars out... \n\n")
        time.sleep(0.5)
        print("Oi! get off my scooter.\n\n")
        time.sleep(0.5)
        print("Half a dozen other voices burst out with varying shouts,\nnone of which seem to be good for your health \n\n")
        time.sleep(0.5)
        print("How is your first ride going to go")
        time.sleep(0.5)
        input("Press ENTER to role the dice of fate...")
        # character by charcter rollling
        print ("rolling")
        words = "........"
        for char in words:
            time.sleep(0.3)
            sys.stdout.write(char)
            sys.stdout.flush()
        # scenarion random outcomes
        if random.randint(0, 10) > 3:
            print("The charge indicator has just 1 red bar left but the scooter lurches forward and throws\nitself off the curb landing cleanly on both wheels. The sound of a dozen or more trainers rapidly hitting\ntarmac starts to close on you at first but after a few seconds you are flying in a more or less straight\nline leaving the gang well behind.\n\nYou were lucky.")
            time.sleep(1.5)
            print("This time")
            path+=1
            random_scenario()
        elif random.randint(0, 10) < 3:
            print("The charge indicator has just 1 red bar left but the scooter lurches forward and throws\nitself of the curb landing at 45 degrees before sliding away from underneath you. Your knee hits\nthe ground hard accompanied by a loud snapping noise. The gang descend upon you and before\nrecovering their scooter they add a few more injuries for you to have patched up during what is\ngoing to be a long night in A & E.")
            time.sleep(1.5)
            print("┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼")
            print("███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀")
            print("██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼")
            print("██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀")
            print("██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼")
            print("███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄")
            print("┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼")
            print("███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼")
            print("██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼")
            print("██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼")
            print("██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼")
            print("███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄")
            print("┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼")
            print("┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼")
            print("┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼")
            print("┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼")
            print("┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼")
            print("┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼")
            print("┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼")
            print("┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼")
            print("┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼")
            print("┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼")
            print("┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼")
            print("┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼")
            print("┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼")
            end_function()
    # option 3 negative outcome      
    elif answer == "3":
        print("After closing the door behind you, a light turns on and you are greeted by Maynard. Bound and\ngagged on the floor you hear him on the 'phone calling someone called Zed")
        time.sleep(1.5)
        print("┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼")
        print("███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀")
        print("██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼")
        print("██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀")
        print("██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼")
        print("███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄")
        print("┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼")
        print("███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼")
        print("██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼")
        print("██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼")
        print("██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼")
        print("███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄")
        print("┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼")
        print("┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼")
        print("┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼")
        print("┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼")
        print("┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼")
        print("┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼")
        print("┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼")
        print("┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼")
        print("┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼")
        print("┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼")
        print("┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼")
        print("┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼")
        print("┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼")
        end_function()
    # player error
    else:
        repeated_scenario.pop()
        print("Please enter a valid option. it is 1, 2 or 3. This isn't rocket science.")
        time.sleep(0.2)
        print("I am waiting")
        matt()
# --------------------------------------------------------------------------------------------------------------------------------------
def toni():
    global path
    global repeated_scenario
    if "toni" in repeated_scenario:
        random_scenario()
    else:
        repeated_scenario.append("toni")
    print("You're not quite sure how you got here but you find yourself walking down a dimly lit street.\nAhead of you, you can hear the not so distant sounds of Saturday night Liverpool.\nYou reach for your phone to check if you've missed any messages from your mates,\nbut as you do so you notice what appears to be a small green man dashing down an alleyway to your right.\nDo you?\n")
    print("Enter 1 to: Think to yourself that you probably should have eaten more before you had those drinks,\nand decide the sensible thing to do is just keep walking. You're nearly there.\nEnter 2 to: Chase the 'little green man' down the alleyway. \nPress 3 to: Think to yourself that you are hallucinating and should probably go home to sleep it off.\n")
    answer = input("Please enter your choice: ")
    print("\033c", end="")
    if answer == "1":
        print("You choose to walk on. You didn't see anything. This is a completely normal night.")
        random_scenario()
    elif answer == "2":
        print("You chase the little green man down the alleyway. You reach him just in time to see him\nclimb into what, in the moment, you believe to be a spaceship.")
        val=random.randint(0,10)
        if val > 5:
            print("As you get closer you realise the little green man was actually a dog in a high visibility\njacket, and the spaceship - a wheelie bin. It turns on you with snarling teeth. Luckily, you realise in time\nand sprint back to the road. Give yourself a shake to wake up a bit and carry on down the road.")
            path=+1
            random_scenario()
        elif val != 10:
            print("You manage to reach the little green man before he climbs into his spaceship. You reach\nout to grab him, at which point you realise that the little green man was, in fact, a dog in a high visibility\njacket and the spaceship - a wheelie bin. The dog turns on you as you grab it and sinks its teeth deep into your\nhand. Looks like you're off to A&E. Night ruined.\nGAME OVER.")
            end_function()
        else:
            print("You catch up to the little green man and he offers you a trip to his homeworld for drinks with HIS mates")
            answer=input("1- to accept his offer. \n2- to refuse his offer and carry on to the club. \n3- to take him with you to the club.")
            print("\033c", end="")
            if answer=="1":
                print("You are whisked away to a far off planet for the night, his alien club is buzzing\nbut you remember little when you wake up three days later at home.")
                end_function()
            elif answer=="2":
                print("He seems very disappointed but lets you go, knowing no-one will believe you anyway.\nYou carry on towards the club...")
                path+=1
                random_scenario()
            else:
                print("Annoyed the alien shoots you with his raygun and you wake up in A&E three days later. \nI'm sorry but it is the END of your night out. You can try again tomorrow.")
                end_function()
    elif answer == "3":
        print("You clearly aren't feeling with it tonight. Maybe next week. You head home and get an early night.")
        print(" \nI'm sorry but it is the END of your night out. You can try again tomorrow.")
        end_function()
    else:
        repeated_scenario.pop()
        print("Please choose 1, 2, or 3. Thanks!")
        toni()
# --------------------------------------------------------------------------------------------------------------------------------------
def end_scenario():
    print("Congratulations, You have made it to A club, it looks lively, you see a group waving outside the club.\nWhat do you want to do?\n")
    final_answer=input("1- Head over to them\n2- Head to another club instead\n")
    print("\033c", end="")
    if final_answer=="1":
        final_randomise=random.randint(0,2)
        if final_randomise==0:
            print("They are your mates and you have arrived in time, you have a great night out\nbut you remember little when you wake up home three days later")
            end_function()
        elif final_randomise==1:
            print("They are not your mates but get you in the club regardless. You have a great night out\nbut remember little when you wake up home three days later")
            end_function()
        elif final_randomise==2:
            print("They are not your mates, an argument breaks out and you wake up in police custody three days later. \nI'm sorry but it is the END of your night out. You can try again tomorrow.")
            end_function()
        else:
            end_scenario()
    elif final_answer=="2":
        final_randomise=random.randint(0,1)
        if final_randomise==0:
            print("You have a great night out but you remember little when you wake up home three days later")
            end_function()
        elif final_randomise==1:
            print("You find a new club, entering is fine but an argument breaks out.\nYou wake up in police custody three days later. \nI'm sorry but it is the END of your night out. You can try again tomorrow.")
            end_function()
        else:
            end_scenario()
    else:
        end_scenario()
# --------------------------------------------------------------------------------------------------------------------------------------
def end_function():
    global path
    global repeated_scenario
    global games
    global endgame
    time.sleep(2.5)
    print("\n\n\nThanks for playing our game, with contributions from Barry Hughes, Jan Kresina, John Wardale, Matt Sloan, Toni Castaglioni\nand of course Demi for her Teaching, Relaxing attitude and most of all Patience!")
    time.sleep(1)
    if endgame==1:
        print("\033c", end="")
        if Demi_scenario()=="Demi":
            print("You don't get a vote in this Demi")
        else:
            print("Of course she's the best!")
            time.sleep(1)
    else:
        print("")
    print("Do you want to play again, 1- Yes, or any key to end.")
    if input("\n >>")=="1":
        print("\033c", end="")
        print("Great, enjoy")
        games+=1
        print(games)
        repeated_scenario=[""]
        path=0
        intro()
    else:
        print("Ok, Goodbye!")
        quit()
# --------------------------------------------------------------------------------------------------------------------------------------
def Demi_scenario():
    return input("Is Demi the best tutor?\n1-Yes\n2-No\n").capitalize()
    # I told you I'd use it ^.^ (return)
# --------------------------------------------------------------------------------------------------------------------------------------
scenario_list = [scenariob1, scenariob2, scenariob3, scenariob4, scenariob5, jan, john, matt, toni]
def random_scenario():
    if path>=(2**2):
    #I told you I'd use it ^.^ (**)
        print("\033c", end="")
        end_scenario()
    else:
        random.choice(scenario_list)()
        # this is the random function
# --------------------------------------------------------------------------------------------------------------------------------------
intro()