from tkinter import *  # Bringing in the magic of GUI with tkinter
import random  # Let's sprinkle some randomness into our project

def generate_quote():  # A function to generate a new insightful quote
    # Selecting a random quote from the list and displaying it
    another_quote_text = random.choice(quotes).strip()  
    quotes_label.config(text=another_quote_text)  

app = Tk()  # Creating the tkinter application window
app.title("Random Quote Generator")  # Setting the title of our awesome app
app.geometry("400x310")  # Defining the dimensions of the window
app.config(padx=10, pady=10)  # Adding some padding for aesthetics

app_title = Label(app, text="Random Quote Generator", font=("nectar bold", 15))  # Displaying the title of our app
app_title.pack()  # Packing it nicely into the window

underline_label = Label(app, text="___________________________________", font=("nectar regular", 12))  # Adding an underline for style
underline_label.pack()  # Making sure it fits nicely

with open("quotes.txt", 'r') as data:  # Opening our file of wisdom
    quotes = data.readlines()  # Reading all the quotes into a list

quote_text = random.choice(quotes).strip()  # Selecting a random quote to start with

quotes_label = Label(app, text=quote_text, font=("nectar bold", 13, 'bold'), wraplength=380)  # Displaying the initial quote
quotes_label.pack()  # Packing it into the window with care

generate_button = Button(text="Generate Another Quote", font=('aria', 13), borderwidth=2, relief=GROOVE, command=generate_quote)  # Creating a button to generate new quotes
generate_button.pack(pady=55)  # Giving it some space to breathe

developer_information = Label(app, text='Made by Ilia keshavarz', font=("nectar bold", 11))  # Giving credit where it's due
developer_information.pack()  # Making sure it's visible

app.mainloop()  # Letting tkinter do its magic and run the app
