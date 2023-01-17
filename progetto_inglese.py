# Impostazione delle librerie e/o liste----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#                                     
import climage                       
import random                        
import time                           
from colored import fg, bg, attr     
from playsound import playsound       
import pygame
from pygame import mixer              
#


enemy_pokemon_list = [ "Caterpie" , "Weedle" , "Pidgey" , "Rattata" , "Spearow" , "Ekans" , "Pikachu" , "Sandshrew" , "Nidoran♀" , "Nidoran♂" , "Mewtwo" , "Onix" , "Ponyta" , "Abra" , "Zubat" , "Vulpix" , "Jigglypuff" , "Oddish" , ]  
lp1 = 1

# Menù iniziale------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
pygame.init()                             
mixer.music.load("Opening.wav")           
mixer.music.play(-1)                     
mixer.music.set_volume(0.4)              
print("")
print(f"{fg(27)}{bg(220)}                                  ,'\                              {attr(0)}")
print(f"{fg(27)}{bg(220)}    _.----.        ____         ,'  _\   ___    ___     ____       {attr(0)}")
print(f"{fg(27)}{bg(220)}_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`. {attr(0)}")
print(f"{fg(27)}{bg(220)}\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |{attr(0)}")
print(f"{fg(27)}{bg(220)} \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |{attr(0)}")
print(f"{fg(27)}{bg(220)}   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |{attr(0)}")
print(f"{fg(27)}{bg(220)}    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |{attr(0)}")
print(f"{fg(27)}{bg(220)}     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |{attr(0)}")
print(f"{fg(27)}{bg(220)}      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |{attr(0)}")
print(f"{fg(27)}{bg(220)}       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |{attr(0)}")
print(f"{fg(27)}{bg(220)}        \_.-'       |__|    `-._ |              '-.|     '-.| |   |{attr(0)}")
print(f"{fg(27)}{bg(220)}                                `'                            '-._|{attr(0)}")

print(f"{fg(88)}╔═════════════════════════════════════════════════════════════════════╗{attr(0)}")
print(f"{fg(88)}║{bg(153)}                         {fg(196)}Welcome in Pokémon{attr(0)}{bg(153)}                        {attr(0)}{fg(99)}║{attr(0)}")
print(f"{fg(99)}╠═════════════════════════════════════════════════════════════════════╣{attr(0)}")
print(f"{fg(99)}║                                                                     ║{attr(0)}")
print(f"{fg(99)}║                This program simulates a pokémon card                ║{attr(0)}")
print(f"{fg(99)}║                           and some fights.                          ║{attr(0)}")
print(f"{fg(99)}║                                                                     ║{attr(0)}")
print(f"{fg(99)}║   Start by choosing one of the three starter pokémon to be able to  ║{attr(0)}")
print(f"{fg(99)}║                        start your adventure!                        ║{attr(0)}")
print(f"{fg(99)}║                                                                     ║{attr(0)}")
print(f"{fg(99)}╠═════════╗             Press ENTER to continue             ╔═════════╣{attr(0)}")
print(f"{fg(88)}║ ◓  ◓  ◓ {fg(99)}╠═════════╗                             ╔═════════╣{attr(0)}{fg(88)} ◓  ◓  ◓ ║{attr(0)}")
print(f"{fg(88)}╚═════════╩═════════{fg(99)}╩═════════════════════════════╩{attr(0)}{fg(88)}═════════╩═════════╝{attr(0)}")

print("Whenever you find something like '→ ' press enter to continue")
next=input('→ ')           
playsound("Archeo_Groudon.mp3")

mixer.music.stop()          
time.sleep(1)               

# Creazione personaggio-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
calem = climage.convert("CalemXY.png",  width=60,  is_unicode=True, is_truecolor=True, palette="default", is_8color=False, is_16color=False, is_256color=False)           
serena = climage.convert("SerenaXY.png",   width=60,  is_unicode=True, is_truecolor=True, palette="default", is_8color=False, is_16color=False, is_256color=False)                                     
pokemon_type_table = climage.convert("Pokemon_Type.png",   width=120,  is_unicode=True, is_truecolor=True, palette="default", is_8color=False, is_16color=False, is_256color=False)
print(pokemon_type_table)
mixer.music.load("ORAS_Birch_Lab.wav")
mixer.music.play(-1)
mixer.music.set_volume(0.4)

