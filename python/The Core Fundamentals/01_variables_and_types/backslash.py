message = "He said, \"Python is awesome!\"\nIt is very readable."
print(message)

"""1. Line Continuation
Python usually expects a statement to be completed on a single line. If you have a very long line of code, you can use the backslash to break it into multiple lines to improve readability.

Python
# Instead of one long, hard-to-read line
total = item_one + item_two + item_three + item_four + item_five

# You can use a backslash to continue the line:
total = item_one + item_two + item_three + \
        item_four + item_five
Note: In most cases (like inside parentheses (), brackets [], or braces {}), you don't actually need the backslash. Python automatically understands that the code continues until the closing bracket. Using parentheses is generally considered more "idiomatic" (Pythonic) than using \.

2. The Escape Character
The backslash is used to "escape" characters inside a string that would otherwise have a special meaning or be difficult to type.

\n (Newline): Moves the cursor to the next line.

\t (Tab): Adds a horizontal tab.

\' or \": Allows you to include quotes inside a string without ending the string early.

\\: Allows you to print a literal backslash.
"""
