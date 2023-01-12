# Impostazione dei moduli e/o liste----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import climage                         # utilizzo il modulo Climage per stampare a schermo delle immagini (ATTENZIONE: le immagini devono essere scaricate, avere lo stesso nome dichiarato nel programma e trovarsi nella stessa cartella del programma).
import random
import time                            # utilizzo il modulo time per 
from colored import fg, bg, attr       # utilizzo le funzioni "fg" (foreground, per il colore del testo), "bg" (background, per lo sfondo), e "attr" (per interrompere i comandi precedenti) del modulo Colored.

enemy_pokemon_list = [ "Caterpie" , "Weedle" , "Pidgey" , "Rattata" , "Spearow" , "Ekans" , "Pikachu" , "Sandshrew" , "Nidoran♀" , "Nidoran♂" , "Mewtwo" , "Onix" , "Ponyta" , "Abra" , "Zubat" , "Vulpix" , "Jigglypuff" , "Oddish" , ]  
enemy_pokemon = random.choice(enemy_pokemon_list)

# Menù iniziale------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print(f"{fg(88)}╔═════════════════════════════════════════════════════════════════════╗{attr(0)}")
print(f"{fg(88)}║{bg(153)}                         {fg(196)}Benvenuto in Pokémon{attr(0)}{bg(153)}                        {attr(0)}{fg(99)}║{attr(0)}")
print(f"{fg(99)}╠═════════════════════════════════════════════════════════════════════╣{attr(0)}")
print(f"{fg(99)}║                                                                     ║{attr(0)}")
print(f"{fg(99)}║          Questo programma simula la scheda di un pokémon            ║{attr(0)}")
print(f"{fg(99)}║                     e alcuni combattimenti.                         ║{attr(0)}")
print(f"{fg(99)}║                                                                     ║{attr(0)}")
print(f"{fg(99)}║     Inizia col scegliere uno dei tre pokémon iniziali per poter     ║{attr(0)}")
print(f"{fg(99)}║                      iniziare la tua avventura!                     ║{attr(0)}")
print(f"{fg(99)}║                                                                     ║{attr(0)}")
print(f"{fg(99)}╠═════════╗            Premi ENTER per continuare           ╔═════════╣{attr(0)}")
print(f"{fg(88)}║ ◓  ◓  ◓ {fg(99)}╠═════════╗                             ╔═════════╣{attr(0)}{fg(88)} ◓  ◓  ◓ ║{attr(0)}")
print(f"{fg(88)}╚═════════╩═════════{fg(99)}╩═════════════════════════════╩{attr(0)}{fg(88)}═════════╩═════════╝{attr(0)}")

next=input()            # questa variabile serve per "fermare" il programma, il programma continua una volta che l'utente dà la conferma semplicemente premendo invio (come nei veri giochi Pokémon).
print(f"Caricamento...")
time.sleep(1)           # il comando serve per fermare il programma e poi farlo ripartire dopo il numero di secondi specificati fra parentesi
# Creazione personaggio-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
calem = climage.convert("CalemXY.png",  width=60,  is_unicode=True, is_truecolor=True, palette="default", is_8color=False, is_16color=False, is_256color=False)          # converte l'immagine in formato ANSI e gli assegna una variabile, 
serena = climage.convert("SerenaXY.jpg",   width=60,  is_unicode=True, is_truecolor=True, palette="default", is_8color=False, is_16color=False, is_256color=False)                                     # questa è la conversione delle immagini dei due personaggi giocabili

character ="a"
while character!="Maschio" or character!="maschio" or character!="MASCHIO" or character!="M" or character!="m" or character!="Femmina" or character!="femmina" or character!="FEMMINA"  or character!="F" or character!="f":
    character=input("\nPrima di iniziare, sei maschio o femmina?: ")
    if character=="Maschio" or character=="maschio" or character=="MASCHIO" or character=="M" or character=="m":
        print(calem)            # stampa l'immagine a schermo
        break
    elif character=="Femmina" or character=="femmina" or character=="FEMMINA"  or character=="F" or character=="f":
        print(serena)           # stampa l'immagine a schermo
        break
    else :
        print("input invalido.")

player_name=input("\nMi puoi ricordare il tuo nome?: ")
print("\nBene! Adesso puoi iniziare la tua avventura scegliendo il tuo primo pokémon.")

next=input()
# Scelta e creazione stats del pokémon--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
img_pokeball = climage.convert('sassari.png')       # converte l'immagine in formato ANSI e gli assegna una variabile
print(img_pokeball)                                 # stampa l'immagine a schermo

print(f"              {fg(98)}SCEGLI UNA POKÉBALL PER RICEVERE IL TUO PRIMO POKÉMON{attr(0)}")
print(f"                                {fg(98)} 1 / 2 / 3 \n{attr(0)}")

