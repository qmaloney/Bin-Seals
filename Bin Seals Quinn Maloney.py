while True:
    #Intro
    print("Script to Verify Proper E-Waste Bin Seals in Ticket Communications:")
    print("")

    print("Please Enter Old E-Waste Bin Seals:")

    #Old Bin Seals
    Old_Bin_Seals_List = []
    while True:
            try:
                Old_1 = int(input("Enter Old Bin Seal 1: "))
                Old_2 = int(input("Enter Old Bin Seal 2: "))
                Old_3 = int(input("Enter Old Bin Seal 3: "))
                Old_4 = int(input("Enter Old Bin Seal 4: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    Old_Bin_Seals_List.append(Old_1)
    Old_Bin_Seals_List.append(Old_2)
    Old_Bin_Seals_List.append(Old_3)
    Old_Bin_Seals_List.append(Old_4)

    #Sort Old Bin Seals:
    Old_Sorted = sorted(Old_Bin_Seals_List)
    print("Old Bin Seals:")
    print(Old_Sorted)
    
    #Verify
    print("Please Confirm these are the Correct Old Bin Seals before moving on:")
    while True:
                print(Old_Sorted)
                repeat = input("Are these the Correct Bin Seals? (yes/no): ")
                try:
                    if repeat.lower() == "yes":
                        break
                    elif repeat.lower() == "no":
                        print("Please Re-Enter Old Bin Seals:")                        
                        while True:
                            try:
                                Old_1 = int(input("Enter Old Bin Seal 1: "))
                                Old_2 = int(input("Enter Old Bin Seal 2: "))
                                Old_3 = int(input("Enter Old Bin Seal 3: "))
                                Old_4 = int(input("Enter Old Bin Seal 4: "))
                                break
                            except ValueError:
                                 print("Invalid input. Please enter a valid number.")
                        Old_Bin_Seals_List = []
                        Old_Bin_Seals_List.append(Old_1)
                        Old_Bin_Seals_List.append(Old_2)
                        Old_Bin_Seals_List.append(Old_3)
                        Old_Bin_Seals_List.append(Old_4)
                        Old_Sorted = sorted(Old_Bin_Seals_List)         
                        #break  # Exit the loop if 'no' is entered
                    else:
                        raise ValueError  # Raise an error for any other input
                except ValueError:
                    print("Invalid input. Please enter either 'yes' or 'no'.")

    #New Bin Seals
    print("Please Enter New Bin Seals:")

    New_Bin_Seals_List = []

    while True:
            try:
                New_1 = int(input("Enter New Bin Seal 1: "))
                New_2 = int(input("Enter New Bin Seal 2: "))
                New_3 = int(input("Enter New Bin Seal 3: "))
                New_4 = int(input("Enter New Bin Seal 4: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    New_Bin_Seals_List.append(New_1)
    New_Bin_Seals_List.append(New_2)
    New_Bin_Seals_List.append(New_3)
    New_Bin_Seals_List.append(New_4)

    #Sort New Bin Seals:
    New_Sorted = sorted(New_Bin_Seals_List)
    print("Old Bin Seals:")
    print(New_Sorted)


    #Verify
    print("Please Confirm these are the Correct New Bin Seals before moving on:")
    while True:
                print(New_Sorted)
                repeat = input("Are these the Correct Bin Seals? (yes/no): ")
                try:
                    if repeat.lower() == "yes":
                        break
                    elif repeat.lower() == "no":
                        print("Please Re-Enter New Bin Seals:")                        
                        while True:
                            try:
                                New_1 = int(input("Enter New Bin Seal 1: "))
                                New_2 = int(input("Enter New Bin Seal 2: "))
                                New_3 = int(input("Enter New Bin Seal 3: "))
                                New_4 = int(input("Enter New Bin Seal 4: "))
                                break
                            except ValueError:
                                 print("Invalid input. Please enter a valid number.")
                        New_Bin_Seals_List = []
                        New_Bin_Seals_List.append(New_1)
                        New_Bin_Seals_List.append(New_2)
                        New_Bin_Seals_List.append(New_3)
                        New_Bin_Seals_List.append(New_4)
                        New_Sorted = sorted(New_Bin_Seals_List)         
                        #break  # Exit the loop if 'no' is entered
                    else:
                        raise ValueError  # Raise an error for any other input
                except ValueError:
                    print("Invalid input. Please enter either 'yes' or 'no'.")

    #Print summary:
    print("SUMMARY:")
    print("")
    print("Old Bin Seals:", Old_Sorted)
    print("")
    print("New Bin Seals:", New_Sorted)
    print("")
    while True: 
        choice = input ("Do you want to restart the script? (y/n)")
        if choice.lower() == "n":
            print("Goodbye!")
            break
        if choice.lower() == "y":
             break



