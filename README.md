### Strings in Python 


# Creating a string in python

Strings in python can be created in three ways.
+ Single Quote,
 Ex: 'i am a single quote string'( used to create single line string, but nnot preferred because another string inside this string cannot be created, if done so compiler gets confused and dont know where to start and returns a compiler error.
+ Double quotes,
 Ex1: "i am adouble quotes string"
Ex2: "i am double quotes string. 'and i am a sub string inside double quote string' End of double quote string "

(Most preferred because sub string can also be created inside this string with the help of singl quotes)
+ Three quotes ( used to create multi line string )

Ex: ''' i am multi
     line 
    string'''


# string indexing

likewise in list, string also have index at each of its character. In python string idnexing start with 0.

 Ex: Lets take a string

string = "crypto aimdy"

accesing index by positive indexing

indexing =  c r y p t o   a i m  d  y
            0 1 2 3 4 5 6 7 8 9 10 11

accesing index by negative indexing

indexing =  c   r   y   p   t   o       a   i  m  d  y
          -12 -11 -10  -9  -8  -7  -6  -5  -4 -3 -2 -1

#slicing and reversing a  string

we can also slice string string from whatever indexes we want with the help of colon(:).

With slices, we can call multiple character values by creating a range of index numbers separated by a colon [x:y]
we can also reverse a string using slice.

Ex: prints char at position 4 all the way upto char at position 5 but leaving the character 5.
print(s[4:5])
prints the character 'c'


You can also use negative index numbers to slice a string.
Ex: print(s[:-8])
prints 'cryp'

#length of string

we can also find the length of a string using leg(string)

ex: print(len("crypto"))
prints:  6

#string concatenatiion and multiplication

#Concatenation:
There are a few ways of doing this, depending on what you’re trying to achieve. The simplest and most common method is to use the plus symbol (+) to add multiple strings together. Simply place a + between as many strings as you want to join together:

EXample:'a' + 'b' + 'c'
prints:   'abc'

Remember, strings are immutable! If you concatenate or repeat a string stored in a variable, you will have to assign the new string to another variable in order to keep it.

Ex: original_string = "hello"
    original_string + "world"
print(original_string) prints only hello

so we have to store it into new variable
# lets store concatenated string into a new variable.
new_string = original_string + "world"

print(new_string) prints helloworld.

#Going From a List to a String in Python With .join()
There is another, more powerful, way to join strings together. You can go from a list to a string in Python with the join() method.
Example:

list_of_strings = ['a','b','c']
','.join(list_of_strings)

prints: 'a,b,c'

#multiplication
strings can multiply using a * operator

Ex:        print('do' * 2)
prints : 'dodo'

#splitting strings
in python strings can be splitted using split() method. this method returns string after splitting into the specified break points.

Syntax :

str.split(separator, maxsplit)
#ttile in strig
synteax:

str.Title()
This function returns a string which 
has first letter in each word is uppercase and all 
remaining letters are lowercase. 


name = "crypto"
print(str.title(name))
returns foirst letter uppercase


#uppercase and lowercase.
print(str.upper(name)), returns all uppercase
print(str.lower(name)), returns all lower case.

str.capitalize()

converts first character of a string into upper case.

#Python Strip

strip()
used to remove all the lead and trail spaces from a string
syntax:

string.strip([remove])


#count()
count method returns the number of substring repeated in the string

string.count(substring, start=..., end=...)

#find()
thihs method returns index position of a string if found els eit returns -1.
syntax:
str.find(sub[, start[, end]] )

#swapcase
The string swapcase() method converts all uppercase characters to lowercase and all lowercase characters to uppercase characters of the given string, and returns it.
syntax:
string.swapcase()

#replace
replace() is an inbuilt function in Python programming language that returns a copy of the string where all occurrences of a substring is replaced with another substring.

Syntax :

string.replace(old, new, count)

#sorted()
sorted method is used to sort characters of string into order

syntax: 
sorted(iterable, key=key, reverse=reverse)
 






