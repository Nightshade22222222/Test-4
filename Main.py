class book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        print("Title of the book is: ", self.title)
        print("Author is: ", self.author)
author = ("Jane Austen")
title  = ("Pride and Prejudice")
b = book()
b.title()
b.author()