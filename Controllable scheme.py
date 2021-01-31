import TurtleCells


#Welcoming of the user in the program
print("Welcome to the controllable immune system scheme drawer!")
print("Type 'help' for a quick list of commands", end = "\n\n")


#Initializing the program for real
while True:
    x = input("Awaiting input: ")

    if x == "help" or x == "Help":
        print("This is the help session")
        print()
    elif x == "Exit" or x == "exit":
        print("Exiting the program")
        break
    else:
        print("Command typed appeared to be inexistent or unknown")


#Ending and goodbying from the program
print()
print("-- Thank you for using my sofware --")
print("$Coded by John Baxter")
print("_CONTACTS_________________")
print("|Email: syumjoba@gmail.com")
print("|Instagram: @syumjoba")
print("|_________________________")
print()
print("FOR CONTRIBUTION____________________________________________________")
print("|Project hosted on github: https://github.com/SYUMJOBA/PE-class-work")
print("____________________________________________________________________")
print()
input("Press ENTER to exit the program")