pokeball="a"
while pokeball!="1" or pokeball!="2" or pokeball!="3": 
    pokeball = input("")
    print(f"Caricamento...")
    time.sleep(2)
    if pokeball == "1":
        pokemon="Charmander"
        img_pokemon = climage.convert("Charmander.png", is_unicode=True, is_truecolor=True, is_8color=False, is_16color=False, is_256color=False)
        print(img_pokemon)
        print(f"{fg(196)}╚═══════════════════════════════🔥 {pokemon} 🔥═════════════════════════════════╝{attr(0)}")
        pokemon_type="Fuoco"            # il "tipo" è una caratteristica (o elemento se vogliamo) che possiede ogni Pokémon e le mosse; ogni tipo è più o meno efficace su un altro
        break
    elif pokeball == "2":
        pokemon="Squirtle"
        img_pokemon = climage.convert("Squirtle.png", is_unicode=True, is_truecolor=True, is_8color=False, is_16color=False, is_256color=False)
        print(img_pokemon)
        print(f"{fg(21)}╚═══════════════════════════════💧 {pokemon} 💧═════════════════════════════════╝{attr(0)}")
        pokemon_type="Acqua"
        break
    elif pokeball == "3":
        pokemon="Bulbasaur"
        img_pokemon = climage.convert("Bulbasaur.png", is_unicode=True, is_truecolor=True, is_8color=False, is_16color=False, is_256color=False)
        print(img_pokemon)
        print(f"{fg(28)}╚═══════════════════════════════🍃 {pokemon} 🍃════════════════════════════════╝{attr(0)}")
        pokemon_type="Erba"
        break
    else:
        print("\ninput invalido.\n")

pokemon_lvl=5                   # livello del pokémon
pokemon_exp=0                   # esperienza del pokémon guadagnata in battaglia per salire di livello


spe=random.randint(1,6)
spe=spe+random.randint(1,6)         # speed/velocità
spe=spe+random.randint(1,6)

att=random.randint(1,6)
att=att+random.randint(1,6)         # attack/attacco
att=att+random.randint(1,6)

dif=random.randint(1,6)
dif=dif+random.randint(1,6)         # defense/difesa   (def è un comando di python quindi non va bene come variabile)
dif=dif+random.randint(1,6)

satt=random.randint(1,6)
satt=satt+random.randint(1,6)       # special attack/attacco speciale
satt=satt+random.randint(1,6)

sdif=random.randint(1,6)
sdif=sdif+random.randint(1,6)       # special defense/difesa speciale
sdif=sdif+random.randint(1,6)

lp=20+random.randint(1,6)
lp=lp+random.randint(1,6)           # life points/punti vita
lp=lp+random.randint(1,6)

# Nome del pokémon----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
opz = "a"
while opz!="si" or opz!="SI" or opz!="Si" or opz!="no" or opz!="NO" or opz!="No":
    opz = input("\nVuoi dargli un nome?: ")
    if opz=="si" or opz=="SI" or opz=="Si" or opz=="S" or opz=="s":
        pokemon = input("\nChe nome vuoi dare al tuo pokémon?: ")
        
        # stampa scheda del pokémon
        print(f"\n{fg(147)}╔═════════════════════════════════════════════════════════════════════╗{attr(0)}")
        print(f"{fg(147)}        Statistiche di {pokemon}     Livello: {pokemon_lvl}     Tipo: {pokemon_type}{attr(0)}")
        print(f"{fg(147)}╠═════════════════════════════════════════════════════════════════════╣{attr(0)}")
        print(f"{fg(147)}                           Punti Vita {lp}                                    {attr(0)}")
        print(f"{fg(147)}                           Attacco {att}                                       {attr(0)}")
        print(f"{fg(147)}                           Difesa {dif}                                        {attr(0)}")
        print(f"{fg(147)}                           Attacco Speciale {satt}                              {attr(0)}")
        print(f"{fg(147)}                           Difesa Speciale {sdif}                               {attr(0)}")
        print(f"{fg(147)}                           Velocità {spe}                                      {attr(0)}")
        print(f"{fg(147)}╚═════════════════════════════════════════════════════════════════════╝{attr(0)}")
        break

    elif opz=="no" or opz=="NO" or opz=="No" or opz=="N" or opz=="n":

        # stampa scheda del pokémon
        print(f"\n{fg(147)}╔═════════════════════════════════════════════════════════════════════╗{attr(0)}")
        print(f"{fg(147)}        Statistiche di {pokemon}     Livello: {pokemon_lvl}     Tipo: {pokemon_type}{attr(0)}")
        print(f"{fg(147)}╠═════════════════════════════════════════════════════════════════════╣{attr(0)}")
        print(f"{fg(147)}                           Punti Vita {lp}                                    {attr(0)}")
        print(f"{fg(147)}                           Attacco {att}                                       {attr(0)}")
        print(f"{fg(147)}                           Difesa {dif}                                        {attr(0)}")
        print(f"{fg(147)}                           Attacco Speciale {satt}                              {attr(0)}")
        print(f"{fg(147)}                           Difesa Speciale {sdif}                               {attr(0)}")
        print(f"{fg(147)}                           Velocità {spe}                                      {attr(0)}")
        print(f"{fg(147)}╚═════════════════════════════════════════════════════════════════════╝{attr(0)}")
        break
    else:
        print("\ninput invalido.\n")

