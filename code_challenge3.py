Name = input("sender name -----> ")
Item = input("item -----> ")
Fragile = input("Fragile? -----> ")
Weight = float(input("Weight of the Item: "))
Distance = float(input("Distance: "))
Express = input("Express? -----> ")
International = input("International? -----> ")

BaseCost = (Weight * 2.50) + (Distance * 0.15)

if Weight <= 2 and Distance <= 100 and Express == "no" and International == "no":
    Total = 0

elif International == "yes" and Express == "yes":
    Total = (BaseCost * 1.40) + 50

elif Express == "yes" or (International == "yes" and Weight > 20):
    Total = (BaseCost * 1.20) + 25

elif Weight > 30 or Distance > 1000:
    Total = BaseCost + 30

else:
    Total = BaseCost

print()
print("Sender Name: ", Name)
print("Item: ", Item)
print("Fragile: ", Fragile)
print("Weight: ", Weight, "kg")
print("Distance: ", Distance, "km")
print("Express?: ", Express)
print("International: ", International)
print("Total: ", Total)