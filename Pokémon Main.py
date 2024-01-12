# Inizio
import time                           # utilizzo la libreria time con il suo comando "time.sleep" per mettere in pausa il programma per un certo numero di secondi
from tqdm import tqdm                 # utilizzo la libreria "tqdm" fatta appositamente per la creazione di barre di caricamento
import pyfiglet
from colored import fg, bg, attr      # utilizzo le funzioni "fg" (foreground, per il colore del testo), "bg" (background, per lo sfondo), e "attr" (per interrompere i comandi precedenti) del modulo Colored.
import Pokémon_ita
import Pokémon_eng

def loading_bar():                   # funzione per la barra di caricamento
    for i in range(1):
        time.sleep(2)
    for i in tqdm(range(10)):        # cicli per la creazione della barra di caricamento
        time.sleep(0.1)
loading_bar()

ascii_language = pyfiglet.figlet_format(f"Select       language ITA              |               ENG")              # scrivo la stringa da trasformare in textart
print(ascii_language)
language = input()


while language!="ITA" or language!="Ita" or language!="ita" or language!="italiano" or language!="i" or language!="ITALIANO" or language!="Italiano" or language!="I" or language!="ENG" or language!="Eng" or language!="eng" or language!="english" or language!="e" or language!="ENGLISH" or language!="English" or language!="E":
    if language == "ITA" or language == "Ita" or language == "ita" or language == "italiano" or language == "i" or language == "ITALIANO" or language == "Italiano" or language == "I":
        Pokémon_ita.game_i()        # esegue il gioco in italiano
        break
    elif language == "ENG" or language == "Eng" or language == "eng" or language == "english" or language == "e" or language == "ENGLISH" or language == "English" or language == "E":
        Pokémon_eng.game_e()        # esegue il gioco in inglese
        break
    else:
        print("Invalid input./Input invalido.")


# Riconoscimenti----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("\033c", end="")
time.sleep(1)
print(f"{fg(103)}\n\n\n╔══════════════════Credits═══════════════════╗{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║                                            ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║                    ~~~~                    ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║             EXECUTIVE PRODUCERS            ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║                                            ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║                 Diego Amati                ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║               Nicola Tonelli               ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║                Paolo D'Elia                ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║             Filippo Cornacchia             ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║                                            ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║                    ~~~~                    ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║               GRAPHICS DESIGN              ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║                                            ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║               Nicola Tonelli               ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║                                            ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║         BATTLE SYSTEM PROGRAMMING          ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║                                            ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║                 Diego Amati                ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║                                            ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║                SOUND EFFECTS               ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║                                            ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║             LEAD: Paolo D'Elia             ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║               Nicola Tonelli               ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║                                            ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║                Translated By               ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║                                            ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║              Filippo Cornacchia            ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║                                            ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║              TECHNICAL SUPPORT             ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║                                            ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║                   ChatGPT                  ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║                                            ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║            ~~~~~~~~~~~~~~~~~~~~~           ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║             {fg(160)}Thanks for playing!{attr(0)}{fg(103)}            ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║            ~~~~~~~~~~~~~~~~~~~~~           ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║                                            ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║   PKM Project   |   3M inc. © 2020-2023    ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}║            All rights reserved             ║{attr(0)}")
time.sleep(0.1)
print(f"{fg(103)}╚════════════════════════════════════════════╝{attr(0)}")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------