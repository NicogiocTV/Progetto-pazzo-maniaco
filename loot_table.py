import random

def loot_ita():                 # una funzione con gli oggetti in italiano
    loot_list = ["pozione", "super pozione", "iper pozione","pozione max", "breadboard"]    # oggetti che si possono trovare dopo ogni scontro
    probability = [40 , 27.5 , 20  , 12.5 , 0.000000000000000000001]                        # probabilità di drop di ogni oggetto

    loot_probability = dict(zip(loot_list, probability))
    loot_prob=True
    open_chest = "si"
    if open_chest.lower() == "si" or open_chest.lower() == "s":
        loot_drop = random.choices(loot_list, weights=probability)
        loot_name = loot_drop[0]
        index = loot_list.index(loot_name)
        loot_prob = loot_probability[loot_name]
        return loot_drop, index
    

def loot_eng():                 # una funzione con gli oggetti in inglese
    loot_list = ["potion", "super potion", "hyper potion","max potion","breadboard"]    # oggetti che si possono trovare dopo ogni scontro
    probability = [40 , 27.5 , 20  , 12.5 , 0.000000000000000000001]                        # probabilità di drop di ogni oggetto

    loot_probability = dict(zip(loot_list, probability))
    loot_prob=True
    open_chest = "si"
    if open_chest.lower() == "si" or open_chest.lower() == "s":
        loot_drop = random.choices(loot_list, weights=probability)
        loot_name = loot_drop[0]
        index = loot_list.index(loot_name)
        loot_prob = loot_probability[loot_name]
        return loot_drop, index    