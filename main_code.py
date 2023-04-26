#Write a method in python to write multiple line of text contents
#into a text file mylife.txt

#Define a function 
def entry_writing():
    #Open a text file named mylife.txt (append)
    with open("mylife.txt") as main_file:
        #Ask user for a line text input
        date_of_entry = input("Date of Entry: ")
        entry = input(str("Kindly enter a text: "))
    #Append/write the input text to mylife.txt file
    #Ask the user if he/she wants to enter a line of text again

entry_writing()