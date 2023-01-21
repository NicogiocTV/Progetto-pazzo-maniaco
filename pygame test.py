import random

sword_list = ["spada rotta", "spada di legno" , "spada di ferro" , "spada di diamante" ,"Excalibur" , "Soulstealer", "The Unbroken" ,"Moonblade","Sunblade", "Ghostblade"]
probability = [40, 15, 10, 5 , 0.01 , 0.01 , 4, 2, 2 ,2] 



for i in range(21):
    sword_drop = random.choices(sword_list, weights=probability)
    print(sword_drop)
