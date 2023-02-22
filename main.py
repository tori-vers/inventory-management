import pickle
import tkinter
from tkinter import tkMessageBox
from BTCInput import *


class Inventory:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

top = tkinter.Tk()
        
def button_display():
    tkMessageBox.showinfo( "1. New Book", new_book())
    
B = tkinter.Button(top, text = "NEW", command = button_display)
B.pack()
top.mainloop()
                   

def new_book():
    
    ''' gathers new book input from user and stores it '''
    
    print("Create new book")
    #data attributes
    
    title = read_text("Enter the book title: ")
    author = read_text("Enter the author name: ")
    genre = read_text("Enter the genre: ")
    
    # instance
    new_book = Inventory(title = title, author = author, genre = genre)
    inventory.append(new_book)
    
def find_book(search_title):
    
    ''' reads in a title and searches inventory '''
    
    search_title = search_title.strip()
    search_title = search_title.lower()
    
    for titles in inventory:
        
        title = titles.title 
        title = title.strip()
        title = title.lower()
        
        if title.startswith(search_title):
            return titles
        
    return None

def display_book():
    
    ''' displays info if book is in inventory '''
    print("Find book")
    search_title = read_text("Book title: ")
    inventory = find_book(search_title)
    
    if inventory != None:
        #book found
        
        print("Title: ", inventory.title)
        print("Author: ", inventory.author)
        print("Genre: ", inventory.genre)

    else:
        print("This book was not found.")
        
def edit_book():
    
    ''' allows user to edit an entry '''
    
    print("Edit book information")
    search_title = read_text("Enter the book title: ")
    titles = find_book(search_title)
    
    if titles != None:
        print("Title: ", titles.title)
        new_title = read_text("Enter new title or type ! to leave unchanged: ")
        if new_title != "!":
            titles.title = new_title
        new_author = read_text("Enter a new author or type ! to leave unchanged: ")
        if new_author != "!":
            titles.author = new_author
        new_genre = read_text("Enter a new genre or type ! to leave unchanged: ")
        if new_genre != "!":
            titles.genre = new_genre
    else:
        print("This book was not found. Sorry!")
        
def save_info(file_name):
    
    ''' saves books to filename using pickle '''
    
    print("Save inventory")
        
    with open(file_name, 'wb') as out_file:
        pickle.dump(inventory, out_file)
            
def load_inventory(file_name):
    ''' loads books from the given filename '''
    global inventory 
    print("Load inventory")
    with open(file_name, 'rb') as input_file:
        inventory = pickle.load(input_file)
    
     
menu = ''' 

 Pocket Library

1. New Book
2. Find Book
3. Edit Book
4: Exit Program

Enter command: 
'''

filename = 'inventory.pickle'

try:
    load_inventory(filename)
except:
    print("Inventory file not found.")
    inventory = []
    
while True:
    command = read_int_ranged(prompt = menu, min_value = 1, max_value = 4)
    if command == 1:
        new_book()
    elif command == 2:
        display_book()
    elif command == 3:
        edit_book()
    elif command == 4:
        save_info(filename)
        break
    
    #new features one arrray