character = True
while character!="Boy" or character!="boy" or character!="BOY" or character!="B" or character!="b" or character!="Girl" or character!="girl" or character!="GIRL"  or character!="G" or character!="g":
    character=input("\nBefore we start, are you a boy or a girl?:")
    if character=="Boy" or character=="boy" or character=="BOY" or character=="B" or character=="b":
        print(calem)            
        break
    elif character=="Girl" or character=="girl" or character=="GIRL"  or character=="G" or character=="g":
        print(serena)           
        break
    else :
        print("Invalid input.")

player_name= True
while player_name!="n" or player_name!="no" or player_name!="No" or player_name!="NO" or player_name!="N":
    player_name=input("\nCan you remind me your name?:")

    if player_name=="n" or player_name=="no" or player_name=="No" or player_name=="NO" or player_name=="N":
        print("\nCome on be serious.")
        next=input('→ ')
    elif player_name == " " or player_name == "" :
        print("Invalid input.")
    else:
        print(f"\nNice! {player_name} Now you can start your adventure by choosing your first pokémon.")
        break
next=input('→ ')

# Scelta e creazione stats del pokémon--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
img_pokeball = climage.convert('sassari.png')      
print(img_pokeball)                               

print(f"                {fg(98)}CHOOSE A POKÉBALL TO GET YOUR FIRST POKÉMON{attr(0)}")
print(f"                                {fg(98)} 1 / 2 / 3 \n{attr(0)}")
pokeball="a"

while pokeball!="1" or pokeball!="2" or pokeball!="3": 
    pokeball = input("")
    print(f"Loading...")
    time.sleep(2)
    if player_name == "/administrator_N3rDiaz" or player_name == "/administrator_NicogiocTV" or player_name == "/administrator_deel" :
        print("Activating administrator privileges...")
        time.sleep(5)
        
        print("Administrator privileges activated.")
        next=input('→ ')
        pokemon="ᒲ╎ᓭᓭ╎リ ⊣リ𝙹"
        img_pokemon = climage.convert("missigno.png", is_unicode=True, is_truecolor=True, is_8color=False, is_16color=False, is_256color=False)
        print(img_pokemon)
        print(f"{fg(241)}╚═══════════════════════════════҉ {pokemon} ҉═════════════════════════════════╝{attr(0)}")
        pokemon_type="null"            
        break

    elif pokeball == "1":
        pokemon="Charmander"
        img_pokemon = climage.convert("Charmander.png", is_unicode=True, is_truecolor=True, is_8color=False, is_16color=False, is_256color=False)
        print(img_pokemon)
        print(f"{fg(196)}╚═══════════════════════════════🔥 {pokemon} 🔥═════════════════════════════════╝{attr(0)}")
        playsound("Charmander.mp3")   
        pokemon_type="Fire"            
        break

    elif pokeball == "2":
        pokemon="Squirtle"
        img_pokemon = climage.convert("Squirtle.png", is_unicode=True, is_truecolor=True, is_8color=False, is_16color=False, is_256color=False)
        print(img_pokemon)
        print(f"{fg(21)}╚═══════════════════════════════💧 {pokemon} 💧═════════════════════════════════╝{attr(0)}")
        playsound("Squirtle.mp3")
        pokemon_type="Water"
        break

    elif pokeball == "3":
        pokemon="Bulbasaur"
        img_pokemon = climage.convert("Bulbasaur.png", is_unicode=True, is_truecolor=True, is_8color=False, is_16color=False, is_256color=False)
        print(img_pokemon)
        print(f"{fg(28)}╚═══════════════════════════════🍃 {pokemon} 🍃════════════════════════════════╝{attr(0)}")
        playsound("Bulbasaur.mp3")
        pokemon_type="Grass"
        break

    else:
        print("\nInvalid input.\n")

pokemon_lvl=5                   
pokemon_exp=0                   


spe = random.randint(1,6)+random.randint(1,6)+random.randint(1,6)        # speed/velocità

