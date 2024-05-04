from cipher import encrypt, decrypt


def main():
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Sign file")
    print("4. Verify signature")
    print("5. Show parameters")
    choice = input("Select option: ")

    if choice == "1":
        encrypt()
    elif choice == "2":
        decrypt()
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    else:
        print("Wrong choice")


if __name__ == "__main__":
    main()
