foods = ["adobo", "tinola", "nilaga", "batchoy", "pakbet"]
            #0       #1        #2         #3         #4


# dictionary
# key, value

foods_s = {"toyo":"adobo", "soup":"tinola", "baboy":"nilaga", "damingluya":"batchoy", "vegetables":"pakbet"}

print(foods[4])

print(foods_s["toyo"])

# traversing a dictionary
for x, y in foods_s.items():
    print("key is ", x, "-- value is ", y)

