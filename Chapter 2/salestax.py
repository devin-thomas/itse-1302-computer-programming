#Devin Thomas
#ITSE 1302-003
#June 8, 2023

purchaseAmount = float(input("Enter the amount of the purchase: "))

stateTax = purchaseAmount * 0.04
countyTax = purchaseAmount * 0.02
totalTax = stateTax + countyTax
totalSale = purchaseAmount + totalTax

print("Purchase Amount: $%.2f" % purchaseAmount)
print("State Sales Tax: $%.2f" % stateTax)
print("County Sales Tax: $%.2f" % countyTax)
print("Total Sales Tax: $%.2f" % totalTax)
print("Total Sale: $%.2f" % totalSale)