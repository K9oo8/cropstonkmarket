import requests as req
import json
import math
import keyboard
from time import sleep
import os
from colorama import Fore, Back, Style


def clear_console(): return os.system('cls')
True==True

def main():

    clear_console()

    print(Fore.GREEN + " \x1B[6m_____ _____ _____ _____    _____ _____ _____ _____ _____\n|   __|  _  | __  |     |  |     | __  |     |  _  |   __|\n|   __|     |    -| | | |  |   --|    -|  |  |   __|__   |\n|__|  |__|__|__|__|_|_|_|  |_____|__|__|_____|__|  |_____|\n _____ _____ _____ _____    _____ _____ _____ _____ __ __\n|     |  _  |  |  |   __|  |     |     |   | |   __|  |  |\n| | | |     |    -|   __|  | | | |  |  | | | |   __|_   _|\n|_|_|_|__|__|__|__|_____|  |_|_|_|_____|_|___|_____| |_|  \n _____ _____ _____ _____ _____ _____ _____    _ _ _ _____ _____ _____ _____\n| __  |   __|   __|  _  |   __|     |_   _|  | | | |     |     |   __|   | |\n|    -|   __|__   |   __|   __|   --| | |    | | | |  |  | | | |   __| | | |\n|__|__|_____|_____|__|  |_____|_____| |_|    |_____|_____|_|_|_|_____|_|___|\n\x1B[0m")


    #more data = more data male
    url = "https://api.hypixel.net/skyblock/bazaar"

    r = req.get(url).json()


    # Harvest value is equal to 1 minute at optimal speed
    carrotHarvest = 39519
    sugarcaneHarvest = 27074 #last update Mar/02/23
    potatoHarvest = 35840
    wheatHarvest = 12407
    melonHarvest = 58080
    pumpkinHarvest = 12180
    mushroomHarvest = 23104
    cocoaHarvest = 35260
    wartsHarvest = 31944
    cactusHarvest = 19335


    #get mushroom data to trip mad balls
    mushroomInstaSell = r["products"]["ENCHANTED_RED_MUSHROOM"]['quick_status']['sellPrice']
    mushroomBuyOrder = r["products"]["ENCHANTED_RED_MUSHROOM"]['quick_status']['buyPrice']

    mushroomperminute = math.trunc(mushroomInstaSell*mushroomHarvest/160)
    mushroomperhour = math.trunc(mushroomperminute*60)


    #get carrot data for good vision
    carrotInstaSell = r["products"]["ENCHANTED_CARROT"]['quick_status']['sellPrice']
    carrotBuyOrder = r["products"]["ENCHANTED_CARROT"]['quick_status']['buyPrice']

    carrotperminute = math.trunc(carrotInstaSell*carrotHarvest/160+mushroomInstaSell*7.5)
    carrotperhour = math.trunc(carrotperminute*60)


    #get sugar data to go fast
    sugarInstaSell = r["products"]["ENCHANTED_SUGAR"]['quick_status']['sellPrice']
    sugarBuyOrder = r["products"]["ENCHANTED_SUGAR"]['quick_status']['buyPrice']

    sugarperminute = math.trunc(sugarInstaSell*sugarcaneHarvest/160+mushroomInstaSell*15)
    sugarperhour = math.trunc(sugarperminute*60)


    #get potato data to kill the irish
    potatoInstaSell = r["products"]["ENCHANTED_POTATO"]['quick_status']['sellPrice']
    potatoBuyOrder = r["products"]["ENCHANTED_POTATO"]['quick_status']['buyPrice']

    potatoperminute = math.trunc(potatoInstaSell*potatoHarvest/160+mushroomInstaSell*7.5)
    potatoperhour = math.trunc(potatoperminute*60)


    #get wheat data to make bread
    wheatInstaSell = r["products"]["ENCHANTED_HAY_BLOCK"]['quick_status']['sellPrice']
    wheatBuyOrder = r["products"]["ENCHANTED_HAY_BLOCK"]['quick_status']['buyPrice']

    wheatperminute = math.trunc(wheatInstaSell*wheatHarvest/1296+mushroomInstaSell*7.5)
    wheatperhour = math.trunc(wheatperminute*60)

    #get melon data to fuck the melons
    melonInstaSell = r["products"]["ENCHANTED_MELON"]['quick_status']['sellPrice']
    melonBuyOrder = r["products"]["ENCHANTED_MELON"]['quick_status']['buyPrice']

    melonperminute = math.trunc(melonInstaSell*melonHarvest/160+mushroomInstaSell*7.5)
    melonperhour = math.trunc(melonperminute*60)


    #get pumpkin data for halloween
    pumpkinInstaSell = r["products"]["ENCHANTED_PUMPKIN"]['quick_status']['sellPrice']
    pumpkinBuyOrder = r["products"]["ENCHANTED_PUMPKIN"]['quick_status']['buyPrice']

    pumpkinperminute = math.trunc(pumpkinInstaSell*pumpkinHarvest/160+mushroomInstaSell*7.5)
    pumpkinperhour = math.trunc(pumpkinperminute*60)

    #get cocoa data to make chocolate
    cocoaInstaSell = r["products"]["ENCHANTED_COCOA"]['quick_status']['sellPrice']
    cocoaBuyOrder = r["products"]["ENCHANTED_COCOA"]['quick_status']['buyPrice']

    cocoaperminute = math.trunc(cocoaInstaSell*cocoaHarvest/160+mushroomInstaSell*7.5)
    cocoaperhour = math.trunc(cocoaperminute*60)


    #get warts data to spread stds
    wartsInstaSell = r["products"]["ENCHANTED_NETHER_STALK"]['quick_status']['sellPrice']
    wartsBuyOrder = r["products"]["ENCHANTED_NETHER_STALK"]['quick_status']['buyPrice']

    wartsperminute = math.trunc(wartsInstaSell*wartsHarvest/160+mushroomInstaSell*7.5)
    wartsperhour = math.trunc(wartsperminute*60)


    #get cactus data to breed camels
    cactusInstaSell = r["products"]["ENCHANTED_CACTUS_GREEN"]['quick_status']['sellPrice']
    cactusBuyOrder = r["products"]["ENCHANTED_CACTUS_GREEN"]['quick_status']['buyPrice']

    cactusperminute = math.trunc(cactusInstaSell*cactusHarvest/160+mushroomInstaSell*15)
    cactusperhour = math.trunc(cactusperminute*60)



    #print carrot/sugarcane stuff
    print(Fore.YELLOW + "\n\x1B[3mCarrots\x1B[0m NPC = 160", Fore.LIGHTGREEN_EX + "                                      \x1B[3mSugar Cane\x1B[0m NPC = 320\n")

    print(Fore.YELLOW + "     Insta Sell Price =",math.trunc(carrotInstaSell), Fore.LIGHTGREEN_EX + "                                Insta Sell Price =",math.trunc(sugarInstaSell))
    print(Fore.YELLOW + "     Buy Order Price =",math.trunc(carrotBuyOrder), Fore.LIGHTGREEN_EX + "                                 Buy Order Price =",math.trunc(sugarBuyOrder))
    print(Fore.YELLOW + "     Estimate Coins Per Minute =", f'{carrotperminute:,}', Fore.LIGHTGREEN_EX + "                    Estimate Coins Per Minute =", f'{sugarperminute:,}')
    print(Fore.YELLOW + "     Estimate Coin Per Hour =", f'{carrotperhour:,}', Fore.LIGHTGREEN_EX + "                    Estimate Coin Per Hour =", f'{sugarperhour:,}')
    print(Fore.YELLOW + "     Crops per second =", f'{carrotHarvest:,}', Fore.LIGHTGREEN_EX + "                              Crops per second =", f'{sugarcaneHarvest:,}')

    #print potato wheat stuff
    print(Fore.RED+ "\n\x1B[3mPotatoes\x1B[0m NPC = 160", Fore.LIGHTYELLOW_EX + "                                     \x1B[3mWheat\x1B[0m NPC = 1300\n")

    print(Fore.RED + "     Insta Sell Price =",math.trunc(potatoInstaSell), Fore.LIGHTYELLOW_EX + "                                Insta Sell Price =",math.trunc(wheatInstaSell))
    print(Fore.RED + "     Buy Order Price =",math.trunc(potatoBuyOrder), Fore.LIGHTYELLOW_EX + "                                 Buy Order Price =",math.trunc(wheatBuyOrder))
    print(Fore.RED + "     Estimate Coins Per Minute =", f'{potatoperminute:,}', Fore.LIGHTYELLOW_EX + "                    Estimate Coins Per Minute =", f'{wheatperminute:,}')
    print(Fore.RED + "     Estimate Coin Per Hour =", f'{potatoperhour:,}', Fore.LIGHTYELLOW_EX + "                    Estimate Coin Per Hour =", f'{wheatperhour:,}')
    print(Fore.RED + "     Crops per second =", f'{potatoHarvest:,}', Fore.LIGHTYELLOW_EX + "                              Crops per second =", f'{wheatHarvest:,}')

    #print melon pumpkin stuff
    print(Fore.GREEN+ "\n\x1B[3mMelon\x1B[0m NPC = 160", Fore.LIGHTRED_EX + "                                        \x1B[3mPumpkin\x1B[0m NPC = 640\n")

    print(Fore.GREEN + "     Insta Sell Price =",math.trunc(melonInstaSell), Fore.LIGHTRED_EX + "                                Insta Sell Price =",math.trunc(pumpkinInstaSell))
    print(Fore.GREEN + "     Buy Order Price =",math.trunc(melonBuyOrder), Fore.LIGHTRED_EX + "                                 Buy Order Price =",math.trunc(pumpkinBuyOrder))
    print(Fore.GREEN + "     Estimate Coins Per Minute =", f'{melonperminute:,}', Fore.LIGHTRED_EX + "                    Estimate Coins Per Minute =", f'{pumpkinperminute:,}')
    print(Fore.GREEN + "     Estimate Coin Per Hour =", f'{melonperhour:,}', Fore.LIGHTRED_EX + "                    Estimate Coin Per Hour =", f'{pumpkinperhour:,}')
    print(Fore.GREEN + "     Crops per second =", f'{melonHarvest:,}', Fore.LIGHTRED_EX + "                              Crops per second =", f'{pumpkinHarvest:,}')

    #print mushroom cocoa stuff
    print(Fore.MAGENTA+ "\n\x1B[3mMushroom\x1B[0m NPC = 640", Fore.CYAN + "                                     \x1B[3mCocoa Beans\x1B[0m NPC = 480\n")

    print(Fore.MAGENTA + "     Insta Sell Price =",math.trunc(mushroomInstaSell), Fore.CYAN + "                                Insta Sell Price =",math.trunc(cocoaInstaSell))
    print(Fore.MAGENTA + "     Buy Order Price =",math.trunc(mushroomBuyOrder), Fore.CYAN + "                                 Buy Order Price =",math.trunc(cocoaBuyOrder))
    print(Fore.MAGENTA + "     Estimate Coins Per Minute =", f'{mushroomperminute:,}', Fore.CYAN + "                    Estimate Coins Per Minute =", f'{cocoaperminute:,}')
    print(Fore.MAGENTA + "     Estimate Coin Per Hour =", f'{mushroomperhour:,}', Fore.CYAN + "                    Estimate Coin Per Hour =", f'{cocoaperhour:,}')
    print(Fore.MAGENTA + "     Crops per second =", f'{mushroomHarvest:,}', Fore.CYAN + "                              Crops per second =", f'{cocoaHarvest:,}')

    #print warts cactus stuff
    print(Fore.RED+ "\n\x1B[3mWart\x1B[0m NPC = 320", Fore.GREEN + "                                         \x1B[3mCactus\x1B[0m NPC = 160\n")

    print(Fore.RED + "     Insta Sell Price =",math.trunc(wartsInstaSell), Fore.GREEN + "                                Insta Sell Price =",math.trunc(cactusInstaSell))
    print(Fore.RED + "     Buy Order Price =",math.trunc(wartsBuyOrder), Fore.GREEN + "                                 Buy Order Price =",math.trunc(cactusBuyOrder))
    print(Fore.RED + "     Estimate Coins Per Minute =", f'{wartsperminute:,}', Fore.GREEN + "                    Estimate Coins Per Minute =", f'{cactusperminute:,}')
    print(Fore.RED + "     Estimate Coin Per Hour =", f'{wartsperhour:,}', Fore.GREEN + "                    Estimate Coin Per Hour =", f'{cactusperhour:,}')
    print(Fore.RED + "     Crops per second =", f'{wartsHarvest:,}', Fore.GREEN + "                              Crops per second =", f'{cactusHarvest:,}')


    #closing function
    print(Style.RESET_ALL)
    print('PRESS ENTER TO EXIT / CTRL TO REFRESH')
    while True==True:
        if keyboard.is_pressed('enter'):
            print(Fore.BLACK + Back.GREEN + "\4may your fields be blessed inshallah\4",)
            print(Style.RESET_ALL + Back.BLACK + "                              ")
            sleep(2)
            exit()
        elif keyboard.is_pressed('ctrl'):
            main()

main()