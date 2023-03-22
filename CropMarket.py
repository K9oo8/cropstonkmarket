import requests as req
import json
import math
from colorama import Fore, Back, Style

url = "https://api.hypixel.net/skyblock/bazaar"

r = req.get(url).json()

# Harvest value is equal to 1 minute at optimal speed
carrotHarvest = 39519
sugarHarvest = 27074 #last update Mar/02/23
potatoHarvest = 35840
wheatHarvest = 12407
melonHarvest = 58080
pumpkinHarvest = 12180
mushroomHarvest = 23104
cocoaHarvest = 35260
wartsHarvest = 31944
cactusHarvest = 19335

#just defining stuff
mushroomPerMinute = 0
carrotsPerMinute = 0
sugarPerMinute = 0
potatoPerMinute = 0
wheatPerMinute = 0
melonperMinute = 0
pumpkinPerMinute = 0
cocoaPerMinute = 0
wartsPerMinute = 0
cactusPerMinute = 0

#filtering
mushroomInstaSell = r["products"]["ENCHANTED_RED_MUSHROOM"]['quick_status']['sellPrice']
carrotInstaSell = r["products"]["ENCHANTED_CARROT"]['quick_status']['sellPrice']
sugarInstaSell = r["products"]["ENCHANTED_SUGAR"]['quick_status']['sellPrice']
potatoInstaSell = r["products"]["ENCHANTED_POTATO"]['quick_status']['sellPrice']
wheatInstaSell = r["products"]["ENCHANTED_HAY_BLOCK"]['quick_status']['sellPrice']
melonInstaSell = r["products"]["ENCHANTED_MELON"]['quick_status']['sellPrice']
pumpkinInstaSell = r["products"]["ENCHANTED_PUMPKIN"]['quick_status']['sellPrice']
cocoaInstaSell = r["products"]["ENCHANTED_COCOA"]['quick_status']['sellPrice']
wartsInstaSell = r["products"]["ENCHANTED_NETHER_STALK"]['quick_status']['sellPrice']
cactusInstaSell = r["products"]["ENCHANTED_CACTUS_GREEN"]['quick_status']['sellPrice']

#more defining
mushroomNPC = 640
carrotNPC = 160
sugarNPC = 320
potatoNPC = 160
wheatNPC = 1300
melonNPC = 160
pumpkinNPC = 640
cocoaNPC = 480
wartsNPC = 320
cactusNPC = 160

#use bigger one
mushroom = max(mushroomInstaSell, mushroomNPC)
carrot = max(carrotInstaSell, carrotNPC)
sugar = max(sugarInstaSell, sugarNPC)
potato = max(potatoInstaSell, potatoNPC)
wheat = max(wheatInstaSell, wheatNPC)
melon = max(melonInstaSell, melonNPC)
pumpkin = max(pumpkinInstaSell, pumpkinNPC)
cocoa = max(cocoaInstaSell, cocoaNPC)
warts = max(wartsInstaSell, wartsNPC)
cactus = max(cactusInstaSell, cactusNPC)

#calculate how much you make inclusive of mooshroom cow pet
def timeProfit(cropIn, cropharvest, ecraft, multiplier): #Wheat Ecraft = 1296 else 160/multiplier= 2 for cactus/sugarcane 0 for mushroom 1 for else
    minuteout = ((cropIn*cropharvest/ecraft)+(mushroom*1200/160*multiplier))
    return minuteout

mushroomPerMinute = timeProfit(mushroom, mushroomHarvest, 160, 0)
carrotsPerMinute = timeProfit(carrot, carrotHarvest, 160, 1)
sugarPerMinute = timeProfit(sugar, sugarHarvest, 160, 2)
potatoPerMinute = timeProfit(potato, potatoHarvest, 160, 1)
wheatPerMinute = timeProfit(wheat, wheatHarvest, 1296, 1)
melonPerMinute = timeProfit(melon, melonHarvest, 160, 1)
pumpkinPerMinute = timeProfit(pumpkin, pumpkinHarvest, 160, 1)
cocoaPerMinute = timeProfit(cocoa, cocoaHarvest, 160, 1)
wartsPerMinute = timeProfit(warts, wartsHarvest, 160, 1)
cactusPerMinute = timeProfit(cactus, cactusHarvest, 160, 2)

