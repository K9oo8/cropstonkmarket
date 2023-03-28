import requests as req
import json
from datetime import datetime


with open('index.md', 'w') as index:
    index.write("last code update march 24th \n")
    index.write(f"Last BZ API Call {datetime.now():%A, %B %d %H:%M:%S} UTC \n\n")

    url = "https://api.hypixel.net/skyblock/bazaar"

    r = req.get(url).json()
    response = req.get(url)

    if response.status_code != 200:
        index.write("!!!API DOWN!!!")
        exit()


    # Harvest value is equal to 1 minute at optimal speed assuming using 3/4th fermento ranchers boots
    carrotHarvest = 39519
    sugarHarvest = 27074 #last update Mar/02/23
    potatoHarvest = 35840
    wheatHarvest = 12407
    seedHarvest = 1
    melonHarvest = 58080
    pumpkinHarvest = 12180
    mushroomHarvest = 13155*2
    cocoaHarvest = 35260
    wartsHarvest = 31944
    cactusHarvest = 19335

    #just defining stuff
    mushroomPerHour = 0
    carrotsPerHour = 0
    sugarPerHour = 0
    potatoPerHour = 0
    wheatPerHour = 0
    melonPerHour = 0
    pumpkinPerHour = 0
    cocoaPerHour = 0
    wartsPerHour = 0
    cactusPerHour = 0

    items = {
            "ENCHANTED_RED_MUSHROOM": "mushroom",
            "ENCHANTED_CARROT": "carrot",
            "ENCHANTED_SUGAR": "sugar",
            "ENCHANTED_POTATO": "potato",
            "ENCHANTED_HAY_BLOCK": "wheat",
            "ENCHANTED_SEEDS": "seeds",
            "ENCHANTED_MELON": "melon",
            "ENCHANTED_PUMPKIN": "pumpkin",
            "ENCHANTED_COCOA": "cocoa",
            "ENCHANTED_NETHER_STALK": "warts",
            "ENCHANTED_CACTUS_GREEN": "cactus",
            "FERMENTO": "fermento",
            "SQUASH": "squash",
            "CROPIE": "cropie"
        }

    instaSell = {}


    for item, var_name in items.items():
        instaSell[var_name] = r["products"][item]['quick_status']['sellPrice']


    #insta sell
    mushroom = instaSell["mushroom"]
    carrot = instaSell["carrot"]
    sugar = instaSell["sugar"]
    potato = instaSell["potato"]
    wheat = instaSell["wheat"]
    seeds = instaSell["seeds"]
    melon = instaSell["melon"]
    pumpkin = instaSell["pumpkin"]
    cocoa = instaSell["cocoa"]
    warts = instaSell["warts"]
    cactus = instaSell["cactus"]
    fermento = instaSell["fermento"]
    squash = instaSell["squash"]
    cropie = instaSell["cropie"]


    #calculate fermento squash cropie stuff per hour profit (assuming normal distribution)
        #cropies 1/2500 or 28.8 per hour
    cropie = cropie*28.8
        #squash 1/5000 or 14.4 per hour
    squash = squash*14.4
        #fermento 1 tall 1/16,666 or 4.3 ish per hour
    fermentosingle = fermento*4.3
        #fermento 2 tall 1/8,333 or 8.6 ish per hour
    fermentodouble = fermento*8.6


    #calculate how much you make inclusive of fermento squash cropie drops
    def timeProfit(cropIn, cropharvest, ecraft, armordrops): #Wheat Ecraft = 1296 else 160
        hourout = ((cropIn*cropharvest/ecraft)*60 + armordrops + (cropharvest*0.2*60))
        return hourout

    #cropies
    potatoPerHour = timeProfit(potato, potatoHarvest, 160, cropie)
    carrotsPerHour = timeProfit(carrot, carrotHarvest, 160, cropie)
    wheatPerHour = timeProfit(wheat, wheatHarvest, 1296, cropie)+(seeds*seedHarvest/160*60)

    #squash
    melonPerHour = timeProfit(melon, melonHarvest, 160, squash)
    pumpkinPerHour = timeProfit(pumpkin, pumpkinHarvest, 160, squash)
    cocoaPerHour = timeProfit(cocoa, cocoaHarvest, 160, squash)

    #fermento
    wartsPerHour = timeProfit(warts, wartsHarvest, 160, fermentosingle)
    mushroomPerHour = timeProfit(mushroom, mushroomHarvest, 160, fermentodouble)

    #doublefermento
    sugarPerHour = timeProfit(sugar, sugarHarvest, 160, fermentodouble)
    cactusPerHour = timeProfit(cactus, cactusHarvest, 160, fermentosingle)

    #highest crop for going to blinkerton
    crop_max = max(mushroomPerHour, carrotsPerHour, sugarPerHour, potatoPerHour, wheatPerHour, melonPerHour, pumpkinPerHour, cocoaPerHour, wartsPerHour, cactusPerHour)

    

    #display module
    def display(displayname, crop, cph):
        index.write(f'{displayname} \n\n')
        index.write(f'     Sell Price: {crop:,.0f} \n\n')
        index.write(f'     Coins per Hour: {cph:,.0f} \n\n\n')
        

    #THERE WAS A BETTER WAY TO DO THIS GOOD JOB ME

    display("Mushroom", mushroom, mushroomPerHour)

    display("Carrots", carrot, carrotsPerHour)

    display("Sugar Cane", sugar, sugarPerHour)

    display("Potato", potato, potatoPerHour)

    display("Wheat (& Seeds)", wheat, wheatPerHour)

    display("Melon", melon, melonPerHour)

    display("Pumpkin", pumpkin, pumpkinPerHour)

    display("Cocoa Beans", cocoa, cocoaPerHour)

    display("Nether Warts", warts, wartsPerHour)

    display("Cactus", cactus, cactusPerHour)
