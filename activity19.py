
isExpensive = True #boolean variable

while isExpensive == True:
    x = bool(input("you are beautiful? (Yes or No) --> "))

    if x == True:
        print("Continuing Loop")
        continue

    else:
        print("Exiting Loop")
        break

