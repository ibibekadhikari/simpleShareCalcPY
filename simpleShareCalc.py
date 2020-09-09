# Bought and Sold items here. :) Happy investing & Trading.
from termcolor import colored

#You have to put the company name that you have bought recently in the same given format inside list: 'Company name: UnitsOfShare * AmountPerUnit:

#Company: UnitsOfShare * AmountPerShare.
boughtList = [
    'nric: 20 * 584.64',
    'ail: 10 * 100']

#You have to put the company name that you have sold recently in the same given format inside list: 'Company name: UnitsOfShare * AmountPerUnit:

soldList = [
    'nric: 20 * 643',
    'ail: 10 * 282',
    ]

def bought(x):
    for i in boughtList:
        if (i.split(': ')[0]) == x:
            return (i.split(': ')[1])
        else:
            pass    

def sold(x):
    for i in soldList:

       if (i.split(': ')[0]) == x:
          return (i.split(': ')[1])
       else:
          pass    

def calculateHere(company):    
    try:
        buyValue = bought(company)
        finalBuy = eval(buyValue)
        soldValue = sold(company)
        finalSold = eval(soldValue)

        totalValue = round(finalSold - finalBuy, 2)
        if totalValue > 0:
            print(colored("Congratulations, You have successfully earned: {}.".format(totalValue),"green"))
        else:
            print(colored("Oh no, you have loose some amount of money: {}.".format(totalValue),"red"))
    except:
        company = company.upper()
        print(colored("I am very sorry to inform you that, either you don't have bought the {} share or sold this share.".format(company),"red"))




#Enter your company name which you have recently Sold.
companyName = input("Enter a Company name here: ")

#If your company has not been listed to Buy or Sell then it won't work. :)

calculateHere(companyName)

