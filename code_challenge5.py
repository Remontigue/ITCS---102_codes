n = int(input("how many slide: "))
z = 1
for x in range(n):
    for y in range(x + 1):
        print(z,end=" ")
        z = z + 1
    print()    
