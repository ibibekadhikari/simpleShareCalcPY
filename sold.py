import json
from termcolor import colored

def sold():
    name = input("Enter comapny Name: ")
    price = float(input("Enter the amount per Share: "))
    unit = float(input("Enter the total Units: "))

    soldNew = {
        "name": name,
        "price": price,
        "units": unit
    }

    with open("soldShares.json") as soldOne:

        soldone = json.load(soldOne)
        temp = soldone["soldList"]
        temp.append(soldNew)

    toBeAdded = {
        "soldList": temp
    }

    # temp.append(boughtNew)
    # print(temp)

    with open ("soldShares.json","w") as sold:
        json.dump(toBeAdded, sold, indent=2)

    print(colored("Thankyou there, Your {units} Units of Share which costs {price} per share of Company {company} has been Added into SoldList. :) ".format(units=unit, price=price, company=name.upper()),"green"))
