# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: W1987544                  Student Name: Rikas Ilamdeen                    Date: 18.04.2023


progress_count = trailing_count =  retriever_count = exclude_count = total_count = 0
progression_list = []                                       

# ---------------------conditional statements------------------------------
def program_outcome(pass_credit, fail_credit):             
    if pass_credit == 120:
            return "Progress"
    elif pass_credit == 100:
            return "Progress (module trailer)"   
    elif 0 <= fail_credit <= 60 :
            return "Module retriever"
    elif fail_credit >= 80:
            return "Exclude" 

# ---------------------Part 1 Main Version---------------------------------
def main():
    def credit_input(prompt):                               # the credit_input function takes a prompt parameter
        while True:
            try:
                credit = int(input(prompt))                 # the variable credit assigns the value of pass_credit, defer_credit or fail_credit
                if credit not in range(0, 121, 20):
                    print("Out of range")
                else:
                    return credit
            except ValueError:
                print("Integer required")

    while True:
        pass_credit = credit_input("Please enter your credits at pass: ")               
        defer_credit = credit_input("Please enter your credit at defer: ")
        fail_credit = credit_input("Please enter your credit at fail: ")
        total_credit = sum((pass_credit, defer_credit, fail_credit))               # the values are passed to the sum() function as a tuple and return the total
        if total_credit != 120:
            print("Total incorrect")
        else:
            global progress_count, trailing_count, retriever_count, exclude_count, total_count          # global variables
            print(program_outcome(pass_credit, fail_credit))
            outcome = program_outcome(pass_credit, fail_credit)                     # the variable outcome assigns the output of student progression outcome
            if outcome == "Progress":
                progression_list.extend([outcome, pass_credit, defer_credit, fail_credit])           # using 'extend' for multiple inputs to list
                progress_count += 1

            elif outcome == "Progress (module trailer)":
                progression_list.extend([outcome, pass_credit, defer_credit, fail_credit])
                trailing_count += 1

            elif outcome == "Module retriever":
                progression_list.extend([outcome, pass_credit, defer_credit, fail_credit])
                retriever_count += 1

            elif outcome == "Exclude":
                progression_list.extend([outcome, pass_credit, defer_credit, fail_credit])
                exclude_count += 1
            total_count += 1
        print("\nWould you like to enter another set of data?")                     # the loop to predicts progression outcomes for multiple students
        data = input("Enter 'y' for yes or 'q' to quit and view results: ")      
        print()
        if data.lower() == "q":                                                     # program exit on 'q' and print Histogram
            break


# ---------------------Part 2 List (extension)-------------------------------
def list_extension():
    main()
    histogram()                                                   
                                                                
    print("Part 2: ")
    for outcome_index in range(0, len(progression_list), 4):           # References: https://docs.python.org/3/library/stdtypes.html#str.join
        print(str(progression_list[outcome_index]) + ' - ' + ', '.join(str(credit_index) for credit_index in progression_list[outcome_index+1 : outcome_index+4]))      # creates a comma-separated string of the next three elements in the list
    print()

# ---------------------Part 3 Text File (extension)---------------------------
def text_file():
    main()
    file = open("SaveData.txt", "w")                                    # open file for write
    file.write("Part 3: \n")
    for outcome_index in range(0, len(progression_list), 4):            # using this range function for find the progression outcome in list
        file.write(f"{str(progression_list[outcome_index]) + ' - ' + ', '.join(str(credit_index) for credit_index in progression_list[outcome_index+1 : outcome_index+4])}\n")      # write to file from list

    file = open("SaveData.txt", "r")                                    # file open for read
    data = file.read()                                                  # read file data
    file.close()                                                        # close file
    print(data)
    

# ---------------------Part 4 Dictionary (separate program)-------------------
progression_dictionary = {}                                             # create an empty dictionary
def dictionary():
    def credit_input(prompt):
        while True:
            try:
                credit = int(input(prompt))
                if credit not in range(0, 121, 20):
                    print("Out of range")
                else:
                    return credit
            except ValueError:
                print("Integer required")

    while True:
        student_id = input("Enter your student id: ")                                      # add key to the dictionary
        pass_credit = credit_input("Please enter your credits at pass: ")
        defer_credit = credit_input("Please enter your credit at defer: ")
        fail_credit = credit_input("Please enter your credit at fail: ")

        total_credit = sum((pass_credit, defer_credit, fail_credit))
        if total_credit != 120:
            print("Total incorrect")
        else:
            print(program_outcome(pass_credit, fail_credit))
            outcome = program_outcome(pass_credit, fail_credit)
 
        progression_dictionary[student_id] = {                                              # key : 'student_id'
        'outcome': outcome,                                                                 # values : 'outcome', 'pass_credit', 'defer_credit', 'fail_credit'
        'pass_credit': pass_credit,
        'defer_credit': defer_credit,
        'fail_credit': fail_credit
        }   

        print("\nWould you like to enter another set of data?")
        data = input("Enter 'y' for yes or 'q' to quit and view results: ")
        print()
        if data.lower() == "q":
            break

    print("Part 4:")
    for student_id, values in progression_dictionary.items():                                   # using 'for loop' for separated by items
        outcome = values['outcome']                                 
        pass_credit = values['pass_credit']
        defer_credit = values['defer_credit']
        fail_credit = values['fail_credit']

        print(f"{student_id} : {outcome} - {pass_credit}, {defer_credit}, {fail_credit}")       # print output for readabilty format using an f-string
    print()

# -------------------histogram------------------------
def histogram():                                                                                # histogram define function used in part 1, 2
    print("-" * 63)
    print("Histogram\n")                                                        
    print(f"Progress {progress_count:<2}  :", progress_count     * "*")             # got perfect space by f-string format specifiers
    print(f"Trailer {trailing_count:<3}  :", trailing_count     * "*")              # and print stars multiplicate by outcome counts
    print(f"Retriever {retriever_count:<1}  :", retriever_count    * "*")
    print(f"Excluded {exclude_count:<2}  :", exclude_count      * "*")
    print()
    print(f"{total_count} outcomes in total.")
    print("-" * 63)


# -------------------Introduction----------------------                             # this part for avoid multiple python scripts
print("""
==================== W E L C O M E ====================

Choose a part for predict student progression outcomes.

Part: 1 Main Version
Part: 2 List (extension)
Part: 3 Text File (extension)
Part: 4 Dictionary (separate program)
""")

while True:
    try:
        part = int(input('Please enter a number: '))                                 # select a part by enter a number 1,2,3 or 4
        if part == 1:
            print("\nPart 1:\n")
            main()
            histogram()
            break
        elif part == 2:
            print("\nPart 2:\n")
            list_extension()
            break
        elif part == 3:
            print("\nPart 3:\n")
            text_file()
            break
        elif part == 4:
            print("\nPart 4:\n")
            dictionary()
            break
        else:
            print("Invalid number!")
    except ValueError:
        print('Wrong selection!')
