from gettext import install
import math
import datetime
now = datetime.datetime.now()

#Input questions

Price_meal = float(input(f"What is the price of a child's meal?: "))
Price_adult = float(input(f"What is the price of an adult's meal?: "))
Many_Children = int(input(f"How many children are there?: "))
Many_adult = int(input(f"How many adults are there?: "))
Tax = float(input(f"What is the sales tax rate?: "))
Want_drink = int(input(f"Do you want a drink?: Answer 1 whit drink or 2 without drinks : "))



#Conditional drink
if (Want_drink == 1):
    Drink = float(input(f"Enter price of drink: "))
    Drink_cant = float(input(f"Enter the number of drinks: "))
else:
     print("without drinks")
     Drink = 0
     Drink_cant = 0

#calculating 
adult_price = Price_meal * Many_Children #children price
children_price = Price_adult * Many_adult # adult price
Price_drinks = Drink * Drink_cant #Calculating drinks
subtotal_price_without_tip = adult_price + children_price + Price_drinks#  subtotal
tip = subtotal_price_without_tip * 0.10
subtotal_price = adult_price + children_price + Price_drinks + tip

#Calculationg taxes
taxes_sales = (Tax * subtotal_price)/100

#calculating total
total_sales = subtotal_price + taxes_sales 


print ("\n \nDate and time of purchase : " + now.strftime("%Y-%m-%d %H:%M:%S"))
print("\n \nSubtotal: $" + str(subtotal_price))
print("Sales Drink: $" + str(Price_drinks))
print("Sales Taxes: ${0:.2f}".format(taxes_sales))
print("Tip: ${0:.2f}".format(tip))
print("------------------")
print("Total: $" + str(total_sales))

#PAY
Payment = float(input(f"\n \n What is the payment amount?: $"))

#Calculating change
change = Payment - total_sales
print("Change : ${0:.2f}".format(change))
print("\n \n Thank for your preference, Have a nice Day.")
