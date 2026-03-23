class Library:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.available = True

    def show(self):
        if self.available:
            status = "Available"
        else:
            status = "Not Available"

        print("Book:", self.name)
        print("Author:", self.author)
        print("Status:", status)
        print()

    def checkout(self):
        if self.available:
            self.available = False
            print(self.name, "checked out")
        else:
            print(self.name, "already taken")

    def return_book(self):
        self.available = True
        print(self.name, "returned")


# Main program
b1 = Library("Python Programming", "Guido van Rossum")

b1.show()
b1.checkout()
b1.show()
b1.return_book()
b1.show()