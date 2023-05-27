def game_e():
    # Impostazione delle librerie e/o liste----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #                                     # LIBRERIE UTILIZZATE:
    import climage                        # utilizzo la libreria Climage per stampare a schermo delle immagini (ATTENZIONE: le immagini devono essere scaricate, avere lo stesso nome dichiarato nel programma e trovarsi nella stessa cartella del programma (stessa cosa vale per i file audio usati con le altre librerie).
    import random                         # importo la libreria random per utilizzare i numeri randomici
    import time                           # utilizzo la libreria time con il suo comando "time.sleep" per mettere in pausa il programma per un certo numero di secondi
    from colored import fg, bg, attr      # utilizzo le funzioni "fg" (foreground, per il colore del testo), "bg" (background, per lo sfondo), e "attr" (per interrompere i comandi precedenti) del modulo Colored.
    from playsound import playsound       # utilizzo la libreria playsound per utilizzare file audio nel programma. ATTENZIONE: la versione installata automaticamente di playsound potrebbe dare problemi con alcuni file audio quindi abbiamo installato una versione precedente (nel cmd basta fare "pip install playsound==1.2.2")
    import pygame
    from pygame import mixer              # importo la funzione "mixer" dalla libreria pygame per riprodurre il file audio in background. Pygame è una libreria potente e potrebbe fare molte cose, ma a noi serve solo per la colonna sonora
    import webbrowser                     # la libreria webbrowser serve per aprire pagine web
    import pyfiglet                       # utilizzo la libreria "pyfiglet" per poter trasformare una stringa in textart
    import numpy as np
    import loot_table                     # importo il file di gestione degli oggetti
    #                                     \\\\\\\\\\# https://github.com/NicogiocTV/Progetto-pazzo-maniaco -----> link GitHub per scaricare tutti i file necessari per l'esecuzione.

    inv = np.array(["potion", "super potion", "hyper potion","max potion","breadboard"])
    invn = [0,0,0,0,0]
    stick = [0,0,0,0,0,0,0,0,0,0,0,0]

    # Dichiaro le funzioni------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def save(player_name, character, pokemon, pokemon_exp, pokemon_lvl, pokemon_type, lp, att, dif, satt, sdif, spe):       # funzione per il salvataggio dei dati
        print("Saving...")
        time.sleep(2)
        save_list = [player_name, character, pokemon, str(pokemon_exp), str(pokemon_lvl), pokemon_type, str(lp), str(att), str(dif), str(satt), str(sdif), str(spe)]
        f = open("salvataggi.txt", "w")     # il programma crea la cartella "salvataggi.txt" o la apre e la sovrascrive se esite già
        for i in range(len(save_list)):
            f.write(save_list[i] + "\n")    # salva una variabile per riga nel file di testo
        f.close()                           # chiude il file
        print("Downloaded successfully.")

    def cura(tot_life):                     # funzione che gestisce la salute del proprio pokémon quando si usa una pozione
        print("What do you want to use between a Potion, Super Potion, Hyper Potion or Max Potion.")
        type_heal=input()
        global heal

        if type_heal == "potion" or type_heal=="Potion" or type_heal=="POTION":
            heal = 30
            invn[0]=invn[0]-1
            playsound("heal_sound.mp3")
            print("Your pokémon has recovered 30 HP.")

        elif type_heal == "super potion" or type_heal=="Super Potion" or type_heal=="SUPER POTION":
            heal = 60
            invn[1]=invn[1]-1
            playsound("heal_sound.mp3")
            print("Your pokémon has recovered 60 HP.")

        elif type_heal == "hyper potion" or type_heal=="Hyper Potion" or type_heal=="HYPER POTION":
            heal = 120
            invn[2]=invn[2]-1
            playsound("heal_sound.mp3")
            print("Your pokémon has recovered 120 HP.")

        elif type_heal == "max potion" or type_heal=="Max Potion" or type_heal=="MAX POTION":
            heal = tot_life
            invn[3]=invn[3]-1
            playsound("heal_sound.mp3")
            print("Your pokémon is back in full force.")

    def damage(pokemon_lvl, power, stat_1, stat_2, modifier):
        global dmg
        dmg= ((((((2*pokemon_lvl)/5)+2)*power*stat_1/stat_2)/50)+2)*modifier    # https://wiki.pokemoncentral.it/Danno -----> il metodo per calcolare il Danno (cioè la quantità di Life Points da sottrarre ad ogni attacco) lo abbiamo preso dalla formula originale dei veri giochi Pokémon.

    def stats(s_pokemon, s_pokemon_lvl, s_pokemon_type, s_lp, s_att, s_dif, s_satt, s_sdif, s_spe):
        print(f"\n{fg(147)}╔═════════════════════════════════════════════════════════════════════╗{attr(0)}")
        print(f"{fg(147)}             {s_pokemon}'s Stats     Level: {s_pokemon_lvl}     Type: {s_pokemon_type}{attr(0)}")
        print(f"{fg(147)}╠═════════════════════════════════════════════════════════════════════╣{attr(0)}")
        print(f"{fg(147)}                           Life Points ❤️  {s_lp}                                    {attr(0)}")
        print(f"{fg(147)}                           Attack ⚔️  {s_att}                                       {attr(0)}")
        print(f"{fg(147)}                           Defense 🛡 {s_dif}                                        {attr(0)}")
        print(f"{fg(147)}                           Special Attack ✨ {s_satt}                              {attr(0)}")
        print(f"{fg(147)}                           Special Defense 🔮 {s_sdif}                               {attr(0)}")
        print(f"{fg(147)}                           Speed ⚡ {s_spe}                                      {attr(0)}")
        print(f"{fg(147)}╚═════════════════════════════════════════════════════════════════════╝{attr(0)}")

    def lvl_up(pokemon_exp, pokemon_lvl, pokemon, lp, att, dif, satt, sdif, spe):   # funzione in caso il pokémon salga di livello
        if pokemon_exp >= 100:                        
            pokemon_exp = 0
            pokemon_lvl=pokemon_lvl+1

            playsound("lvl_sound.mp3")
            print(f"{pokemon}  leveled up {pokemon_lvl}!")

            lp=lp+(lp/100*7)

            att=att+(att/100*7)

            dif=dif+(dif/100*7)

            satt=satt+(satt/100*7)

            sdif=sdif+(sdif/100*7)

            spe=spe+(spe/100*7)
        return pokemon_lvl, pokemon_exp
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    enemy_pokemon_list = [ "Caterpie" , "Weedle" , "Pidgey" , "Rattata" , "Spearow" , "Ekans" , "Pikachu" , "Sandshrew" , "Nidoran♀" , "Nidoran♂" , "Mewtwo" , "Onix" , "Ponyta" , "Abra" , "Zubat" , "Vulpix" , "Jigglypuff" , "Oddish" , ]  
    lp1 = 1


    # Menù iniziale------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    pygame.init()                             # inizializzo pygame
    mixer.music.load("Opening.wav")           # carico il file audio
    mixer.music.play(-1)                      # inizia la musica (fra parentesi il numero di volte da riprodurre il file, -1 è in loop)
    mixer.music.set_volume(0.4)               # regolazione del volume
    print("")
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
    print("")
    print("")
    print(f"{fg(88)}╔═════════════════════════════════════════════════════════════════════╗{attr(0)}")
    print(f"{fg(88)}║{bg(153)}                         {fg(196)}Welcome in Pokémon{attr(0)}{bg(153)}                          {attr(0)}{fg(99)}║{attr(0)}")
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
    next=input('→ ')           # questa variabile serve per "fermare" il programma, il programma continua una volta che l'utente dà la conferma semplicemente premendo invio (come nei veri giochi Pokémon).
    playsound("Archeo_Groudon.mp3")
    mixer.music.stop()         # fermo la musica
    time.sleep(1)              # il comando serve per fermare il programma e poi farlo ripartire dopo il numero di secondi specificati fra parentesi

    saves = input("Want to load a game? ")
    if saves == "yes" or saves=="y" or saves=="YES" or saves=="Y" or saves=="Yes":
        z = open("salvataggi.txt", "r")
        stick = z.readlines()
        z.close()
        
        player_name = stick[0].strip()  # Rimuovi spazi bianchi e caratteri di nuova riga
        character = stick[1].strip()
        pokemon = stick[2].strip()
        pokemon_exp = int(stick[3].strip())  # Converti in intero
        pokemon_lvl = int(stick[4].strip())
        pokemon_type = stick[5].strip()
        lp = int(stick[6].strip())
        att = int(stick[7].strip())
        dif = int(stick[8].strip())
        satt = int(stick[9].strip())
        sdif = int(stick[10].strip())
        spe = int(stick[11].strip())

        stats(pokemon, pokemon_lvl, pokemon_type, lp, att, dif, satt, sdif, spe)
    else:
        # Creazione personaggio-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        calem = climage.convert("CalemXY.png",  width=60,  is_unicode=True, is_truecolor=True, palette="default", is_8color=False, is_16color=False, is_256color=False)          # converte l'immagine in formato ANSI e gli assegna una variabile, 
        serena = climage.convert("SerenaXY.png",   width=60,  is_unicode=True, is_truecolor=True, palette="default", is_8color=False, is_16color=False, is_256color=False)                                     # questa è la conversione delle immagini dei due personaggi giocabili
        mixer.music.load("ORAS_Birch_Lab.wav")
        mixer.music.play(-1)
        mixer.music.set_volume(0.4)
        character = True
        while character!="Male" or character!="male" or character!="MALE" or character!="M" or character!="m" or character!="Female" or character!="female" or character!="FEMALE"  or character!="F" or character!="f":
            character=input("\nBefore we start, are you a male or a female?: ")
            if character=="Male" or character=="male" or character=="MALE" or character=="M" or character=="m":
                print(calem)            # stampa l'immagine a schermo
                break
            elif character=="Female" or character=="female" or character=="FEMALE"  or character=="F" or character=="f":
                print(serena)           # stampa l'immagine a schermo
                break
            else:
                print("input invalid.")
        player_name= True
        while player_name!="n" or player_name!="no" or player_name!="No" or player_name!="NO" or player_name!="N":
            player_name=input("\nCan you remind me your name?: ")
            if player_name=="n" or player_name=="no" or player_name=="No" or player_name=="NO" or player_name=="N":
                print("\nCome on be serious...")
                next=input('→ ')
            elif player_name == " " or player_name == "" :
                print("input invalid")
            else:
                print(f"\nNice! {player_name} Now you can start your adventure by choosing your first pokémon.")
                break
        next=input('→ ')
        # Scelta e creazione stats del pokémon--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        img_pokeball = climage.convert('sassari.png')       # converte l'immagine in formato ANSI e gli assegna una variabile
        print(img_pokeball)                                 # stampa l'immagine a schermo
        print(f"              {fg(98)}CHOOSE A POKÉBALL TO GET YOUR FIRST POKÉMON{attr(0)}")
        print(f"                                {fg(98)} 1 / 2 / 3 \n{attr(0)}")
        pokeball="a"
        while pokeball!="1" or pokeball!="2" or pokeball!="3": 
            pokeball = input("")
            if player_name == "/administrator_N3rDiaz" or player_name == "/administrator_NicogiocTV" or player_name == "/administrator_deel" :
                print("Activating administrator privileges...")
                time.sleep(5)
                print("Administrator privileges activated.")
                next=input('→ ')
                pokemon="ᒲ╎ᓭᓭ╎リ ⊣リ𝙹"
                playsound("pokeball_out_sound.mp3")
                img_pokemon = climage.convert("missigno.png", is_unicode=True, is_truecolor=True, is_8color=False, is_16color=False, is_256color=False)
                print(img_pokemon)
                print(f"{fg(241)}╚═══════════════════════════════҉ {pokemon} ҉═════════════════════════════════╝{attr(0)}")
                pokemon_type="null"            # il "tipo" è una caratteristica (o elemento se vogliamo) che possiede ogni Pokémon e le mosse; ogni tipo è più o meno efficace su un altro
                break
            elif pokeball == "1":
                pokemon="Charmander"
                playsound("pokeball_out_sound.mp3")
                img_pokemon = climage.convert("Charmander.png", is_unicode=True, is_truecolor=True, is_8color=False, is_16color=False, is_256color=False)
                print(img_pokemon)
                print(f"{fg(196)}╚═══════════════════════════════🔥 {pokemon} 🔥═════════════════════════════════╝{attr(0)}")
                playsound("Charmander.mp3")     # riproduce il "verso" del pokémon
                pokemon_type="Fire"            # il "tipo" è una caratteristica (o elemento se vogliamo) che possiede ogni Pokémon e le mosse; ogni tipo è più o meno efficace su un altro
                break
            elif pokeball == "2":
                pokemon="Squirtle"
                playsound("pokeball_out_sound.mp3")
                img_pokemon = climage.convert("Squirtle.png", is_unicode=True, is_truecolor=True, is_8color=False, is_16color=False, is_256color=False)
                print(img_pokemon)
                print(f"{fg(21)}╚═══════════════════════════════💧 {pokemon} 💧═════════════════════════════════╝{attr(0)}")
                playsound("Squirtle.mp3")
                pokemon_type="Water"
                break
            elif pokeball == "3":
                pokemon="Bulbasaur"
                playsound("pokeball_out_sound.mp3")
                img_pokemon = climage.convert("Bulbasaur.png", is_unicode=True, is_truecolor=True, is_8color=False, is_16color=False, is_256color=False)
                print(img_pokemon)
                print(f"{fg(28)}╚═══════════════════════════════🍃 {pokemon} 🍃════════════════════════════════╝{attr(0)}")
                playsound("Bulbasaur.mp3")
                pokemon_type="Grass"
                break
            else:
                print("\ninput invalid.\n")
        pokemon_lvl=5                   # livello del pokémon
        pokemon_exp=0                   # esperienza del pokémon guadagnata in battaglia per salire di livello
        spe = random.randint(1,6)+random.randint(1,6)+random.randint(1,6)        # speed/velocità
        att = random.randint(1,6)+random.randint(1,6)+random.randint(1,6)        # attack/attacco
        dif = random.randint(1,6)+random.randint(1,6)+random.randint(1,6)        # defense/difesa
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
        while opz!="yes" or opz!="YES" or opz!="Yes" or opz!= "y" or opz!= "Y" or opz!="no" or opz!="NO" or opz!="No" or opz!= "n" or opz!= "N":
            opz = input("\nDo you want to give it a name?: ")
            
            if opz=="yes" or opz=="YES" or opz=="Yes" or opz=="Y" or opz=="y":
                pokemon = input("\nWhat name do you want to give to your pokémon?: ")
                stats(pokemon, pokemon_lvl, pokemon_type, lp, att, dif, satt, sdif, spe)     # stampa scheda del pokémon
                break
            elif opz=="no" or opz=="NO" or opz=="No" or opz=="N" or opz=="n":
                stats(pokemon, pokemon_lvl, pokemon_type, lp, att, dif, satt, sdif, spe)     # stampa scheda del pokémon
                break
            else:
                print("\ninput invalid.")

        next=input('→ ')    
        info_type = input("Do you want to view the types your pokémon is super effective against or weak to?: ")
        if info_type == "YES" or info_type == "Yes" or info_type == "yes" or info_type == "Y" or info_type == "y":
            pokemon_type_table="https://pwtng.altervista.org/wp-content/uploads/2017/08/tipi.png"
            webbrowser.open(pokemon_type_table)
        mixer.music.stop()      # ferma la musica
        time.sleep(2)
    # Inizio scontro------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    tot_life = lp
    x = 0
    prob = 0
    a = 0
    choice_combat="yes"
    while choice_combat != "no" or choice_combat != "NO" or choice_combat != "No" or choice_combat == "n" or choice_combat == "N" :
        if choice_combat == "yes" or choice_combat == "YES" or choice_combat == "Yes" or choice_combat == "y" or choice_combat == "Y" :
            fight = "a"
            enemy_pokemon = random.choice(enemy_pokemon_list)
            if lp1  <= 0 :
                print("We are healing your pokémon ...")
                playsound("Cura.mp3")
                print(f"We've restored your {pokemon} to full health!")
                next=input('→ ')
            while fight!="yes" or fight!="YES" or fight!="Yes" or fight!="Y" or fight!="y":
                prob == random.randint(1, 10)
                if prob > 6:
                    drop, index_drop=loot_table.loot_eng()
                    playsound("item_sound.mp3")
                    print(f"Oh! You found a {drop} in a pokéball!")
                    invn[index_drop] = invn[index_drop] + 1

                elif prob <= 6:
                    if x  == 0 :
                        fight = input("You walk through the tall grass and you see a pokémon, do you want to fight it? ")
                    else:
                        fight = "yes"
                        print("You walk through the tall grass, watch out, a pokémon attacks you! ")
                        time.sleep(2)
                    if fight == "yes" or fight == "Yes" or fight == "YES" or fight=="Y" or fight=="y":
                        print (f"{fg(126)}\nA wild {enemy_pokemon} has appeared!{attr(0)}")
                        break
                    elif fight == "no" or fight == "No" or fight == "NO" or fight=="N" or fight=="n":
                        print("\nHey champ we are in a pokémon game, you must have at least one fight...")
                        next =input('→ ')
                        print (f"{fg(126)}\nA wild {enemy_pokemon} has appeared!{attr(0)}")
                        break
                    else:
                        print("\ninput invalid\n")
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
                            edif = 1000         # Mewtwo è uno dei pokémon più forti e infatti non dovrebbe nemmeno essere questi
                            esatt = 1000
                            esdif = 1000
                            espe = 1000
                        case "Abra":
                            enemy_pokemon_type = "Psico"
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
            mixer.music.load("battle_ost.wav")  # carica la musica del combattimento
            mixer.music.play(-1)                # parte la musica
            mixer.music.set_volume(0.4)         # settaggio del volume
            time.sleep(2)

            stats(enemy_pokemon, enemy_pokemon_lvl, enemy_pokemon_type, elp, eatt, edif, esatt, esdif, espe)
            next=input('→ ')
            # Efficacia dei tipi-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            def efficacy_types(pokemon_type, enemy_pokemon_type):
                global modifier
                modifier = 1
                global enemy_modifier
                enemy_modifier = 1
                if pokemon_type=="Fire" and enemy_pokemon_type=="Grass" or enemy_pokemon_type=="Bug":
                    modifier=2
                    enemy_modifier=0.5
                elif pokemon_type=="Fire" and enemy_pokemon_type=="Fire":
                    modifier=0.5
                    enemy_modifier=0.5
                elif pokemon_type=="Water" and enemy_pokemon_type=="Fire" or enemy_pokemon_type=="Ground" or enemy_pokemon_type=="Rock":
                    modifier=2
                    enemy_modifier=0.5
                elif pokemon_type=="Grass" and enemy_pokemon_type=="Water" or enemy_pokemon_type=="Ground" or enemy_pokemon_type=="Rock":
                    modifier=2
                    enemy_modifier=0.5
                elif pokemon_type=="Grass" and enemy_pokemon_type=="Electro":
                    enemy_modifier=0.5
                #--------------------------------------------------------------|             # https://wiki.pokemoncentral.it/Tipo -----> Per fare i Superefficace/Poco Efficace dei tipi abbiamo consultato la wiki ufficiale del gioco
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
            efficacy_types(pokemon_type, enemy_pokemon_type)
            # Attacco------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            lp1 = lp
            while not(lp1<=0 or elp<=0):
                def combat_menu(lp1, elp):
                    print(f"{fg(222)}\n╔═{lp1:.0f} Your HP's                                            Enemy HP {elp:.0f}═╗{attr(0)}")
                    print(f"{fg(222)}╠══════════════════════════════════╦══════════════════════════════════╣{attr(0)}")
                    print(f"{fg(222)}║{attr(0)}{bg(53)}              Attack              {attr(0)}{fg(222)}║{attr(0)}{bg(53)}          Special Attack          {attr(0)}{fg(222)}║{attr(0)}")
                    print(f"{fg(222)}╠════════════════╗1╔═══════════════╬═══════════════╗2╔════════════════╣{attr(0)}")
                    print(f"{fg(222)}║{attr(0)}{bg(53)}                Run               {attr(0)}{fg(222)}║{attr(0)}{bg(53)}               Bag                {attr(0)}{fg(222)}║{attr(0)}")
                    print(f"{fg(222)}╚════════════════╗3╔═══════════════╩═══════════════╗4╔════════════════╝{attr(0)}")
                    global option
                    option=input("\n════════════╣Choose your attack: ")
                combat_menu(lp1, elp)
                power=30            # potenza della mossa, che in questo caso mettiamo 30 di base sia per attacchi fisici che speciali
                if option=="4" or option=="bag":
                    cura(tot_life)
                    print(heal)
                    lp1=lp1 + heal
                    if lp1 > lp:
                        lp1=lp
                if option=="run" or option=="3":
                        print(f"Got away safely!")
                        time.sleep(2)
                        next =input('→ ')
                        mixer.music.stop()
                        break
                if spe >= espe :
                    if option=="attack" or option=="1": 
                        miss_perc=random.randint(1,100)
                        print("It's your turn and you've chosen Attack.")
                        if miss_perc < 90:
                            damage(pokemon_lvl, power, att, edif, modifier)
                            elp=elp-dmg
                            time.sleep(1)
                            print(f"You have done {dmg:.0f} damage.")
                        else:
                            print("The enemy pokémon dodged the attack!")
                        i = 1
                    elif option=="special attack" or option=="2":
                        print("It's your turn and you've chosen Special Attack.")
                        miss_perc=random.randint(1,100)
                        if miss_perc < 90:
                            damage(pokemon_lvl, power, satt, esdif, modifier)
                            elp=elp-dmg
                            time.sleep(1)
                            print(f"You have done {dmg:.0f} damage.")
                        else:
                            print("The enemy pokémon dodged the attack!")
                        i = 2
                    elif option == "":   
                        if  i == 1 :
                            print("It's your turn and you've chosen Attack.")
                            miss_perc=random.randint(1,100) 
                            if miss_perc < 90: 
                                damage(pokemon_lvl, power, att, edif, modifier)
                                elp=elp-dmg
                                time.sleep(1)
                                print(f"You have done {dmg:.0f} damage.")
                            else:
                                print("The enemy pokémon dodged the attack!")
                        elif i == 2 :
                            print("It's your turn and you've chosen Special Attack.")
                            miss_perc=random.randint(1,100) 
                            if miss_perc < 90:
                                damage(pokemon_lvl, power, satt, esdif, modifier)
                                elp=elp-dmg
                                time.sleep(1)
                                print(f"You have done {dmg:.0f} damage.")
                            else:
                                print("The enemy pokémon dodged the attack!")
                    print(f"{fg(222)}════════════════════════════════════════════════{attr(0)}")
                    if elp<=0:
                        print(f"The enemy {enemy_pokemon} fainted!")
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
                            damage(pokemon_lvl, power, eatt, dif, enemy_modifier)
                            print(f"Your {pokemon} has taken {dmg:.0f} damage.")
                            lp1=lp1-dmg
                            time.sleep(1)
                        else:
                            print(f"{pokemon} dodged the attack!")
                    elif enemy_attack==2:
                        print(f"The opponent has chosen Special Attack!") 
                        miss_perc=random.randint(1,100) 
                        if miss_perc < 90:
                            damage(pokemon_lvl, power, esatt, sdif, enemy_modifier)
                            time.sleep(1)
                            print(f"Your {pokemon} has taken {dmg:.0f} damage.")
                            lp1=lp1-dmg
                        else:
                            print(f"{pokemon} dodged the attack!")
                    print(f"{fg(222)}════════════════════════════════════════════════{attr(0)}")
                    if lp1<=0:
                        print(f"Your pokémon has been defeated.")
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
                            damage(pokemon_lvl, power, eatt, dif, enemy_modifier)
                            print(f"Your {pokemon} has taken {dmg:.0f} damage.")
                            lp1=lp1-dmg
                            time.sleep(1)
                        else:
                            print(f"{pokemon} dodged the attack!")
                    elif enemy_attack==2:
                        print(f"The opponent has chosen Special Attack!")
                        miss_perc=random.randint(1,100) 
                        if miss_perc < 90:
                            damage(pokemon_lvl, power, esatt, sdif, enemy_modifier)
                            print(f"Your {pokemon} has taken {dmg:.0f} damage.")
                            time.sleep(1)
                            lp1=lp1-dmg
                        else:
                            print(f"{pokemon} dodged the attack!")
                    print(f"{fg(222)}════════════════════════════════════════════════{attr(0)}")
                    if lp1<=0:
                        print(f"Your pokémon has been defeated.")
                        time.sleep(1)
                        break
                    if option=="attack" or option=="1":  
                        print("It's your turn and you've chosen Attack.")
                        miss_perc=random.randint(1,100) 
                        if miss_perc < 90:
                            damage(pokemon_lvl, power, att, edif, modifier)
                            elp=elp-dmg
                            time.sleep(1)
                            print(f"You have done {dmg:.0f} damage.")
                        else:
                            print("The enemy pokémon dodged the attack!")
                        i = 1
                    elif option=="special attack" or option=="2":
                        print("It's your turn and you've chosen Special Attack.")
                        miss_perc=random.randint(1,100) 
                        if miss_perc < 90:
                            damage(pokemon_lvl, power, satt, esdif, modifier)
                            elp=elp-dmg
                            time.sleep(1)
                            print(f"You have done {dmg:.0f} damage.")
                        else:
                            print("The enemy pokémon dodged the attack!")
                        i = 2
                    elif option == "":   
                        if  i == 1 :
                            print("It's your turn and you've chosen Attack.")
                            miss_perc=random.randint(1,100) 
                            if miss_perc < 90:
                                damage(pokemon_lvl, power, att, edif, modifier)
                                elp=elp-dmg
                                time.sleep(1)
                                print(f"You have done {dmg:.0f} damage.")
                            else:
                                print("The enemy pokémon dodged the attack!")
                        elif i == 2 :
                            print("It's your turn and you've chosen Special Attack.")
                            miss_perc=random.randint(1,100) 
                            if miss_perc < 90:
                                damage(pokemon_lvl, power, satt, esdif, modifier)
                                elp=elp-dmg
                                time.sleep(1)
                                print(f"You have done {dmg:.0f} damage.")
                            else:
                                print("The enemy pokémon dodged the attack!")
                        print(f"{fg(222)}════════════════════════════════════════════════{attr(0)}")
                    if elp<=0:
                        print(f"The enemy {enemy_pokemon} fainted!")
                        time.sleep(1)
                        battle_exp=random.randint(7, 36)
                        print(f"You have won the battle. Experience gained: {battle_exp}")
                        pokemon_exp=pokemon_exp+battle_exp
                        break
                    
            pokemon_lvl, pokemon_exp = lvl_up(pokemon_exp, pokemon_lvl, pokemon, lp, att, dif, satt, sdif, spe)

            mixer.music.stop()    
        elif choice_combat == "NO" or choice_combat == "No" or choice_combat == "no" or choice_combat == "n" or choice_combat == "N" :
            break
        else:
            print("input invalid.")
        x = 1
        choice_combat=input("Do you want to continue on the path? ")
        if (choice_combat == "Yes" or choice_combat == "YES" or choice_combat == "yes" or choice_combat == "Y" or choice_combat == "y") and lp1 > 0: 
            healt_regen_choice = input("Do you want to heal your pokémon first? ")
            x = 1
            if healt_regen_choice == "Yes" or healt_regen_choice == "YES" or healt_regen_choice == "yes" or healt_regen_choice == "Y" or healt_regen_choice == "y" :
                print("We are taking care of your pokémon...")
                playsound("Cura.mp3")
                print(f"We've restored your {pokemon} to full health!")
        save(player_name, character, pokemon, pokemon_exp, pokemon_lvl, pokemon_type, lp, att, dif, satt, sdif, spe)