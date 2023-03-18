import requests as req
import json
import math
import time
import keyboard
from time import sleep
import os
from colorama import Fore, Back, Style


def clear_console(): return os.system('cls')
True==True

def main():

    clear_console()

    print(Fore.GREEN + "#crop market written by K9oo8")
    print("#to optimize coin output")
    print("#from farming")

    #more data = more data male
    url = "https://api.hypixel.net/skyblock/bazaar"

    r = req.get(url).json()


    # Harvest value is equal to 1 minute at optimal speed
    carrotHarvest = 39519
    sugarcaneHarvest = 27392 #12k mushrooms
    potatoHarvest = 35840
    wheatHarvest = 12407
    melonHarvest = 58080
    pumpkinHarvest = 12180
    mushroomHarvest = 23104
    cocoaHarvest = 35260
    wartsHarvest = 31944
    cactusHarvest = 19335



    #get carrot data for good vision
    carrotInstaSell = r["products"]["ENCHANTED_CARROT"]['quick_status']['sellPrice']
    carrotBuyOrder = r["products"]["ENCHANTED_CARROT"]['quick_status']['buyPrice']

    carrotperminute = math.trunc(carrotInstaSell*carrotHarvest/160)
    carrotperhour = math.trunc(carrotperminute*60)



    #get sugar data to go fast
    sugarInstaSell = r["products"]["ENCHANTED_SUGAR"]['quick_status']['sellPrice']
    sugarBuyOrder = r["products"]["ENCHANTED_SUGAR"]['quick_status']['buyPrice']

    sugarperminute = math.trunc(sugarInstaSell*sugarcaneHarvest/160)
    sugarperhour = math.trunc(sugarperminute*60)



    #get potato data to kill the irish
    potatoInstaSell = r["products"]["ENCHANTED_POTATO"]['quick_status']['sellPrice']
    potatoBuyOrder = r["products"]["ENCHANTED_POTATO"]['quick_status']['buyPrice']

    potatoperminute = math.trunc(potatoInstaSell*potatoHarvest/160)
    potatoperhour = math.trunc(potatoperminute*60)


    #get wheat data to make bread
    wheatInstaSell = r["products"]["ENCHANTED_HAY_BLOCK"]['quick_status']['sellPrice']
    wheatBuyOrder = r["products"]["ENCHANTED_HAY_BLOCK"]['quick_status']['buyPrice']

    wheatperminute = math.trunc(wheatInstaSell*wheatHarvest/1296)
    wheatperhour = math.trunc(wheatperminute*60)

    #get melon data to fuck the melons
    melonInstaSell = r["products"]["ENCHANTED_MELON"]['quick_status']['sellPrice']
    melonBuyOrder = r["products"]["ENCHANTED_MELON"]['quick_status']['buyPrice']

    melonperminute = math.trunc(melonInstaSell*melonHarvest/160)
    melonperhour = math.trunc(melonperminute*60)


    #get pumpkin data for halloween
    pumpkinInstaSell = r["products"]["ENCHANTED_PUMPKIN"]['quick_status']['sellPrice']
    pumpkinBuyOrder = r["products"]["ENCHANTED_PUMPKIN"]['quick_status']['buyPrice']

    pumpkinperminute = math.trunc(pumpkinInstaSell*pumpkinHarvest/160)
    pumpkinperhour = math.trunc(pumpkinperminute*60)

    #get mushroom data to trip mad balls
    mushroomInstaSell = r["products"]["ENCHANTED_RED_MUSHROOM"]['quick_status']['sellPrice']
    mushroomBuyOrder = r["products"]["ENCHANTED_RED_MUSHROOM"]['quick_status']['buyPrice']

    mushroomperminute = math.trunc(mushroomInstaSell*mushroomHarvest/160)
    mushroomperhour = math.trunc(mushroomperminute*60)

    #get cocoa data to make chocolate
    cocoaInstaSell = r["products"]["ENCHANTED_COCOA"]['quick_status']['sellPrice']
    cocoaBuyOrder = r["products"]["ENCHANTED_COCOA"]['quick_status']['buyPrice']

    cocoaperminute = math.trunc(cocoaInstaSell*cocoaHarvest/160)
    cocoaperhour = math.trunc(cocoaperminute*60)

    #get warts data to spread stds
    wartsInstaSell = r["products"]["ENCHANTED_NETHER_STALK"]['quick_status']['sellPrice']
    wartsBuyOrder = r["products"]["ENCHANTED_NETHER_STALK"]['quick_status']['buyPrice']

    wartsperminute = math.trunc(wartsInstaSell*wartsHarvest/160)
    wartsperhour = math.trunc(wartsperminute*60)

    #get cactus data to breed camels
    cactusInstaSell = r["products"]["ENCHANTED_CACTUS_GREEN"]['quick_status']['sellPrice']
    cactusBuyOrder = r["products"]["ENCHANTED_CACTUS_GREEN"]['quick_status']['buyPrice']

    cactusperminute = math.trunc(cactusInstaSell*cactusHarvest/160)
    cactusperhour = math.trunc(cactusperminute*60)

    #print carrot/sugarcane stuff
    print(Fore.YELLOW + "\nCarrots", Fore.LIGHTGREEN_EX + "                                            Sugar Cane\n")

    print(Fore.YELLOW + "Insta Sell Price =",math.trunc(carrotInstaSell), Fore.LIGHTGREEN_EX + "                             Insta Sell Price =",math.trunc(sugarInstaSell))
    print(Fore.YELLOW + "Buy Order Price =",math.trunc(carrotBuyOrder), Fore.LIGHTGREEN_EX + "                              Buy Order Price =",math.trunc(sugarBuyOrder))
    print(Fore.YELLOW + "Estimate Coins Per Minute =", f'{carrotperminute:,}', Fore.LIGHTGREEN_EX + "                  Estimate Coins Per Minute =", f'{sugarperminute:,}')
    print(Fore.YELLOW + "Estimate Coin Per Hour =", f'{carrotperhour:,}', Fore.LIGHTGREEN_EX + "                   Estimate Coin Per Hour =", f'{sugarperhour:,}')

    #print potato wheat stuff
    print(Fore.RED+ "\nPotatoes", Fore.LIGHTYELLOW_EX + "                                           Wheat\n")

    print(Fore.RED + "Insta Sell Price =",math.trunc(potatoInstaSell), Fore.LIGHTYELLOW_EX + "                             Insta Sell Price =",math.trunc(wheatInstaSell))
    print(Fore.RED + "Buy Order Price =",math.trunc(potatoBuyOrder), Fore.LIGHTYELLOW_EX + "                              Buy Order Price =",math.trunc(wheatBuyOrder))
    print(Fore.RED + "Estimate Coins Per Minute =", f'{potatoperminute:,}', Fore.LIGHTYELLOW_EX + "                  Estimate Coins Per Minute =", f'{wheatperminute:,}')
    print(Fore.RED + "Estimate Coin Per Hour =", f'{potatoperhour:,}', Fore.LIGHTYELLOW_EX + "                   Estimate Coin Per Hour =", f'{wheatperhour:,}')

    #print melon pumpkin stuff
    print(Fore.GREEN+ "\nMelon", Fore.LIGHTRED_EX + "                                            Pumpkin\n")

    print(Fore.GREEN + "Insta Sell Price =",math.trunc(melonInstaSell), Fore.LIGHTRED_EX + "                             Insta Sell Price =",math.trunc(pumpkinInstaSell))
    print(Fore.GREEN + "Buy Order Price =",math.trunc(melonBuyOrder), Fore.LIGHTRED_EX + "                              Buy Order Price =",math.trunc(pumpkinBuyOrder))
    print(Fore.GREEN + "Estimate Coins Per Minute =", f'{melonperminute:,}', Fore.LIGHTRED_EX + "                  Estimate Coins Per Minute =", f'{pumpkinperminute:,}')
    print(Fore.GREEN + "Estimate Coin Per Hour =", f'{melonperhour:,}', Fore.LIGHTRED_EX + "                   Estimate Coin Per Hour =", f'{pumpkinperhour:,}')

    #print mushroom cocoa stuff
    print(Fore.MAGENTA+ "\nMushroom", Fore.CYAN + "                                            Cocoa\n")

    print(Fore.MAGENTA + "Insta Sell Price =",math.trunc(mushroomInstaSell), Fore.CYAN + "                             Insta Sell Price =",math.trunc(cocoaInstaSell))
    print(Fore.MAGENTA + "Buy Order Price =",math.trunc(mushroomBuyOrder), Fore.CYAN + "                              Buy Order Price =",math.trunc(cocoaBuyOrder))
    print(Fore.MAGENTA + "Estimate Coins Per Minute =", f'{mushroomperminute:,}', Fore.CYAN + "                  Estimate Coins Per Minute =", f'{cocoaperminute:,}')
    print(Fore.MAGENTA + "Estimate Coin Per Hour =", f'{mushroomperhour:,}', Fore.CYAN + "                   Estimate Coin Per Hour =", f'{cocoaperhour:,}')

    #print warts cactus stuff
    print(Fore.RED+ "\nWart", Fore.GREEN + "                                            Cactus\n")

    print(Fore.RED + "Insta Sell Price =",math.trunc(wartsInstaSell), Fore.GREEN + "                             Insta Sell Price =",math.trunc(cactusInstaSell))
    print(Fore.RED + "Buy Order Price =",math.trunc(wartsBuyOrder), Fore.GREEN + "                              Buy Order Price =",math.trunc(cactusBuyOrder))
    print(Fore.RED + "Estimate Coins Per Minute =", f'{wartsperminute:,}', Fore.GREEN + "                  Estimate Coins Per Minute =", f'{cactusperminute:,}')
    print(Fore.RED + "Estimate Coin Per Hour =", f'{wartsperhour:,}', Fore.GREEN + "                   Estimate Coin Per Hour =", f'{cactusperhour:,}')

    #closing function
    print(Style.RESET_ALL)
    print('PRESS ENTER TO EXIT / SPACE TO REFRESH')
    while True==True:
        if keyboard.is_pressed('enter'):
            print(Fore.BLACK + Back.GREEN + "\4may your fields be blessed inshallah\4",)
            print(Style.RESET_ALL + "                              ")
            sleep(2)
            exit()
        elif keyboard.is_pressed('space'):
            main()

main()