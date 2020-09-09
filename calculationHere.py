from termcolor import colored
import json

finalBoughtValue = 0
finalSoldValue = 0

soldUnits = 0
soldValue = 0

boughtUnits = 0
boughtValue = 0

sebonCharge = 0.015/100
dpCharge = 25
tax = 5/100
profitAfterTax = 0

def calculationHere():

    name = input("Enter comapny Name that you want to perform calculation: ")

    ipoOrfpo = input("Did you purchase your Share as IPO or FPO? \n Please write IPO or FPO: ").upper()
    
    try:
        with open("soldShares.json") as soldOne:
            dataSold = json.load(soldOne)
            for i in dataSold['soldList']:
                if (name == i['name']):
                    soldValue = i['price']
                    soldUnits = i['units']
                    break;
                else:
                    pass

        with open("boughtShares.json") as boughtOne:
            dataBought = json.load(boughtOne)
            for i in dataBought['buyList']:
                if (name == i['name']):
                    boughtValue = i['price']
                    boughtUnits = i['units']
                    break;
                else:
                    pass
        
        boughtValue = boughtValue * boughtUnits
        
        if (ipoOrfpo == "FPO"):
            if (boughtValue <= 5000):            
                brokerCommision = 25
                finalBoughtValue = boughtValue + brokerCommision + dpCharge

            elif (boughtValue <= 100000):
                brokerCommision = 0.6/100
                finalBoughtValue = boughtValue + (boughtValue * brokerCommision) + dpCharge
            else:
                brokerCommision = 0.55/100
                finalBoughtValue = boughtValue + (boughtValue * brokerCommision) + dpCharge        
        else:
            boughtValue = boughtValue
            finalBoughtValue = boughtValue

        soldValue = soldValue * soldUnits
        
        if (soldValue <= 4000):
            brokerCommision = 25
            sebonCharges = soldValue * sebonCharge - dpCharge
        elif (soldValue <= 100000):
            brokerCommision = soldValue * (0.6/100)
            sebonCharges = soldValue * sebonCharge
            finalSoldValue = soldValue - brokerCommision - sebonCharges - dpCharge 
        else:
            print("The Amount may be Huge, Contact ADMIN. :)")

        profitValue = finalSoldValue - finalBoughtValue
        profitAfterTax = profitValue - (profitValue * tax)
        
        print(colored("Here goes your Calculation; ","green"))

        print("Sold Share Amount: ",soldValue)
        print("Bought Share Amount : ",boughtValue)
        print("Broker Commision ; ", brokerCommision)
        print("Sebon charge ", sebonCharges)
        print("DP FEE : ", dpCharge)
        print("Capital Gain : ",profitValue)
        print("Capital Tax : ", profitValue * tax)
        print("Total Profit : ", profitAfterTax)
    except:
        print(colored("You may have mistyped the Company Name. \n Please make sure you have added the company name in BoughtList and SoldList.","red"))