#display module
def display(displayname, crop, cpm, cropNPC):
    print(displayname)
    if crop <= cropNPC:
        print("     Sell Price:", crop, "(NPC)")
    else:
        print("     Sell Price:", f'{math.trunc(crop):,}')
    #print("     Coins per Minute:", f'{math.trunc(cpm):,}')
    print("     Coins per Hour:", f'{math.trunc(cpm*60):,}')
    print(Style.RESET_ALL, end =" "),

print(Fore.LIGHTMAGENTA_EX + "\x1B[6m$$$$$$$$\$$\   $$\ $$$$$$\ $$\   $$\       $$$$$$$\ $$$$$$\$$$$$$$$\ $$$$$$\ $$\   $$\$$$$$$$$\ $$$$$$\         $$$$$$\ $$$$$$$$\$$$$$$$$\       $$\      $$\ $$$$$$\ $$\   $$\$$$$$$$$\$$\     $$\ ")
print("$$  _____$$ |  $$ $$  __$$\$$ | $$  |      $$  __$$\\\_$$ _\___$$  __$$  __$$\$$ |  $$ $$  _____$$  __$$\       $$  __$$\$$  _____\__$$  __|      $$$\    $$$ $$  __$$\$$$\  $$ $$  _____\$$\   $$  |")
print("$$ |     $$ |  $$ $$ /  \__$$ |$$  /       $$ |  $$ | $$ |    $$ |  $$ /  \__$$ |  $$ $$ |     $$ /  \__|      $$ /  \__$$ |        $$ |         $$$$\  $$$$ $$ /  $$ $$$$\ $$ $$ |      \$$\ $$  / ")
print("$$$$$\   $$ |  $$ $$ |     $$$$$  /        $$$$$$$\ | $$ |    $$ |  $$ |     $$$$$$$$ $$$$$\   \$$$$$$\        $$ |$$$$\$$$$$\      $$ |         $$\$$\$$ $$ $$ |  $$ $$ $$\$$ $$$$$\     \$$$$  /  ")
print("$$  __|  $$ |  $$ $$ |     $$  $$<         $$  __$$\  $$ |    $$ |  $$ |     $$  __$$ $$  __|   \____$$\       $$ |\_$$ $$  __|     $$ |         $$ \$$$  $$ $$ |  $$ $$ \$$$$ $$  __|     \$$  /   ")
print("$$ |     $$ |  $$ $$ |  $$\$$ |\$$\        $$ |  $$ | $$ |    $$ |  $$ |  $$\$$ |  $$ $$ |     $$\   $$ |      $$ |  $$ $$ |        $$ |         $$ |\$  /$$ $$ |  $$ $$ |\$$$ $$ |         $$ |    ")
print("$$ |     \$$$$$$  \$$$$$$  $$ | \$$\       $$$$$$$  $$$$$$\   $$ |  \$$$$$$  $$ |  $$ $$$$$$$$\\\$$$$$$  |      \$$$$$$  $$$$$$$$\   $$ |         $$ | \_/ $$ |$$$$$$  $$ | \$$ $$$$$$$$\    $$ |    ")
print("\__|      \______/ \______/\__|  \__|      \_______/\______|  \__|   \______/\__|  \__\________|\______/        \______/\________|  \__|         \__|     \__|\______/\__|  \__\________|   \__|    \x1B[0m")

print(Fore.MAGENTA)
display("Mushroom", mushroom, mushroomPerMinute, mushroomNPC)
print(Fore.LIGHTRED_EX)
display("Carrots", carrot, carrotsPerMinute, carrotNPC)
print(Fore.LIGHTGREEN_EX)
display("Sugar Cane", sugar, sugarPerMinute, sugarNPC)
print(Fore.YELLOW)
display("Potato", potato, potatoPerMinute, potatoNPC)
print(Fore.LIGHTYELLOW_EX)
display("Wheat", wheat, wheatPerMinute, wheatNPC)
print(Fore.GREEN)
display("Melon", melon, melonPerMinute, melonNPC)
print(Fore.BLUE)
display("Pumpkin", pumpkin, pumpkinPerMinute, pumpkinNPC)
print(Fore.CYAN)
display("Cocoa Beans", cocoa, cocoaPerMinute, cocoaNPC)
print(Fore.RED)
display("Nether Warts", warts, wartsPerMinute, wartsNPC)
print(Fore.GREEN)
display("Cactus", cactus, cactusPerMinute, cactusNPC)

input("\nPress Enter to Exit")