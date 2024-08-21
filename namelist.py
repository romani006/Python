usernames = []
while True:
    name = input("Enter a name: ")
    if usernames.count(name) >= 1:
        print("Username already in use!")
    else:
        print("Username created!")
        usernames.append(name)


