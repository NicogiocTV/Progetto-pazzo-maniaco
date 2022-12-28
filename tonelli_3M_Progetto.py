import climage                         # utilizzo il modulo Climage per stampare a schermo delle immagini (ATTENZIONE: le immagini devono essere scaricate, avere lo stesso nome dichiarato nel programma e trovarsi nella stessa cartella del programma).
import random

from colored import fg, bg, attr       # utilizzo le funzioni "fg" (foreground, per il colore del testo), "bg" (background, per lo sfondo), e "attr" (per interrompere i comandi precedenti) del modulo Colored.


print(f"{fg(88)}╔═════════════════════════════════════════════════════════════════════╗{attr(0)}")
print(f"{fg(88)}║{bg(153)}                         {fg(196)}Benvenuto in Pokémon{attr(0)}{bg(153)}                        {attr(0)}{fg(99)}║{attr(0)}")
print(f"{fg(99)}╠═════════════════════════════════════════════════════════════════════╣{attr(0)}")
print(f"{fg(99)}║                                                                     ║{attr(0)}")
print(f"{fg(99)}║          Questo programma simula la scheda di un pokémon            ║{attr(0)}")
print(f"{fg(99)}║                     e alcuni combattimenti.                         ║{attr(0)}")
print(f"{fg(99)}║                                                                     ║{attr(0)}")
print(f"{fg(99)}║     Inizia col scegliere uno dei tre pokémon iniziali per poter     ║{attr(0)}")
print(f"{fg(99)}║                      iniziare la tua avventura!                     ║{attr(0)}")
print(f"{fg(99)}╠═════════╗                                                 ╔═════════╣{attr(0)}")
print(f"{fg(88)}║ ◓  ◓  ◓ {fg(99)}╠═════════╗                             ╔═════════╣{attr(0)}{fg(88)} ◓  ◓  ◓ ║{attr(0)}")
print(f"{fg(88)}╚═════════╩═════════{fg(99)}╩═════════════════════════════╩{attr(0)}{fg(88)}═════════╩═════════╝{attr(0)}")

continua=input()            # questa variabile serve per "fermare" il programma, il programma continua una volta che l'utente dà la conferma semplicemente premendo invio (come nei veri giochi Pokémon).
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

img_pokeball = climage.convert('sassari.png')       # converte l'immagine in formato ANSI e gli assegna una variabile
print(img_pokeball)                                 # stampa l'immagine a schermo

print(f"              {fg(98)}SCEGLI UNA POKÉBALL PER RICEVERE IL TUO PRIMO POKÉMON{attr(0)}")
print(f"                                {fg(98)} 1 / 2 / 3 \n{attr(0)}")

pokeball="a"
while pokeball!="1" or pokeball!="2" or pokeball!="3": 
    pokeball = input("")

    if pokeball == "1":
        pokemon="Charmander"
        img_pokemon = climage.convert('Charmander.png')
        print(img_pokemon)
        print(f"{fg(196)}╚═══════════════════════════════🔥 {pokemon} 🔥═════════════════════════════════╝{attr(0)}")
        tipo="Fuoco"
        break
    elif pokeball == "2":
        pokemon="Squirtle"
        img_pokemon = climage.convert('Squirtle.png')
        print(img_pokemon)
        print(f"{fg(21)}╚═══════════════════════════════💧 {pokemon} 💧═════════════════════════════════╝{attr(0)}")
        tipo="Acqua"
        break
    elif pokeball == "3":
        pokemon="Bulbasaur"
        img_pokemon = climage.convert('Bulbasaur.png')
        print(img_pokemon)
        print(f"{fg(28)}╚═══════════════════════════════🍃 {pokemon} 🍃════════════════════════════════╝{attr(0)}")
        tipo="Erba"
        break
    else:
        print("\ninput invalido.\n")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

opz = "a"
while opz!="si" or opz!="SI" or opz!="Si" or opz!="no" or opz!="NO" or opz!="No":
    opz = input("\nVuoi dargli un nome?: ")
    if opz=="si" or opz=="SI" or opz=="Si":
        nome = input("\nChe nome vuoi dare al tuo pokémon?: ")
        # creazione stats del pokemon
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

        lp=10+random.randint(1,6)
        lp=lp+random.randint(1,6)           # life points/punti vita
        lp=lp+random.randint(1,6)
        

        # stampa scheda del pokémon
        print(f"\n{fg(100)}╔═════════════════════════════════════════════════════════════════════╗{attr(0)}")
        print(f"{fg(100)}         Statistiche di {nome}                  Tipo: {tipo}                    {attr(0)}")
        print(f"{fg(100)}╠═════════════════════════════════════════════════════════════════════╣{attr(0)}")
        print(f"{fg(100)}                           Punti Vita {lp}                                    {attr(0)}")
        print(f"{fg(100)}                           Attacco {att}                                       {attr(0)}")
        print(f"{fg(100)}                           Difesa {dif}                                        {attr(0)}")
        print(f"{fg(100)}                           Attacco Speciale {satt}                              {attr(0)}")
        print(f"{fg(100)}                           Difesa Speciale {sdif}                               {attr(0)}")
        print(f"{fg(100)}                           Velocità {spe}                                      {attr(0)}")
        print(f"{fg(100)}╚═════════════════════════════════════════════════════════════════════╝{attr(0)}")
        break

    elif opz=="no" or opz=="NO" or opz=="No":
        # creazione stats del pokémon
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

        lp=10+random.randint(1,6)
        lp=lp+random.randint(1,6)           # life points/punti vita
        lp=lp+random.randint(1,6)



        # stampa scheda del pokémon
        print(f"\n{fg(100)}╔═════════════════════════════════════════════════════════════════════╗{attr(0)}")
        print(f"{fg(100)}                       Statistiche di {pokemon}{attr(0)}                     {attr(0)}{fg(99)}{attr(0)}")
        print(f"{fg(100)}╠═════════════════════════════════════════════════════════════════════╣{attr(0)}")
        print(f"{fg(100)}                           Punti Vita {lp}                                    {attr(0)}")
        print(f"{fg(100)}                           Attacco {att}                                       {attr(0)}")
        print(f"{fg(100)}                           Difesa {dif}                                        {attr(0)}")
        print(f"{fg(100)}                           Attacco Speciale {satt}                              {attr(0)}")
        print(f"{fg(100)}                           Difesa Speciale {sdif}                               {attr(0)}")
        print(f"{fg(100)}                           Velocità {spe}                                      {attr(0)}")
        print(f"{fg(100)}╚═════════════════════════════════════════════════════════════════════╝{attr(0)}")
        break
    else:
        print("\ninput invalido.\n")

continua=input()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