next=input()
# Creazione stats del pokémon avversario------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
enemy_pokemon_lvl=random.randint(1,10)

espe=random.randint(1,6)
espe=espe+random.randint(1,6)         # enemy speed/velocità dell'avversario
espe=espe+random.randint(1,6)

eatt=random.randint(1,6)
eatt=eatt+random.randint(1,6)         # enemy attack/attacco dell'avversario
eatt=eatt+random.randint(1,6)

edif=random.randint(1,6)
edif=edif+random.randint(1,6)         # enemy defense/difesa dell'avversario  (def è un comando di python quindi non va bene come variabile)
edif=edif+random.randint(1,6)

esatt=random.randint(1,6)
esatt=esatt+random.randint(1,6)       # enemy special attack/attacco speciale dell'avversario
esatt=esatt+random.randint(1,6)

esdif=random.randint(1,6)
esdif=esdif+random.randint(1,6)       # enemy special defense/difesa speciale dell'avversario
esdif=esdif+random.randint(1,6)

elp=20+random.randint(1,6)
elp=elp+random.randint(1,6)           # enemy life points/punti vita dell'avversario
elp=elp+random.randint(1,6)

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
                enemy_pokemon_type = "Veleno"
            case "Mewtwo":
                enemy_pokemon_type = "Psico"

                elp = 1000
                eatt = 1000
                edif = 1000         # Mewtwo è uno dei pokémon più forti e infatti non dovrebbe nemmeno essere questi
                esatt = 1000
                esdif = 1000
                espe = 1000

            case "Abra":
                enemy_pokemon_type = "Psico"
            case "Pidgey" | "Rattata" | "Spearow" | "Jigglypuff":
                enemy_pokemon_type = "Normale"
            case "Caterpie" | "Weedle":
                enemy_pokemon_type = "Coleottero"
            case "Sandshrew":
                enemy_pokemon_type = "Terra"
            case "Onix":
                enemy_pokemon_type = "Roccia"
            case "Pikachu":
                enemy_pokemon_type = "Elettro"
            case "Ponyta" | "Vulpix":
                enemy_pokemon_type = "Fuoco"
            case "Oddish":
                enemy_pokemon_type = "Erba"
            case _:
                print("Errore nella lista")
# Inizio scontro------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

fight = "a"

while fight!="si" or fight!="SI" or fight!="Si" or fight!="S" or fight!="s":
    fight = input("Vuoi andare nell'erba alta?: ")

    if fight == "si" or fight == "Si" or fight == "SI" or fight=="S" or fight=="s":
        print (f"{fg(126)}\nÈ apparso un {enemy_pokemon} selvatico!{attr(0)}")
        break

    elif fight == "no" or fight == "No" or fight == "NO" or fight=="N" or fight=="n":
        print("\nHey campione siamo in un gioco pokémon, sei obbligato a fare almeno un combattimento")
        print (f"{fg(126)}\nÈ comparso un {enemy_pokemon} selvatico!{attr(0)}")
        break

    else:
        print("\ninput invalido.\n")

print(f"{fg(196)}╔═════════════════════════════════════════════════════════════════════╗{attr(0)}")
print(f"{fg(196)}        Statistiche di {enemy_pokemon}                Tipo: {enemy_pokemon_type}             {attr(0)}")
print(f"{fg(196)}╠═════════════════════════════════════════════════════════════════════╣{attr(0)}")
print(f"{fg(196)}                           Punti Vita {elp}                                   {attr(0)}")
print(f"{fg(196)}                           Attacco {eatt}                                      {attr(0)}")
print(f"{fg(196)}                           Difesa {edif}                                       {attr(0)}")
print(f"{fg(196)}                           Attacco Speciale {esatt}                             {attr(0)}")
print(f"{fg(196)}                           Difesa Speciale {esdif}                              {attr(0)}")
print(f"{fg(196)}                           Velocità {espe}                                     {attr(0)}")
print(f"{fg(196)}╚═════════════════════════════════════════════════════════════════════╝{attr(0)}")
next=input()

