#Welcome to the share Calculator made by Bibek Adhikari.
from termcolor import colored
from sold import sold
from buy import bought
from calculationHere import calculationHere
import time

print(colored("\t Welcome to Your share watcher made By BibekAdhikari.","green"))


print("Hello there, how may i help you?")
print("Please type 1 to add the share on your Bought list.")
print("Please type 2 to add the share on your Sold list.")
print("Please type 3 if you have just Sold your share and want to check Calculation.")

try:
    options = int(input("What do you want to perform? "))
    if (options == 1 ):
        bought()
    elif(options == 2):       
        sold()        
    elif(options == 3):
        calculationHere()
    else:
        print("Please give the input Correctly.")
except:
    print(colored("Please type the Options in a Numeric Form.","red"))