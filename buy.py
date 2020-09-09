import json
from termcolor import colored
def bought():
    name = input("Enter comapny Name: ")
    price = float(input("Enter the amount per Share: "))
    unit = float(input("Enter the total Units: "))

    boughtNew = {
        "name": name,
        "price": price,
        "units": unit
    }

    with open("boughtShares.json") as buyOne:

        buyone = json.load(buyOne)
        temp = buyone["buyList"]
        temp.append(boughtNew)

    toBeAdded = {
        "buyList": temp
    }

    # temp.append(boughtNew)
    # print(temp)

    with open ("boughtShares.json","w") as bought:
        json.dump(toBeAdded, bought, indent=2)
    
    print(colored("Thankyou there, Your {units} Units of Share which costs {price} per share of Company {company} has been Added into Bought List. :) ".format(units=unit, price=price, company=name.upper()),"green"))