att = random.randint(1,6)+random.randint(1,6)+random.randint(1,6)        # attack/attacco

dif = random.randint(1,6)+random.randint(1,6)+random.randint(1,6)        # defense/difesa   (def è un comando di python quindi non va bene come variabile)

satt = random.randint(1,6)+random.randint(1,6)+random.randint(1,6)       # special attack/attacco speciale

sdif = random.randint(1,6)+random.randint(1,6)+random.randint(1,6)       # special defense/difesa speciale

lp = 20+random.randint(1,6)+random.randint(1,6)+random.randint(1,6)      # life points/punti vita


if player_name == "/administrator_N3rDiaz" or player_name == "/administrator_NicogiocTV" or player_name == "/administrator_deel" :

    lp=9999
    att=9999
    satt=9999
    dif=9999
    sdif=9999
    spe=9999

    pokemon_lvl = 100



# Nome del pokémon----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
opz = True
while opz!="yes" or opz!="YES" or opz!="Yes" or opz!="no" or opz!="NO" or opz!="No":
    opz = input("\nDo you want to give it a name?: ")
    if opz=="yes" or opz=="YES" or opz=="Yes" or opz=="Y" or opz=="y":
        pokemon = input("\nWhat name do you want to give to your pokémon?: ")
        
        # stampa scheda del pokémon
        print(f"\n{fg(147)}╔═════════════════════════════════════════════════════════════════════╗{attr(0)}")
        print(f"{fg(147)}       {pokemon}'s Stats     Level: {pokemon_lvl}     Type: {pokemon_type}{attr(0)}")
        print(f"{fg(147)}╠═════════════════════════════════════════════════════════════════════╣{attr(0)}")
        print(f"{fg(147)}                           Life points: {lp}                                    {attr(0)}")
        print(f"{fg(147)}                           Attack {att}                                       {attr(0)}")
        print(f"{fg(147)}                           Defense {dif}                                        {attr(0)}")
        print(f"{fg(147)}                           Special attack {satt}                              {attr(0)}")
        print(f"{fg(147)}                           Special defense {sdif}                               {attr(0)}")
        print(f"{fg(147)}                           Speed {spe}                                      {attr(0)}")
        print(f"{fg(147)}╚═════════════════════════════════════════════════════════════════════╝{attr(0)}")
        break

    elif opz=="no" or opz=="NO" or opz=="No" or opz=="N" or opz=="n":

        # stampa scheda del pokémon
        print(f"\n{fg(147)}╔═════════════════════════════════════════════════════════════════════╗{attr(0)}")
        print(f"{fg(147)}     {pokemon}'s Stats     Level: {pokemon_lvl}     Type: {pokemon_type}{attr(0)}")
        print(f"{fg(147)}╠═════════════════════════════════════════════════════════════════════╣{attr(0)}")
        print(f"{fg(147)}                           Life points: {lp}                                    {attr(0)}")
        print(f"{fg(147)}                           Attack {att}                                       {attr(0)}")
        print(f"{fg(147)}                           Defense {dif}                                        {attr(0)}")
        print(f"{fg(147)}                           Special attack {satt}                              {attr(0)}")
        print(f"{fg(147)}                           Special defense {sdif}                               {attr(0)}")
        print(f"{fg(147)}                           Speed {spe}                                      {attr(0)}")
        print(f"{fg(147)}╚═════════════════════════════════════════════════════════════════════╝{attr(0)}")
        break
    else:
        print("\nInvalid input.\n")
next=input('→ ')    

info_type = input("Do you want to view the types your pokémon is super effective against or weak to?:")
if (info_type == "YES" or info_type == "Yes" or info_type == "yes" or info_type == "Y" or info_type == "y") and pokemon_type == "Fire":
    print("Fire-type is super effective on grass and bug pokémon")
    print("\nWhile it is not very effective on fire-type, rocks-type, ground-type and water-type pokémon")
    print("\nAnd rock, ground and water type pokemon are super effective for him")
    print("\nWhile on fire the grass and bug type pokemon are not very effective")

