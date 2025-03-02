def getUsername(first, last):
    s = first + "." + last
    return s.lower()

def main():
    firstName = input("First")
    lastName = input("Last")
    username = getUsername(firstName, lastName)
    print(username)

if __name__ == "__main__":
    main()