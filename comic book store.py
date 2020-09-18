from tkinter import *
from tkinter import ttk

#----------- Tkinter coding root
root = Tk()
root.title("Comic Book Store")
root.geometry("525x600") # the size of the window

#----------- Class code for Books
class Book:
    """The Book class stores the details of each book in the comic book store and has methods of purchasing, restocking and viewing details"""
    def __init__(self, title, amount, sold):
        self.title = title
        self.amount = amount
        self.sold = sold
        book_list.append(self)

    # Purchasing book - subtracts 1 book from book amount
    def sell(self):
        if self.amount > 0:
            self.amount -= 1
            self.sold += 1
            return True
        else:
            return False

    # Restocking book - adds number to book amount
    def restock(self, number):
        if number > 0:
            self.amount += number
            return True
        else:
            return False

#----------- Functions
# Update restock - updates the amount of available books
# Create function to get book names list
def book_names_list():
    name_list = []
    for book in book_list:
        name_list.append(book.title)
    return name_list

# Create function that manages book purchase details
def purchase_book():
    for book in book_list:
        if selected_book.get() == book.title:
            book.sell()
            if book.amount > 0:
                action_feedback.set("A book copy of {} was successfully sold! ".format(book.title))
            elif book.amount == 0:
                action_feedback.set("No more copies of {} available in stock. ".format(book.title))
        # Update the GUI
        update_total_sold()
        number.set("")

        message_text.set(sell_message)

# Update restock - updates the amount of books that have been restocked
# (Create function that manages book restock details)
def restock_book():
    for book in book_list:
        if selected_book.get() == book.title:
            if book.restock(number.get()):
                action_feedback.set("Total of {} was successfully restocked into {}! ".format(number.get(), book.title))
                message_text.set(restock_message)
            else:
                action_feedback.set(error_message)
                message_text.set("")
            #Update the GUI
            update_restock()
            number.set("")

# Update sold - updates the total amount of sold books
def update_total_sold():
    total_sold = 0
    book_details_string = ""
    amount_string = ""
    # Add each book amount to the 'total books sold:' label
    for book in book_list:
        book_details_string += "{}: {}\n".format(book.title, book.amount)
        total_sold += book.sold
    amount_string += "\nTotal Books Sold: {}".format(total_sold)
    sold_details.set(amount_string)
    book_details.set(book_details_string)

# Create function that restocks the book
def update_restock():
    book_details_string = ""
    # Update restocked book amount
    for book in book_list:
        book_details_string += "{}: {}\n".format(book.title, book.amount)
    book_details.set(book_details_string)
        
#----------- Set ups
book_list = []
restock_message = ("Restock complete! ")
sell_message = ("Purchase complete! ")
error_message = ("Error! please enter a valid amount! ")

# instances of the class
Comic_1 = Book("Super Dude", 8, 0)
Comic_2 = Book("Lizard Man", 12, 0)
Comic_3 = Book("Water Woman", 3, 0)

# name list command
book_names = book_names_list()




#----------- Top frame / welcome_container LabelFrame
# Welcome frame / 'Comic Book Store' LabelFrame
welcome_container = ttk.LabelFrame(root, text="Comic Book Store", padding=20)
welcome_container.grid(column=0, row=0, sticky="WE", padx=100, pady=10)
welcome_text = StringVar()
welcome_text.set("""Welcome to the Comic Book Store!

Here is the list of our books in store and the total amount of books sold: """)
welcome_label = ttk.Label(welcome_container, textvariable=welcome_text, wraplength=200)
welcome_label.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

# Book details
book_details = StringVar()
book_details_string = ""
for book in book_list:
    book_details_string += "{}: {}\n".format(book.title, book.amount)
book_details.set(book_details_string)
book_details_label = ttk.Label(welcome_container, textvariable=book_details, wraplength=200)
book_details_label.grid(column=0, row=1, padx=10, pady=10)

# Number of books sold
sold_details = StringVar()
total_sold = 0
amount_string = ""
amount_string += "\nTotal Books Sold: {}".format(total_sold)
sold_details.set(amount_string)
sold_details_label = ttk.Label(welcome_container, textvariable=sold_details, wraplength=200)
sold_details_label.grid(column=1, row=1, padx=10, pady=10)


#----------- Bottom frame / option_container LabelFrame
# Option frame
option_container = ttk.LabelFrame(root, text="User Options", padding=20)
option_container.grid(column=0, row=1, sticky="WE", padx=100, pady=10)
option_text = ttk.Label(option_container, text="Please select a book and option.")
option_text.grid(column=0, row=0, padx=10, pady=10)

# Select book
selected_book = StringVar()
selected_book.set(book_names[0])
books_combobox = ttk.Combobox(option_container, textvariable=selected_book, state="readonly")
books_combobox['values'] = book_names
books_combobox.grid(column=0, row=2, padx=5, pady=5, sticky="WE")

# Store the number
number = IntVar()
number.set("")

# Option entry/type number
option_entry = ttk.Entry(option_container, textvariable=number, state="normal")
option_entry.grid(column=0, row=3, padx=5, pady=5, sticky="WE")

# Purchase button
confirmation_button = ttk.Button(option_container, text="Purchase", command=purchase_book)
confirmation_button.grid(column=1, row=2, columnspan=1, padx=10, pady=10)

# Restock button
confirmation_button = ttk.Button(option_container, text="Restock", command=restock_book)
confirmation_button.grid(column=1, row=3, columnspan=1, padx=10, pady=10)

# Action Feedback Label
action_feedback = StringVar()
action_feedback_label = ttk.Label(option_container, textvariable=action_feedback, wraplength=250)
action_feedback_label.grid(column=0, row=4, columnspan=2, padx=5, pady=5)


# Message Label
message_text = StringVar()
message_text_label = ttk.Label(option_container, textvariable=message_text, wraplength=200)
message_text_label.grid(column=0, row=5, columnspan=2, padx=5, pady=5)

#----------- Main loop for root tkinter code
# Mainloop
root.mainloop()
