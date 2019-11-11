from functional import Funct

funct = Funct()


def menu():
    print("What would you like to do?")
    print("1. Add element")
    print("2. Remove element")
    print("3. Reverse list")
    print("4. Search element in list")
    print("5. Count character of elements in list")
    print("6. Compare elements in list")
    print("7. Create XML-file from list")
    print("8. Read from file")
    print("9. Inner search")
    print("10. Character check")


while True:
    menu()
    choice = input()
    if choice == "1":
        funct.add()
    elif choice == "2":
        funct.remove()
    elif choice == "3":
        funct.reverse()
    elif choice == "4":
        funct.search()
    elif choice == "5":
        funct.count()
    elif choice == "6":
        funct.compare()
    elif choice == "7":
        funct.create_xml()
    elif choice == "8":
        funct.from_file()
    elif choice == "9":
        funct.inner_search()
    elif choice == "10":
        funct.character_check()
    else:
        print("Wrong input")