# Efficacia dei tipi-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
modifier=1
enemy_modifier=1
if pokemon_type=="Fuoco" and enemy_pokemon_type=="Erba" or enemy_pokemon_type=="Coleottero":
    modifier=2
    enemy_modifier=0.5
elif pokemon_type=="Fuoco" and enemy_pokemon_type=="Fuoco":
    modifier=0.5
    enemy_modifier=0.5
elif pokemon_type=="Acqua" and enemy_pokemon_type=="Fuoco" or enemy_pokemon_type=="Terra" or enemy_pokemon_type=="Roccia":
    modifier=2
    enemy_modifier=0.5
elif pokemon_type=="Erba" and enemy_pokemon_type=="Acqua" or enemy_pokemon_type=="Terra" or enemy_pokemon_type=="Roccia":
    modifier=2
    enemy_modifier=0.5
elif pokemon_type=="Erba" and enemy_pokemon_type=="Elettro":
    enemy_modifier=0.5
#--------------------------------------------------------------|             # https://wiki.pokemoncentral.it/Tipo -----> Per fare i Superefficace/Poco Efficace dei tipi abbiamo consultato la wiki ufficiale del gioco
if enemy_pokemon_type=="Veleno" and pokemon_type=="Erba":
    modifier=0.5
    enemy_modifier=2
elif enemy_pokemon_type=="Coleottero" and pokemon_type=="Erba":
    enemy_modifier=2
elif enemy_pokemon_type=="Terra" and pokemon_type=="Fuoco":
    modifier=0.5
    enemy_modifier=2
elif enemy_pokemon_type=="Roccia" and pokemon_type=="Fuoco":
    modifier=0.5
    enemy_modifier=2
elif enemy_pokemon_type=="Elettro" and pokemon_type=="Acqua":
    enemy_modifier=2
elif enemy_pokemon_type=="Fuoco" and pokemon_type=="Erba":
    modifier=0.5
    enemy_modifier=2
elif enemy_pokemon_type=="Erba" and pokemon_type=="Acqua":
    modifier=0.5
    enemy_modifier=2

# Attacco------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while not(lp<=0 or elp<=0):
    print(f"{fg(222)}\n╔═{lp} HP ╦                                                     ╦ HP {elp}═╗{attr(0)}")
    print(f"{fg(222)}╠═══════╩══════════════════════════╦══════════════════════════╩═══════╣{attr(0)}")
    print(f"{fg(222)}║{attr(0)}{bg(53)}              Attacco             {attr(0)}{fg(222)}║{attr(0)}{bg(53)}         Attacco Speciale         {attr(0)}{fg(222)}║{attr(0)}")
    print(f"{fg(222)}╚════════════════╗1╔═══════════════╩═══════════════╗2╔════════════════╝{attr(0)}")
    option=input("\n════════════╣Scegliere l'attacco: ")

    power=30            # potenza della mossa, che in questo caso mettiamo 30 di base sia per attacchi fisici che speciali
    if option=="attacco" or option=="1":  
        dmg= ((((((2*pokemon_lvl)/5)+2)*power*att/edif)/50)+2)*modifier                # https://wiki.pokemoncentral.it/Danno -----> il metodo per calcolare il Danno (cioè la quantità di Life Points da sottrarre ad ogni attacco) 
        elp=elp-dmg                                                                                                     # lo abbiamo preso dalla formula originale dei veri giochi Pokémon.
        time.sleep(1)

    elif option=="attacco speciale" or option=="2":
        dmg= ((((((2*pokemon_lvl)/5)+2)*power*satt/esdif)/50)+2)*modifier
        elp=elp-dmg
        time.sleep(1)

    elif option=="fuga" or option=="3":
        print(f"Scampato pericolo!")
        time.sleep(2)

    enemy_attack=random.randint(1,3)
    print(f"È il turno dell'avversario!")
    time.sleep(1)
    
    if enemy_attack==1:
        print(f"L'avversario ha scelto Attacco!")
        dmg= ((((((2*enemy_pokemon_lvl)/5)+2)*power*eatt/dif)/50)+2)*enemy_modifier
        time.sleep(1)

    elif enemy_attack==2:
        print(f"L'avversario ha scelto Attacco Speciale!")
        dmg= ((((((2*enemy_pokemon_lvl)/5)+2)*power*esatt/sdif)/50)+2)*enemy_modifier
        time.sleep(1)

if elp<=0:
    print(f"{enemy_pokemon} è esausto!")
    time.sleep(1)
    battle_exp=random.randint(7, 36)
    print(f"Hai vinto la battaglia. Esperienza ottenuta: {battle_exp}")
    pokemon_exp=pokemon_exp+battle_exp
if pokemon_exp >= 100:
    pokemon_lvl=pokemon_lvl+1


choice_combat=input("Vuoi continuare a combattere?: ")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------