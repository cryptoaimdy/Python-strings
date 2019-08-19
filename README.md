# Strings in Python 


## Creating a string in python

Strings in python can be created in three ways.
+ Single Quote,

      Example: 'i am a single quote string' 
 
 Single Quote is used to create single line string, but not preferred because another string inside this string cannot be created, if done so compiler gets confused and dont know where to start and returns a compiler error.)
 
+ Double quotes,

       Ex1: "i am a double quotes string"

       Ex2: "i am double quotes string, 'and i am a sub string inside double quote string' End of double quote string"

(Double Quoto strings are Most preferred because sub string can also be created inside this string with the help of single quotes)

+ Three quotes ( used to create multi line string )

         Ex: '''i am multi
         
                 line
                 
                 string'''


## String Indexing:

Likewise in list, strings also have index at each of its character. In python string idnexing start with 0.

Ex: Lets take a string

         string = "crypto aimdy"

+ Accesing index by positive indexing

        indexing =  c r y p t o   a i m  d  y
                    0 1 2 3 4 5 6 7 8 9 10 11

+ Accesing index by negative indexing

       indexing =  c   r   y   p   t   o       a   i  m  d  y
                 -12 -11 -10  -9  -8  -7  -6  -5  -4 -3 -2 -1

### Slicing and reversing a String:

+ We can also slice string string from whatever indexes we want with the help of colon(:).

+ With slices, we can call multiple character values by creating a range of index numbers separated by a colon [x:y]
we can also reverse a string using slice.

Example : prints char at position 4 all the way upto char at position 5 but leaving the character 5.

      print(s[4:5])

      prints the character 't'


You can also use negative index numbers to slice a string.

Ex:           
    
    print(s[:-8])

    prints 'cryp'

### Length of String:

We can also find the length of a string using len(string)

Ex: 
     
      print(len("crypto"))'''

      prints:  6

## String Concatenatiion and Multiplication

### Concatenation:

There are a few ways of doing this, depending on what you’re trying to achieve. The simplest and most common method is to use the plus symbol (+) to add multiple strings together. Simply place a + between as many strings as you want to join together:

Example:

      'a' + 'b' + 'c'
       prints:   'abc'
   
***Remember, strings are immutable! If you concatenate or repeat a string stored in a variable, you will have to assign the new string to another variable in order to keep it.

Example: 

    original_string = "hello"

    original_string + "world"
    
print(original_string) prints only hello

So we have to store it into new variable

+ lets store concatenated string into a new variable.

      new_string = original_string + "world"

      print(new_string) prints helloworld.

### Going From a List to a String in Python With .join()
There is another, more powerful, way to join strings together. You can go from a list to a string in Python with the join() method.

Example:

     list_of_strings = ['a','b','c']

     ','.join(list_of_strings)

     prints: 'a,b,c'

### Multiplication

Strings can multiply using a * operator

Ex:         

       print('do' * 2)

       prints : 'dodo'

### Splitting strings
In python strings can be splitted using split() method. this method returns string after splitting into the specified break points.

     Syntax : str.split(separator, maxsplit) ***



### Str.Title()
This function returns a string which has first letter in each word is uppercase and all remaining letters are lowercase. 

    name = "crypto"

    print(str.title(name))

    returns first letter uppercase


### Uppercase and lowercase.

     print(str.upper(name)), #returns all uppercase***

     print(str.lower(name)), #returns all lower case.

     str.capitalize()        #converts first character of a string into upper case.

### Python Strip

+ Used to remove all the lead and trail spaces from a string

      Syntax: string.strip([remove])


### Count():

Count method returns the number of substring repeated in the string

     Syntax: tring.count(substring, start=..., end=...)

### Find()
This method returns index position of a string if found els eit returns -1.

     Syntax: str.find(sub[, start[, end]] )

# Swapcase():

The string swapcase() method converts all uppercase characters to lowercase and all lowercase characters to uppercase characters of the given string, and returns it.

      Syntax: string.swapcase()

### Replace():

Replace() is an inbuilt function in Python programming language that returns a copy of the string where all occurrences of a substring is replaced with another substring.

      Syntax : string.replace(old, new, count)

# Sorted():

Sorted method is used to sort characters of string into order

    Syntax:  sorted(iterable, key=key, reverse=reverse)
 
