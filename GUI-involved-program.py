#CREATION OF GUI
from tkinter import *
#Create the main window that will be appear on the screen 
file = Tk()
file.geometry("325x300")
file.configure(bg="#F1F6F5")
file.title("My Diary")

#Create the header and labels that instructs the user what to enter
#HEADER
heading = Label(text="Dear Diary...", fg="#176D81", bg="#F1F6F5", width="450",height="1", font=("courier new", 20, "bold"))
heading.pack(padx=5, pady=(5, 20))
#LABELS
entry_date_text = Label(text="Entry Date:", fg="teal", bg="#F1F6F5", font=("courier new", 14, "bold"))
entry_date_text.place(x=10, y=55)
entry_text_label = Label(text="How was your day?", fg="teal", bg="#F1F6F5", font=("courier new", 14, "bold"))
entry_text_label.place(x=10, y=105)

#Create text box where the user will input their entry
entry_date_input = Entry(width="48")
entry_date_input.place(x=10,y=80, width=301, height=25)
entry_text_input = Entry(width="48")
entry_text_input.place(x=10,y=130, width=301, height=25)

#Create necessary buttons
button = Button(file,text="Submit", command=save_entries, width="32", height="1", bg="#71ADB5", fg="white", font=("courier new", 11, "bold"))
button.place(x=11, y=185)

button = Button(file,text="I want to write more", command=try_again, width="32", height="1", bg="#176D81", fg="white", font=("courier new", 11, "bold"))
button.place(x=11, y=220)

button = Button(file,text="Quit", command=close, width="32", height="1", bg="#0D3446", fg="white", font=("courier new", 11, "bold"))
button.place(x=11, y=255)

mainloop()
#CREATION OF COMMANDS FOR THE BUTTONS TO FOLLOW
#Ask user to input their entry in the 
#1st COMMAND: Get the entries inputted by the user
#Open a text file and name it "mylife.txt"
#Append/write the input text to mylife.txt file
#Link commands to the buttons
#2nd COMMAND: Deletes the previous entry of the user from the text box in order to enter new line of texts
#3rd COMMAND: Quits and Exits the GUI Window