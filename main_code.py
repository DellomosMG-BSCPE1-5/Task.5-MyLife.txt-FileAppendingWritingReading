#Write a method in python to write multiple line of text contents
#into a text file mylife.txt

while True:
    #HEADER 
    import pyfiglet
    from colorama import Fore, Back, Style
    print(Fore.BLUE + pyfiglet.figlet_format("  My Life   ", font = "xsansb", width=500))

    #Define a function
    def entry_writing():
        #Open a text file named mylife.txt (append)
        with open("mylife.txt", "a") as main_file:
            #Ask user for a line text input
            print(Fore.BLUE + Style.BRIGHT + "✨ Date: " + Fore.LIGHTCYAN_EX + Style.NORMAL,  end = "")
            date_of_entry = input(Fore.WHITE + "")
            print(Fore.BLUE + Style.BRIGHT + "\n✨ Your Entry: " + Fore.LIGHTCYAN_EX + Style.NORMAL,  end = "")
            entry = input(Fore.WHITE + "")
            #Append/write the input text to mylife.txt file
            main_file.write((str(date_of_entry) + "\n" + str(entry) + "\n\n"))            

    entry_writing() 

    #Ask the user if he/she wants to enter text again
    check = input(Fore.YELLOW + "\nDo you want to add an entry again? Yes or No? ") 
    if check.upper() == "Y" or check == "yes" or check == "YES" or check == "Yes":  
        continue
    break
