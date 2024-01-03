books = {
    1: ('Test Automation in the Real World', 'Greg Paskal', '$9.99'),
    2: ('Experiences of Test Automation', 'Dorothy Graham and Mark Fewster', '$44.09'),
    3: ('Agile Testing', 'Lisa Crispin and Janet Gregory', '$49.07'),
    4: ('How Google Tests Software', 'James A. Whittaker, Jason Arbon, Jeff Carollo', '$31.67'),
    5: ('Java For Testers', 'Alan Richardson', '$29.99'),
    6: ('Advanced Selenium in Java', 'Paul Watson', '$29.99'),
    7: ('The Cucumber for Java Book', 'Seb Rose', '$34.99'),
    8: ('BDD in Action', 'John Ferguson Smart', '$40.31')
}

testcases = {
    "Filtering by name: 1 letter entered": ("x", [books[2]]),
    "Filtering by first letters of the name": ("exp", [books[2]]),
    "Filtering by letters in the middle of the name": ("for", [books[5], books[7]]),
    "Filtering by last letters of the name": ("book", [books[7]]),
    "Filtering by full name": ("Experiences of Test Automation", [books[2]]),

    "Filtering by author: 1 letter entered": ("y", [books[2], books[3]]),
    "Filtering by first letters of the author": ("Do", [books[2]]),
    "Filtering by letters in the middle of the author": ("tt", [books[4]]),
    "Filtering by last letters of the author": ("llo", [books[4]]),
    "Filtering by full author name": ("Paul Watson", [books[6]]),

    "Filtering by 1 number": ("9", [books[1], books[2], books[3], books[5], books[6], books[7]]),
    "Filtering by value before dot": ("44", [books[2]]),
    "Filtering by value after dot": ("67", [books[4]]),
    "Filtering by full price": ("40.31", [books[8]]),
    "Filtering by full price with $": ("$40.31", [books[8]]),

    "No filter results": ("gsdhsdthbsdfbdfabgs", []),
}