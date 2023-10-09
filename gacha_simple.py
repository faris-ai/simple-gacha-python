from numpy.random import choice
from colorama import Fore, Back
import json

f = open('data.json')
data_gacha = json.load(f)
f.close()
# f = open('counter_data.json')
# counter_data = json.load(f)

counter_prob = {"normal":0,"rare":0,"epic":0,"epic (100)":0,"legend":0}
counter_gacha = 0
counter_epic = 0
legend_at = []
while True:
    f = open('counter_data.json')
    counter_data = json.load(f)
    f.close()
    print("Enter number you want to gacha:")
    while True:
        try:
            input_g = int(input())
            break
        except:
            print("Enter the number!!")
    
    i = 0
    is_legend = False 
    while i < input_g:
        counter_gacha += 1
        counter_epic += 1
        add_string = ""
        if counter_epic != 100:
            item_choosen_grade = choice(list(data_gacha["probability"].keys()),p=list(data_gacha["probability"].values()))
            item_choosen_type = dict()
            counter_prob[item_choosen_grade] +=1
            if item_choosen_grade == "legend":
                item_choosen_type = list(data_gacha["items"]["legend"].keys())[0]
                add_string = "(l) "
                is_legend = True
                legend_at.append(counter_gacha)
            elif item_choosen_grade == "epic":
                item_choosen_type = list(data_gacha["items"]["epic"].keys())[0]
                counter_epic = 0
                add_string = "(e) "
            elif item_choosen_grade == "rare":
                item_choosen_type = choice(list(data_gacha["items"]["rare"]["probability"].keys()),p=list(data_gacha["items"]["rare"]["probability"].values()))
                add_string = "(r) "
            elif item_choosen_grade == "normal":
                item_choosen_type = choice(list(data_gacha["items"]["normal"]["probability"].keys()),p=list(data_gacha["items"]["normal"]["probability"].values()))
                add_string = "(n) "
            
            # item = choice()

            # print(item_choosen_grade)
            # print(item_choosen_type)
            item = choice(data_gacha["items"][item_choosen_grade][item_choosen_type])
            # print(item)
            counter_data[item_choosen_type][add_string+item] += 1
        else:
            counter_prob["epic (100)"] +=1
            item = choice(data_gacha["items"]["epic"]["charas"])
            add_string = "(e) "
            counter_data["charas"][add_string+item] += 1
            counter_epic = 0
        i+=1
    for c in counter_prob:
        txt = "{}: {}".format(c, counter_prob[c]).title()
        if c == "legend":
            print(Fore.YELLOW + txt)
        elif c == "epic" or c == "epic (100)" :
            print(Fore.MAGENTA + txt)
        elif c == "rare":
            print(Fore.BLUE + txt)
        else:
            print(Fore.GREEN + txt)
        # print(Fore.WHITE)
    for cc in counter_data["charas"]:
        if counter_data["charas"][cc] > 0:
            txt = "{}: {}".format(cc, counter_data["charas"][cc]).title()
            if "(l)" in cc:
                print(Fore.YELLOW + txt)
            elif "(e)" in cc:
                print(Fore.MAGENTA + txt)
            elif "(r)" in cc:
                print(Fore.BLUE + txt)
            else:
                print(Fore.GREEN + txt)
    for cc in counter_data["weapolement"]:
        if counter_data["weapolement"][cc] > 0:
            txt = "{}: {}".format(cc, counter_data["weapolement"][cc]).title()
            if "(r)" in cc:
                print(Fore.BLUE + txt)
            else:
                print(Fore.GREEN + txt)
    if is_legend:
        txt_legend = ""
        for l in legend_at:
            txt_legend += str(l)
            if l != legend_at[len(legend_at) - 1]:
                txt_legend += ", "
        print(Fore.WHITE,Back.GREEN+"\nCongratulation you got legend item at {} gachas".format(txt_legend))
        print(Back.BLACK)
        is_legend = False
    print(Fore.WHITE+"\nYou have gacha {} times".format(counter_gacha))
    print("{} times gacha for epic item".format(100 - counter_epic))
    print("\nContinue?")
    que= input()
    if que == "n":
        break
    # if x == "Fire":
    #     print(Fore.RED + x)
    #     list_counter[0] += 1
    # elif x == "Water":
    #     print(Fore.BLUE + x)
    #     list_counter[1] += 1
    # elif x == "Earth":
    #     print(Fore.YELLOW + x)
    #     list_counter[2] += 1
    # elif x == "Air":
    #     print(Fore.WHITE + x)
    #     list_counter[3] += 1
    

# print(Back.WHITE+"Fire: {}. Water: {}. Earth: {}. Air: {}.".format(list_counter[0],list_counter[1],list_counter[2],list_counter[3]))