diction={}
while True:
    print("\nDictionary Management System")
    print("1. Add a Word")
    print("2. Search for Meaning")
    print("3. Display All Words")
    print("4. Update Meaning")
    print("5. Delete Word")
    print("6. Exit")

    Choice = input("Enter your choice: ")

    if Choice == "1":
        Keyword = input("Enter the word : ").lower()
        MeaningValue = input("Enter the meaning : ")
        diction[Keyword] = MeaningValue
        print("Word added successfully!")

    elif Choice == '2':
        Keyword = input("Enter the word to search : ").lower()
        if Keyword in diction:
            print("Meaning :",diction[Keyword])
        else:
            print("Word not found in the dictionary.")
    elif Choice == '3':
        if diction:
            print("Enter the word in the dictionary and their meanings:")
            for Keyword, MeaningValue in diction.items():
                print(f"{Keyword} : {MeaningValue}")
        else:
            print("Dictionary is empty.")
    elif Choice == '4':
        Keyword = input("Enter the word to update meaning : ").lower()
        if Keyword in diction:
            newmeaningvalue = input("Enter the new meaning :")
            diction[Keyword] = newmeaningvalue
            print("Meaning updated successfully!")
            print("Updated Meaning :",diction[Keyword])
    elif Choice == '5':
        Keyword = input("Enter the word to delete : ").lower()
        if Keyword in diction:
            del diction[Keyword]
            print("Deleted the word successfully")
        else:
            print("Word is not found in the dictionary")
    elif Choice == '6':
        print("Exit the programm.......")
        break
    else:
        print("Invalid choice! Please enter a valid option.")