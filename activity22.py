anime_genre = ["isekai", "romance", "horror", "adventure,", "drama"]
anime_title = []

while True:
    ans = input("Do you watch any anime ---> (yes / no): ")

    if ans.lower() == "yes":
        print("what is its type -- ? select from the list ")
        for x in anime_type:
            print(x)
        type = input("type ---> ")


        title = input("what is the title of the anime---> ")
        anime_title.append(title)
        continue
    else:
        print("Goods ")
        break 