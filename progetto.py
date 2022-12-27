import climage
import random

from colored import fg, bg, attr       #utilizzo le funzioni "fg" (foreground, per il colore del testo), "bg" (background, per lo sfondo), e "attr" (per interrompere i comandi precedenti) del modulo Colored.

print(f"{fg(88)}╔═════════════════════════════════════════════════════════════════════╗{attr(0)}")
print(f"{fg(88)}║{bg(153)}                         {fg(196)}Benvenuto in Pokémon{attr(0)}{bg(153)}                        {attr(0)}{fg(99)}║{attr(0)}")
print(f"{fg(99)}╠═════════════════════════════════════════════════════════════════════╣{attr(0)}")
print(f"{fg(99)}║                                                                     ║{attr(0)}")
print(f"{fg(99)}║        QUESTO PROGRAMMA SIMULA UNA SCHEDA  DI UN POKEMON            ║{attr(0)}")
print(f"{fg(99)}║                   ED  ALCUNI COMBATTIMENTI                          ║{attr(0)}")
print(f"{fg(99)}║                                                                     ║{attr(0)}")
print(f"{fg(99)}║     Inizia col scegliere uno dei tre pokémon iniziali per poter     ║{attr(0)}")
print(f"{fg(99)}║                      iniziare la tua avventura!                     ║{attr(0)}")
print(f"{fg(99)}╠═════════╗                                                 ╔═════════╣{attr(0)}")
print(f"{fg(88)}║ ◓  ◓  ◓ {fg(99)}╠═════════╗                             ╔═════════╣{attr(0)}{fg(88)} ◓  ◓  ◓ ║{attr(0)}")
print(f"{fg(88)}╚═════════╩═════════{fg(99)}╩═════════════════════════════╩{attr(0)}{fg(88)}═════════╩═════════╝{attr(0)}")


# converts the image to print in terminal
# inform of ANSI Escape codes
output = climage.convert('sassari.png')
  
# stampa l'immagine a schermo
print(output)
print(f"                         {fg(98)}SCEGLI UNA POKEBALL{attr(0)}")
print(f"                         {fg(98)} la 1 / la 2/ la 3 {attr(0)}")
pokeball = int(input(""))
if pokeball == 1:
    pokemon="Charmander"
    output1 = climage.convert('Charmander.png')
    
    print(output1)
    print(f"{fg(196)}╚══════════════════════════════════{pokemon}══════════════════════════════════╝{attr(0)}")
elif pokeball == 2:
    pokemon="Squirtle"
    output1 = climage.convert('Squirtle.png')

    print(output1)
    print(f"{fg(21)}╚══════════════════════════════════{pokemon}══════════════════════════════════╝{attr(0)}")
elif pokeball == 3:
    pokemon="Bulbasaur"
    output1 = climage.convert('Bulbasaur.png')

    print(output1)
    print(f"{fg(28)}╚══════════════════════════════════{pokemon}══════════════════════════════════╝{attr(0)}")
else :
    print("tua mamma morta")


op = input("voi dargli un nome")
if op == "si" or op == "SI" or "Si" :
    nome = input("Che nome vuoi dare al tuo pokemon   ")
    #creazione stats del pokemon
    spe=random.randint(1,6)        #
    spe=spe+random.randint(1,6)    #     speed   /   velocità
    spe=spe+random.randint(1,6)    #

    att=random.randint(1,6)        #
    att=att+random.randint(1,6)    #     attacco
    att=att+random.randint(1,6)    #

    dif=random.randint(1,6)        #
    dif=dif+random.randint(1,6)    #     defense  /   difesa   (def non va bene come variabile)
    dif=dif+random.randint(1,6)    #

    satt=random.randint(1,6)        #
    satt=satt+random.randint(1,6)    #     special attack  /   attacco speciale
    satt=satt+random.randint(1,6)    #

    sdif=random.randint(1,6)        #
    sdif=sdif+random.randint(1,6)    #     special defense    /   difesa speciale
    sdif=sdif+random.randint(1,6)    #

    pv=10+random.randint(1,6)        #
    pv=pv+random.randint(1,6)    #     Life points   /   Punti vita
    pv=pv+random.randint(1,6)    #



    #stampa scheda del pokemon
    print(f"{fg(100)}╔═════════════════════════════════════════════════════════════════════╗{attr(0)}")
    print(f"{fg(100)}                     Statistiche di   {nome}{attr(0)}                       {attr(0)}{fg(99)}{attr(0)}")
    print(f"{fg(100)}╠═════════════════════════════════════════════════════════════════════╣{attr(0)}")
    print(f"{fg(100)}                    punti vita {pv}                                    {attr(0)}")
    print(f"{fg(100)}                    attacco {att}                                       {attr(0)}")
    print(f"{fg(100)}                    difesa {dif}                                        {attr(0)}")
    print(f"{fg(100)}                    attacco speciale {satt}                              {attr(0)}")
    print(f"{fg(100)}                    difesa speciale {sdif}                               {attr(0)}")
    print(f"{fg(100)}                    velocità {spe}                                      {attr(0)}")
    print(f"{fg(100)}╚═════════════════════════════════════════════════════════════════════╝{attr(0)}")
elif op == "no" or op=="NO" or op=="No" :
    #creazione stats del pokemon
    spe=random.randint(1,6)        #
    spe=spe+random.randint(1,6)    #     speed   /   velocità
    spe=spe+random.randint(1,6)    #

    att=random.randint(1,6)        #
    att=att+random.randint(1,6)    #     attacco
    att=att+random.randint(1,6)    #

    dif=random.randint(1,6)        #
    dif=dif+random.randint(1,6)    #     defense  /   difesa   (def non va bene come variabile)
    dif=dif+random.randint(1,6)    #

    satt=random.randint(1,6)        #
    satt=satt+random.randint(1,6)    #     special attack  /   attacco speciale
    satt=satt+random.randint(1,6)    #

    sdif=random.randint(1,6)        #
    sdif=sdif+random.randint(1,6)    #     special defense    /   difesa speciale
    sdif=sdif+random.randint(1,6)    #

    pv=10+random.randint(1,6)        #
    pv=pv+random.randint(1,6)    #     speed   /   velocità
    pv=pv+random.randint(1,6)    #



    #stampa scheda del pokemon
    print(f"{fg(100)}╔═════════════════════════════════════════════════════════════════════╗{attr(0)}")
    print(f"{fg(100)}                     Statistiche di   {pokemon}{attr(0)}                       {attr(0)}{fg(99)}{attr(0)}")
    print(f"{fg(100)}╠═════════════════════════════════════════════════════════════════════╣{attr(0)}")
    print(f"{fg(100)}                    punti vita {pv}                                    {attr(0)}")
    print(f"{fg(100)}                    attacco {att}                                       {attr(0)}")
    print(f"{fg(100)}                    difesa {dif}                                        {attr(0)}")
    print(f"{fg(100)}                    attacco speciale {satt}                              {attr(0)}")
    print(f"{fg(100)}                    difesa speciale {sdif}                               {attr(0)}")
    print(f"{fg(100)}                    velocità {spe}                                      {attr(0)}")
    print(f"{fg(100)}╚═════════════════════════════════════════════════════════════════════╝{attr(0)}")
