#CREATION OF GUI
from tkinter import *
#Create the main window that will be appear on the screen 
file = Tk()
file.geometry("325x300")
file.configure(bg="#F1F6F5")
file.title("My Diary")

mainloop()
#Create the header and labels that instructs the user what to enter
#Create text box where the user will input their entry
#Create necessary buttons

#CREATION OF COMMANDS FOR THE BUTTONS TO FOLLOW
#Ask user to input their entry in the 
#1st COMMAND: Get the entries inputted by the user
#Open a text file and name it "mylife.txt"
#Append/write the input text to mylife.txt file
#Link commands to the buttons
#2nd COMMAND: Deletes the previous entry of the user from the text box in order to enter new line of texts
#3rd COMMAND: Quits and Exits the GUI Window