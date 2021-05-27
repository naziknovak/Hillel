txt = "the first letter is capital"
x = txt.capitalize()
print(x)

txt = "The first letter in lower case"
x = txt.casefold()
print(x)

txt = "The text is displayed in the center"
x = txt.center(50)
print(x)

txt = "There are _ letters 't' in this string"
x = txt.count("t")
print(f"There are {x} letters 't' in this string")

txt = "It doesn't interpret special symbols like á and ñ"
x = txt.encode()
print(x)

txt = "Hello, world!"
x = txt.endswith("!")
print(f"'{txt}' ends with '!':", x)

txt = "\tIt \texpands \tthe \ttabs"
x = txt.expandtabs()
print(x)

txt = "Hello, world!"
x = txt.find(",")
print(f"The symbol ',' starts at {x} position")

name = "Nazar"
city = "Kyiv"
txt = f"My name is {name}, I live in {city}"
print(txt)

point = {'x': 4, 'y': -5, 'z': 0}
print("The list of numbers is:", '{x}, {y} and {z}'.format_map(point))

txt = "Hello, world!"
x = txt.index("world")
print(f"The word 'world' starts at {x} position")

txt = "This string contains only alphanumeric symbols"
x = txt.isalnum()
print(txt, ":", x)

txt = "world"
x = txt.isalpha()
print(f"The word '{txt}' contains only alphabet letters:", x)

txt = "12345"
x = txt.isdecimal()
print(f"The string '{txt}' contains only decimal numbers:", x)

txt = "12345"
x = txt.isdigit()
print(f"The string '{txt}' contains only digits:", x)

txt = "world"
x = txt.isidentifier()
print(f"The string '{txt}' is a valid identifier:", x)

txt = "All symbols in this string are in lower case"
x = txt.islower()
print(txt, ":", x)

txt = "1²345"
x = txt.isnumeric()
print(f"All the characters in '{txt}' are numeric :", x)

txt = "1(23*4)5"
x = txt.isprintable()
print(f"All the characters in '{txt}' are printable :", x)

txt = "All the characters in this text are whitespaces"
x = txt.isspace()
print(txt, ":", x)

txt = "Each Word In This String Start With An Upper Case Letter"
x = txt.istitle()
print(txt, ":", x)

txt = "All the characters in the text are in upper case"
x = txt.isupper()
print(txt, ":", x)

txt = ("apple", "banana", "pineapple")
x = ", ".join(txt)
print("This method joins words in one string:", x)

txt = "This method"
x = txt.ljust(20)
print(x, "leaves a justified version of the word/string")

txt = "This ONE converts a string INTO lower case"
x = txt.lower()
print(x)

txt = "version   "
x = txt.lstrip()
print("Returns a left trim", x, "of the string")

txt = "Let's translate letter 't' into upper case"
trans = txt.maketrans("t", "T")
print(txt.translate(trans))

txt = "It splits this sentence into 3 parts"
x = txt.partition("this sentence")
print(x)

txt = "It replaces apples"
x = txt.replace("apples", "pineapples")
print(x)

txt = "The position of 'word' in this text is"
x = txt.rfind("word")
print(txt, ":", x)

txt = "The position of 'word' in this text is"
x = txt.rindex("word")
print(txt, ":", x)

txt = "This method"
x = txt.rjust(20)
print(x, "leaves a justified version of the word/string")

txt = "It splits this sentence into 3 parts"
x = txt.rpartition("this sentence")
print(x)

txt = "It splits every word"
x = txt.rsplit(" ")
print(x)

txt = "It removes any trailing characters.,.,.,."
x = txt.rstrip(".,")
print(x)

txt = "It,splits,every,word"
x = txt.split(",")
print(x)

txt = "It splits a string into a list\nwhere each line is a list item"
x = txt.splitlines()
print(x)

txt = "¡Hello, world!"
x = txt.startswith("¡")
print(f"'{txt}' starts with '¡':", x)

txt = "It removes any trailing characters))))"
x = txt.strip(")")
print(x)

txt = "mAKE the lower case letters upper case AND VICE VERSA"
x = txt.swapcase()
print(x)

txt = "Make the first letter in each word upper case"
x = txt.title()
print(x)

txt = "Let's translate letter 't' into upper case"
x = {116:  84}
print(txt.translate(x))

txt = "Upper case the string"
x = txt.upper()
print(x)

txt = "Fills the string with zeroes"
x = txt.zfill(40)
print(x)

