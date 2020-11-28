
#####
#Mission started from Codecademy and Tim Bohmert evolved into a book store with multiple Choose Your Own Adventure stories
# 
# Welcome to Wilderness Escape, an online Choose-Your-Own-Adventure. Our users get a unique story experience by picking the next chapter of their adventure. We use the tree data structure to keep track of the different paths a user may choose. Let’s get started!
#####

#####
#USER INTERFACE SCRIPT FOR BOOK SELECTION, TRAVERSING THE STORY, AND EXITING THE STORE
#####


import wildernessEscape

available_books = {'Wilderness Esscape': wildernessEscape, 'exit store': 0}

#helper function that prints the keys alongside their book title
def print_book_names(book_dict):
    book_names = ''
    for i, name in enumerate(book_dict.keys(), 1):
        book_names += '{0}: {1}\n'.format(i, name)
    return book_names


#function that allows user to select their book
def select_book():
    book_choice_idx = int(input('Select the number of the book that you would like to read next:\n{0}'.format(print_book_names(available_books)))) - 1 
    if book_choice_idx < 0 or book_choice_idx >= len(available_books):
        print('Invalid selection')
        select_book()
    return list(available_books.keys())[book_choice_idx]


#intro into the book store
print('Hello and welcome to Biscuit\'s Choose Your Own Adventure Bookstore.!\n')

#code to have user select their book
book_name = select_book()

#while loop that allows user to read multiple books
while book_name != "exit store":

    #accessing book file and execute code to traverse book
    book_file = available_books[book_name]
    book_file.story_root.traverse()

    #code that executes once the book is finished and askes the user if they want to read another book or exit the store 
    print('I hope you enjoyed your book!')
    book_name = select_book()


print('Thanks for coming to Biscuit\'s Choose Your Own Adventure Bookstore and have a great day!')

