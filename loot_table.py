import random

def loot():
    loot_list = ["pozione", "super pozione", "iper pozione","pozione max", "breadboard"]
    probability = [40 , 27.5 , 20  , 12.5 , 0.000000000000000000001] 

    loot_probability = dict(zip(loot_list, probability))
    loot_prob=True
    open_chest = "si"
    if open_chest.lower() == "si" or open_chest.lower() == "s":
        loot_drop = random.choices(loot_list, weights=probability)
        loot_name = loot_drop[0]
        index = loot_list.index(loot_name)
        loot_prob = loot_probability[loot_name]
        return loot_drop, index
    


        