usernames = []
while True:
    name = input("Enter a name: ")
    if usernames.count(name) >= 1:
        print("Username already in use!")
    elif len(name) > 20:
        print("Username has too many characters!")
    else:
        print("Username created!")
        usernames.append(name)


