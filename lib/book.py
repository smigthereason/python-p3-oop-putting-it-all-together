#!/usr/bin/env python3

class Book:
    pass

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None  
        self.page_count = page_count  
        
    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


if __name__ == "__main__":
    import io
    import sys

    class TestBook:
        '''Book in book.py'''

        def test_has_title_and_page_count(self):
            '''has the title and page_count passed into __init__, and values can be set to new instance.'''
            book = Book("And Then There Were None", 272)
            assert(book.page_count == 272)
            assert(book.title == "And Then There Were None")

        def test_requires_int_page_count(self):
            '''prints "page_count must be an integer" if page_count is not an integer.'''
            book = Book("And Then There Were None", 272)
            captured_out = io.StringIO()
            sys.stdout = captured_out
            book.page_count = "not an integer"
            sys.stdout = sys.__stdout__
            assert captured_out.getvalue() == "page_count must be an integer\n"

        def test_can_turn_page(self):
            '''outputs "Flipping the page...wow, you read fast!" when method turn_page() is called'''
            book = Book("The World According to Garp", 69)
            captured_out = io.StringIO()
            sys.stdout = captured_out
            book.turn_page()
            sys.stdout = sys.__stdout__
            assert(captured_out.getvalue() == "Flipping the page...wow, you read fast!\n")

    

    
     