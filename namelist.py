usernames = []
while True:
    name = input("Enter a name: ")
    if name in usernames:
        print("Username already in use!")
    elif len(name) > 20:
        print("Username has too many characters!")
    else:
        usernames.append(name)
        print("Username created!")


