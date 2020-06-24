ages = {'cody':17, 'larry':12, 'moss':30, 'josh':8, 'eren':18, 'miku':17, 'uno':1, 'gary':24}

# GUIDE
def guide():
    print("""type the following for the options:
1: name list
2: age check
3: exit
""")

# NAME. LISt
def name_list():
    print("The following people are in the age list: \n")
    for name, age in ages.items():
        print(name.title())
    print("")

# AGE CHECK
def age_check():
    name = input("Who's age would you like to check \n").lower().strip()
    if name in ages:
        print("{} is {} years old.".format(name.title(), ages[name]))
    else:
        print("{} is not applied on the age list".format(name.title()))

# yes
mainloop = True

# EPIC MAIN
def main():

    # yes
    while mainloop == True:
        guide()
        decision = input("What would you like to do?")

        # if name list
        if decision == '1':
            name_list()

        # but what if age check
        elif decision == '2':
            age_check()

        # but what if not
        elif decision == '3':
            mainloop == False
            exit()
            
        # but they didn't type the correct
        else:
            print("NOT AN OPTION")

# forever
main()