if (info_type == "YES" or info_type == "Yes" or info_type == "yes" or info_type == "Y" or info_type == "y") and pokemon_type == "Water":
    print("The water type is super effective on fire, ground, and rock pokémon")
    print("\nWhile it is not very effective on grass-type pokémon ")
    print("\nAnd electric and grass type pokemon are super effective for him")
    print("\nWhile on water the fire, earth and rock type pokemon are not very effective")

if (info_type == "YES" or info_type == "Yes" or info_type == "yes" or info_type == "Y" or info_type == "y") and pokemon_type == "Grass":
    print("The grass type is super effective on water and ground and rock pokémon")
    print("\nWhile it is not very effective on fire and electric type pokémon")
    print("\nAnd the bug and fire type pokemon are super effective at him")
    print("\nWhile fire-type pokemon are not very effective on grass")
if info_type == ""

next=input('→ ')
mixer.music.stop()
time.sleep(2)

# Inizio scontro------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
x = 0
choice_combat="yes"
while choice_combat != "no" or choice_combat != "NO" or choice_combat != "No" :
    if choice_combat == "yes" or choice_combat == "YES" or choice_combat == "Yes" or choice_combat == "y" or choice_combat == "Y" :
        fight = "a"

        enemy_pokemon = random.choice(enemy_pokemon_list)
        if lp1  <= 0 :
            print("We are healing your pokémon ...")
            playsound("Cura.mp3")
            print(f"We've restored your {pokemon} to full healt!")
            next=input('→ ')

        while fight!="yes" or fight!="YES" or fight!="Yes" or fight!="Y" or fight!="y":
            
            if x  == 0 :
                fight = input("You walk in the tall grass and you see a pokémon, do you want to fight it?: ")
            else:
                fight = "yes"
                print("You walk in the tall grass, watch out, that pokémon attacks you")
                time.sleep(2)
            if fight == "yes" or fight == "Yes" or fight == "YES" or fight=="Y" or fight=="y":
                print (f"{fg(126)}\nA wild {enemy_pokemon} has appeared!{attr(0)}")
                break

            elif fight == "no" or fight == "No" or fight == "NO" or fight=="N" or fight=="n":
                print("\nHey champ we are in a pokémon game, you are obligated to have at least one fight...")
                next =input('→ ')
                print (f"{fg(126)}\nA wild {enemy_pokemon} has appeared!{attr(0)}")
                break

            else:
                print("\nInvalid input.\n")

        
        # Creazione stats del pokémon avversario------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        enemy_pokemon_lvl=random.randint(1,10)

        espe = random.randint(1,6)+random.randint(1,6)+random.randint(1,6)        # enemy speed/velocità dell'avversario
      
        eatt = random.randint(1,6)+random.randint(1,6)+random.randint(1,6)        # enemy attack/attacco dell'avversario
        
        edif = random.randint(1,6)+random.randint(1,6)+random.randint(1,6)        # enemy defense/difesa dell'avversario  (def è un comando di python quindi non va bene come variabile)

        esatt = random.randint(1,6)+random.randint(1,6)+random.randint(1,6)       # enemy special attack/attacco speciale dell'avversario

        esdif = random.randint(1,6)+random.randint(1,6)+random.randint(1,6)       # enemy special defense/difesa speciale dell'avversario

        elp = 20+random.randint(1,6)+random.randint(1,6)+random.randint(1,6)      # enemy life points/punti vita dell'avversario


        match enemy_pokemon_lvl:
            case 2:
                espe=espe+1
                eatt=eatt+1
                edif=edif+1
                esatt=esatt+1
                esdif=esdif+1
                elp=elp+1
            case 3:
                espe=espe+1
                eatt=eatt+1
                edif=edif+1
                esatt=esatt+1
                esdif=esdif+1
                elp=elp+1
            case 4:
                espe=espe+2
                eatt=eatt+2
                edif=edif+2
                esatt=esatt+2
                esdif=esdif+2
                elp=elp+2
            case 5:
                espe=espe+2
                eatt=eatt+2
                edif=edif+2
                esatt=esatt+2
                esdif=esdif+2
                elp=elp+2
            case 6:
                espe=espe+3
                eatt=eatt+3
                edif=edif+3
                esatt=esatt+3
                esdif=esdif+3
                elp=elp+3
            case 7:
                espe=espe+3
                eatt=eatt+3
                edif=edif+3
                esatt=esatt+3
                esdif=esdif+3
                elp=elp+3
            case 8:
                espe=espe+3
                eatt=eatt+3
                edif=edif+3
                esatt=esatt+3
                esdif=esdif+3
                elp=elp+3
            case 9:
                espe=espe+3
                eatt=eatt+3
                edif=edif+3
                esatt=esatt+3
                esdif=esdif+3
                elp=elp+3
            case 10:
                espe=espe+4
                eatt=eatt+4
                edif=edif+4
                esatt=esatt+4
                esdif=esdif+4
                elp=elp+4

        enemy_pokemon_type = "a"
        match enemy_pokemon:
                    case "Zubat" | "Nidoran♂" | "Nidoran♀" | "Ekans":
                        enemy_pokemon_type = "Poison"
                    case "Mewtwo":
                        enemy_pokemon_type = "Psychic"

                        enemy_pokemon_lvl = 100
                        elp = 1000
                        eatt = 1000
                        edif = 1000         
                        esatt = 1000
                        esdif = 1000
                        espe = 1000

                    case "Abra":
                        enemy_pokemon_type = "Psychic"
                    case "Pidgey" | "Rattata" | "Spearow" | "Jigglypuff":
                        enemy_pokemon_type = "Normal"
                    case "Caterpie" | "Weedle":
                        enemy_pokemon_type = "Bug"
                    case "Sandshrew":
                        enemy_pokemon_type = "Ground"
                    case "Onix":
                        enemy_pokemon_type = "Rock"
                    case "Pikachu":
                        enemy_pokemon_type = "Electro"
                    case "Ponyta" | "Vulpix":
                        enemy_pokemon_type = "Fire"
                    case "Oddish":
                        enemy_pokemon_type = "Grass"
                    case _:
                        print("List Error")

        mixer.music.load("battle_ost.wav")
        mixer.music.play(-1)
        mixer.music.set_volume(0.4)
        time.sleep(2)
        print(f"{fg(196)}╔═════════════════════════════════════════════════════════════════════╗{attr(0)}")
        print(f"{fg(196)}      {enemy_pokemon}'s stats        Level: {enemy_pokemon_lvl}        Type: {enemy_pokemon_type}             {attr(0)}")
        print(f"{fg(196)}╠═════════════════════════════════════════════════════════════════════╣{attr(0)}")
        print(f"{fg(196)}                           Life points {elp}                                   {attr(0)}")
        print(f"{fg(196)}                           Attack {eatt}                                      {attr(0)}")
        print(f"{fg(196)}                           Defense {edif}                                       {attr(0)}")
        print(f"{fg(196)}                           Special Attack {esatt}                             {attr(0)}")
        print(f"{fg(196)}                           special Defense {esdif}                              {attr(0)}")
        print(f"{fg(196)}                           Speed {espe}                                     {attr(0)}")
        print(f"{fg(196)}╚═════════════════════════════════════════════════════════════════════╝{attr(0)}")

        next=input('→ ')

        # Efficacia dei tipi-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        modifier=1
        enemy_modifier=1
        if pokemon_type=="Fire" and enemy_pokemon_type=="Grass" or enemy_pokemon_type=="Bug":
            modifier=2
            enemy_modifier=0.5
        elif pokemon_type=="Fire" and enemy_pokemon_type=="Fire":
            modifier=0.5
            enemy_modifier=0.5
        elif pokemon_type=="Water" and enemy_pokemon_type=="Fire" or enemy_pokemon_type=="Ground" or enemy_pokemon_type=="Rock":
            modifier=2
            enemy_modifier=0.5
        elif pokemon_type=="Grass" and enemy_pokemon_type=="Wter" or enemy_pokemon_type=="Ground" or enemy_pokemon_type=="Rock":
            modifier=2
            enemy_modifier=0.5
        elif pokemon_type=="Grass" and enemy_pokemon_type=="Electro":
            enemy_modifier=0.5
        #--------------------------------------------------------------|             
        if enemy_pokemon_type=="Poison" and pokemon_type=="Grass":
            modifier=0.5
            enemy_modifier=2
        elif enemy_pokemon_type=="Bug" and pokemon_type=="Grass":
            enemy_modifier=2
        elif enemy_pokemon_type=="Ground" and pokemon_type=="Fire":
            modifier=0.5
            enemy_modifier=2
        elif enemy_pokemon_type=="Rock" and pokemon_type=="Fire":
            modifier=0.5
            enemy_modifier=2
        elif enemy_pokemon_type=="Electro" and pokemon_type=="Water":
            enemy_modifier=2
        elif enemy_pokemon_type=="Fire" and pokemon_type=="Grass":
            modifier=0.5
            enemy_modifier=2
        elif enemy_pokemon_type=="Grass" and pokemon_type=="Water":
            modifier=0.5
            enemy_modifier=2

        # Attacco------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        lp1 = lp
        while not(lp1<=0 or elp<=0):
            
            print(f"{fg(222)}\n╔═{lp1:.0f} I tuoi HP                                       HP avversario {elp:.0f}═╗{attr(0)}")
            print(f"{fg(222)}╠══════════════════════════════════╦══════════════════════════════════╣{attr(0)}")
            print(f"{fg(222)}║{attr(0)}{bg(53)}              Attack              {attr(0)}{fg(222)}║{attr(0)}{bg(53)}         Special Attack           {attr(0)}{fg(222)}║{attr(0)}")
            print(f"{fg(222)}╚════════════════╗1╔═══════════════╩═══════════════╗2╔════════════════╝{attr(0)}")
            print(f"{fg(222)}                   ║{bg(53)}              Run              {attr(0)}{fg(222)}║{attr(0)}")
            print(f"{fg(222)}                   ╚══════════════╗3╔══════════════╝{attr(0)}")
            option=input("\n════════════╣Choose your attack: ")
            power=30            
            
        
            if option=="Run" or option=="3":
                    print(f"Got away safely!")
                    time.sleep(2)
                    next =input('→ ')
                    mixer.music.stop()
                    break
            if spe >= espe :

                if option=="attack" or option=="1": 
                    miss_perc=random.randint(1,100)
                    print("It's your turn and you've chosen attack.")
                    if miss_perc < 90: 
                        dmg= ((((((2*pokemon_lvl)/5)+2)*power*att/edif)/50)+2)*modifier                
                        elp=elp-dmg                                                                                                    
                        time.sleep(1)

                        print(f"You have done {dmg:.0f} damage.")
                    else:
                        print("The opposing pokémon dodged the attack!")

                    i = 1
                elif option=="special attack" or option=="2":
                    print("It's your turn and you've chosen special attack.")
                    miss_perc=random.randint(1,100)
                    if miss_perc < 90: 
                        dmg= ((((((2*pokemon_lvl)/5)+2)*power*satt/esdif)/50)+2)*modifier
                        elp=elp-dmg
                        time.sleep(1)

                        print(f"You have done {dmg:.0f} damage.")
                    else:
                        print("The opposing pokémon dodged the attack!")
                    i = 2
                
                elif option == "":   
                    if  i == 1 :
                        print("ÈIt's your turn and you've chosen attack.")
                        miss_perc=random.randint(1,100) 
                        if miss_perc < 90: 
                            
                            dmg= ((((((2*pokemon_lvl)/5)+2)*power*att/edif)/50)+2)*modifier               
                            elp=elp-dmg                                                                                                     
                            time.sleep(1)
                            
                            print(f"You have done {dmg:.0f} damage.")
                        else:
                            print("The opposing pokémon dodged the attack!")
                    elif i == 2 :
                        print("It's your turn and you've chosen special attack.")
                        miss_perc=random.randint(1,100) 
                        if miss_perc < 90:  
                            dmg= ((((((2*pokemon_lvl)/5)+2)*power*satt/esdif)/50)+2)*modifier
                            elp=elp-dmg
                            time.sleep(1)
                            
                            print(f"You have done {dmg:.0f} damage.")
                        else:
                            print("The opposing pokémon dodged the attack!")
                print(f"{fg(222)}════════════════════════════════════════════════{attr(0)}")
                
                if elp<=0:
                    print(f"The opposing {enemy_pokemon} fainted!")
                    time.sleep(1)
                    battle_exp=random.randint(7, 36)
                    print(f"You have won the battle. Experience gained: {battle_exp}")
                    pokemon_exp=pokemon_exp+battle_exp
                    
                    break
                enemy_attack=random.randint(1,2)

                print(f"It's your opponent's turn!")
                time.sleep(1)
                
                if enemy_attack==1:
                    print(f"The opponent has chosen Attack!")
                    miss_perc=random.randint(1,100) 
                    if miss_perc < 90:
                        dmg= ((((((2*enemy_pokemon_lvl)/5)+2)*power*eatt/dif)/50)+2)*enemy_modifier
                        print(f"Your {pokemon} has taken {dmg:.0f} damage.")
                        lp1=lp1-dmg
                        time.sleep(1)

                    else:
                        print(f"{pokemon} dodged the attack!")
                    
                elif enemy_attack==2:
                    
                    print(f"The opponent has chosen Special Attack!") 
                    miss_perc=random.randint(1,100) 
                    if miss_perc < 90:
                        dmg= ((((((2*enemy_pokemon_lvl)/5)+2)*power*esatt/sdif)/50)+2)*enemy_modifier
                        time.sleep(1)
                        print(f"Your {pokemon} has taken {dmg:.0f} damage.")
                        
                        lp1=lp1-dmg
                    else:
                        print(f"{pokemon} dodged the attack!")
                print(f"{fg(222)}════════════════════════════════════════════════{attr(0)}")
                if lp1<=0:
                    print(f"Your pokemon has been defeated.")
                    time.sleep(1)
                
                    break 
            else:

                enemy_attack=random.randint(1,2)
                print(f"It's your opponent's turn!")
                time.sleep(1)
                
                if enemy_attack==1:
                    print(f"The opponent has chosen Attack!")
                    miss_perc=random.randint(1,100) 
                    if miss_perc < 90:
                        dmg= ((((((2*enemy_pokemon_lvl)/5)+2)*power*eatt/dif)/50)+2)*enemy_modifier
                        print(f"Your {pokemon} has taken {dmg:.0f} damage.")
                        lp1=lp1-dmg
                        time.sleep(1)

                    else:
                        print(f"{pokemon} dodged the attack!")
                    
                elif enemy_attack==2:
                    
                    print(f"The opponent has chosen Special Attack!") 
                    miss_perc=random.randint(1,100) 
                    if miss_perc < 90:
                        dmg= ((((((2*enemy_pokemon_lvl)/5)+2)*power*esatt/sdif)/50)+2)*enemy_modifier
                        time.sleep(1)
                        print(f"Your {pokemon} has taken {dmg:.0f} damage.")
                        
                        lp1=lp1-dmg
                    else:
                        print(f"{pokemon} dodged the attack!")
                print(f"{fg(222)}════════════════════════════════════════════════{attr(0)}")
                if lp1<=0:
                    print(f"Your pokemon has been defeated.")
                    time.sleep(1)
                
                    break 

                if option=="attack" or option=="1": 
                    miss_perc=random.randint(1,100)
                    print("It's your turn and you've chosen attack.")
                    if miss_perc < 90: 
                        dmg= ((((((2*pokemon_lvl)/5)+2)*power*att/edif)/50)+2)*modifier               
                        elp=elp-dmg                                                                                                     
                        time.sleep(1)

                        print(f"You have done {dmg:.0f} damage.")
                    else:
                        print("The opposing pokémon dodged the attack!")

                    i = 1
                elif option=="special attack" or option=="2":
                    print("It's your turn and you've chosen special attack.")
                    miss_perc=random.randint(1,100)
                    if miss_perc < 90: 
                        dmg= ((((((2*pokemon_lvl)/5)+2)*power*satt/esdif)/50)+2)*modifier
                        elp=elp-dmg
                        time.sleep(1)

                        print(f"You have done {dmg:.0f} damage.")
                    else:
                        print("The opposing pokémon dodged the attack!")
                    i = 2
                
                elif option == "":   
                    if  i == 1 :
                        print("ÈIt's your turn and you've chosen attack.")
                        miss_perc=random.randint(1,100) 
                        if miss_perc < 90: 
                            
                            dmg= ((((((2*pokemon_lvl)/5)+2)*power*att/edif)/50)+2)*modifier             
                            elp=elp-dmg                                                                                                     
                            time.sleep(1)
                            
                            print(f"You have done {dmg:.0f} damage.")
                        else:
                            print("The opposing pokémon dodged the attack!")
                    elif i == 2 :
                        print("It's your turn and you've chosen special attack.")
                        miss_perc=random.randint(1,100) 
                        if miss_perc < 90:  
                            dmg= ((((((2*pokemon_lvl)/5)+2)*power*satt/esdif)/50)+2)*modifier
                            elp=elp-dmg
                            time.sleep(1)
                            
                            print(f"You have done {dmg:.0f} damage.")
                        else:
                            print("The opposing pokémon dodged the attack!")
                print(f"{fg(222)}════════════════════════════════════════════════{attr(0)}")
                if elp<=0:
                    print(f"The opposing {enemy_pokemon} fainted!")
                    time.sleep(1)
                    battle_exp=random.randint(7, 36)
                    print(f"You have won the battle. Experience gained: {battle_exp}")
                    pokemon_exp=pokemon_exp+battle_exp
                    
                    break
        if pokemon_exp >= pokemon_exp + 100:
            pokemon_lvl=pokemon_lvl+1
            
            print(f"{pokemon} grew to level {pokemon_lvl}!")

            lp=lp+(lp/100*7)

            att=att+(att/100*7)

            dif=dif+(dif/100*7)

            satt=satt+(satt/100*7)

            sdif=sdif+(sdif/100*7)

            spe=spe+(spe/100*7)

        mixer.music.stop()    
    elif choice_combat == "NO" or choice_combat == "No" or choice_combat == "no" or choice_combat == "n" or choice_combat == "N" :
        break
    else:
        print("Invalid input.")
    x = 1
    choice_combat=input("Do you want to continue on the path?: ")
    if (choice_combat == "Yes" or choice_combat == "YES" or choice_combat == "yes" or choice_combat == "Y" or choice_combat == "y") and lp1 > 0: 
        healt_regen_choice = input("Prima di proseguire vuoi curare il tuo pokémon?: ")

        x = 1
        if healt_regen_choice == "Yes" or healt_regen_choice == "YES" or healt_regen_choice == "yes" or healt_regen_choice == "Y" or healt_regen_choice == "y" :
            print("We are taking care of your pokémon...")
            playsound("Cura.mp3")
            print("We've restored your {pokemon} to full healt!")

