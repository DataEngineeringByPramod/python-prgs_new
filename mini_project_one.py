# create a library class
# display book
#     lend book-->(who owns the book if not present)
#     add book
#     return book
# HarryLibrary = Library(listofbooks,library_name)
# dictionary (books-nameof person)
# create a main function 2and run an infinite while loop asking user for their input
class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lenddict = {}

    def displaybooks(self):
        print(f'we have following books in our library:{self.name}')
        for book in self.booklist:
            print(book)

    def lendBook(self, book, user):
        if book not in self.lenddict.keys():
            self.lenddict.update({book: user})
            print('lender-book database has been updated you can take the book now')
        else:
            print(f'book is already being used by {self.lenddict[book]}')

    def addbook(self, book):
        self.booklist.append(book)
        print('book has been added to your booklist')

    def returbbook(self, book):
        self.lenddict.pop(book)


if __name__ == '__main__':
    Pramod = Library(['python', 'c++', 'java', 'rich daddy poor daddy', 'harry potter'
                         , 'data structures', 'algo br clrs'], 'MY LIBRARY')
    while (True):
        print(f'welcome to {Pramod.name} library.enter your choice to continue ')
        print('1.DISPLAY A BOOK')
        print('2.LEND  A BOOK')
        print('3.ADD A BOOK')
        print('4.RETURN A BOOK')
        user_choice = int(input())
        if user_choice == 1:
            Pramod.displaybooks()
        elif user_choice == 2:
            print('enter the book which u want to land')
            book = input()
            user = input('enter your name')
            Pramod.lendBook(book, user)
        elif user_choice == 3:
            print('enter the book which u want to add:')
            book = input()
            Pramod.addbook(book)
        elif user_choice == 4:
            print('enter the book which u want to add:')
            book = input()
            Pramod.returbbook(book)
        else:
            print('not a valid a option')
        print('press q for quit and c to continue')
        user_choice2 = input()
        while user_choice2 != 'c' and user_choice2 != 'q':
            # user_choice2 = input()
            # user_choice2 = ''
            if user_choice2 == 'q':
                exit()
            if user_choice2 == 'c':
                continue
