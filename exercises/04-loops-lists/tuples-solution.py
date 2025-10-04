# Coding exercises using Tuples
"""
You're organizing books in a library.

The books: 
1. "1984", George Orwell, 1949
2. "Pride and Prejudice", Jane Austen, 1813
3. "To Kill a Mockingbird", Harper Lee, 1960
4. "The Murder of Roger Ackroyd", Agatha Christie, 1926
5. "11/22/63", Stephen King, 2011

Tasks
1. Create 3 book tuples with (title, author, year).
2. Print all the books in the format: 1984, by George Orwell (1949)

# Hint:
# this is a tuple containing the name of the book, the author, and the publication year
book1 = ("1984", "George Orwell", 1949) 
"""

# 1. Create 3 book tuples with (title, author, year)
book1 = ("1984", "George Orwell", 1949)
book2 = ("Pride and Prejudice", "Jane Austen", 1813)
book3 = ("To Kill a Mockingbird", "Harper Lee", 1960)
book4 = ("The Murder of Roger Ackroyd", "Agatha Christie", 1926)
book5 = ("11/22/63", "Stephen King", 2011)

# Put the books in a list
books = [book1, book2, book3, book4, book5]

# 2. Print all the books in the requested format using f-strings
for book in books:
    title = book[0]
    author = book[1]
    year = book[2]
    print(f"{title}, by {author} ({year})")

# Alternate solution
# 2. Print all the books in the requested format using string concatenation
for book in books:
    title = book[0]
    author = book[1]
    year = book[2]
    print(title + ", by " + author + " (" + str(year) + ")")