# Riconoscimenti----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
time.sleep(3)
print(f"{fg(103)}\n\n\n╔═══════════════Riconoscimanti═══════════════╗{attr(0)}")
print(f"{fg(103)}║                                            ║{attr(0)}")
print(f"{fg(103)}║                    ~~~~                    ║{attr(0)}")
print(f"{fg(103)}║             Executive producers            ║{attr(0)}")
print(f"{fg(103)}║                                            ║{attr(0)}")
print(f"{fg(103)}║                 Diego Amati                ║{attr(0)}")
print(f"{fg(103)}║               Nicola Tonelli               ║{attr(0)}")
print(f"{fg(103)}║                Paolo D'Elia                ║{attr(0)}")
print(f"{fg(103)}║                    ~~~~                    ║{attr(0)}")
print(f"{fg(103)}║                                            ║{attr(0)}")
print(f"{fg(103)}║          {fg(160)}Thank you for playing!{attr(0)}{fg(103)}            ║{attr(0)}")
print(f"{fg(103)}║                                            ║{attr(0)}")
print(f"{fg(103)}║                    ~~~~                    ║{attr(0)}")
print(f"{fg(103)}║                                            ║{attr(0)}")
print(f"{fg(103)}║   PKM Project   |   3M inc. © 2020-2023    ║{attr(0)}")
print(f"{fg(103)}║            All rights reserved             ║{attr(0)}")
print(f"{fg(103)}╚════════════════════════════════════════════╝{attr(0)}")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------