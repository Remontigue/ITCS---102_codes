name = input("Your NAME ----->  ")
age = int(input("Input Your AGE ----->  "))

print("HI," , name, "That age is considered as ")
if age >= 13 and age <= 19:
	print("Teenager")
elif age >= 6 and age <= 12:
	print("School age")
elif age >= 3 and age <= 5:
	print("Preschooler")
elif age >= 3 and age <= 1:
	print("Todler")

else:
	print("YOU'RE HUMAN")