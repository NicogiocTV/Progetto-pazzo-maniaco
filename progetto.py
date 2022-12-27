import climage

from colored import fg, bg, attr       #utilizzo le funzioni "fg" (foreground, per il colore del testo), "bg" (background, per lo sfondo), e "attr" (per interrompere i comandi precedenti) del modulo Colored.

print(f"{fg(88)}╔═════════════════════════════════════════════════════════════════════╗{attr(0)}")
print(f"{fg(88)}║{bg(153)}                         {fg(196)}Benvenuto in Pokémon{attr(0)}{bg(153)}                        {attr(0)}{fg(99)}║{attr(0)}")
print(f"{fg(99)}╠═════════════════════════════════════════════════════════════════════╣{attr(0)}")
print(f"{fg(99)}║                                                                     ║{attr(0)}")
print(f"{fg(99)}║        QESTO PROGRAMMA SIMULA UNA SCHEDA  DI UN POKEMON             ║{attr(0)}")
print(f"{fg(99)}║                     ALCUNI COMBATTIMENTI                            ║{attr(0)}")
print(f"{fg(99)}║                                                                     ║{attr(0)}")
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
    print(f"il pockemon che hai scelto è {pokemon}")
elif pokeball == 2:
    pokemon="Squirtle"
    print(f"il pockemon che hai scelto è {pokemon}")
elif pokeball == 3:
    pokemon="Bulbasaur"
    print(f"il pockemon che hai scelto è {pokemon}")
else :
    print("tua mamma morta")