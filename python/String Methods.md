# String Methods
## `lower()` Method
- The `lower()` method returns the lower-case version of a string.
```python
# lower() Example
print(my_dna.lower())

# Answer
atgcac
```

## `upper()` Method
- The `upper()` method returns the upper-case version of a string.
```python
# upper() Example
print(my_dna.upper())

# Answer
ATGCAC
```

## `isupper()` Method
- The `isupper()` method will return a Boolean `True` value if the string letters are all uppercase.
```python
# isupper() Method
var = 'Hello World!'
print(var.isupper())

# Answer 
False
```

## `islower()` Method
- The `islower()` method will return a Boolean `True` value if the string letters are all lower-case.
```python
# islower() Method
var = 'boo!'
print(var.islower())

# Answer 
True
```

## `isX()` Methods
- The `isalph()` method returns `True` if the string consists only of letters and is not blank.
- The `isalnum()` method returns `True` if the string consists only of letters and numbers and is not blank.
- The `isdecimal()` method returns `True` if the string consists only of numeric characters and is not blank.
- The `isspace()` method returns `True` if the string consists only of spaces, tabs, and new-lines and is not blank.
- The `istitle()` method returns `True` if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.

## `capitalize()` Method
- The `capitalize()` method returns a string with first char in upper-case and there rest in lower-case.
```python
# capitalize() Example
print(name.capitalize())

#Answer
Hello world
```

## `startswith()` Method
- The `startswith()` method returns `True` if the string value called on begins with the string passed to the method.
```python
# startswith() Example
print('Hello world!'.startswith('Hello'))

# Answer
True
```

## `endswith()` Method
- The `endswith()` method returns `True` if the string value called on ends with the string passed to the method.
```python
# startswith() Example
print('Hello world!'.endswith('world!'))

# Answer
True
```
## `count()` Method
- The `count()` string method returns the number of non-overlapping occurences of substring.
```python
# count() Example 1
text = 'babababa'
i = text.count('baba')
print(i)

# Answer
2
```
- The `count()` string method has a start and end arguments.
```python
# count() Example 2
text = 'babababa'
i = text.count('baba,1,6')
print(i)

# Answer
1
```

## `find()` Method
- The `find()` string method returns the index of the first occurrence of a substring.
- You can specify starting and ending index of the search
  - If the substring is not found, `find()` returns `-1`
```python
# find() Example
text = 'foo bar foo'
x = text.find('bar')
y = text.find('bar', 5)
z = text.find('bar', 0, 5)
print(x)
print(y)
print(z)

# Answer
4
-1
-1
```

## `replace()`  Method
- The `replace()` method replaces the occurences of one substring by the other
- If the optional argument `value` in `replace()` is given, only the first `value` occurrences are replaced.
```python
# replace() Example
text = '11223451'
print(text.replace('1', 'One'))
print(text.replace('1', 'One', 2))

# Answer
OneOne22345One
OneOne223451
```

## `strip()`, `rstrip()`, and `lstrip()`
- The `strip()` string methods will return a new string without any whitespace characters at the beginning or end.
- A string argument can be used to specify which characters on the ends should be stripped.
- The order of the characters in the string passed to `strip()` does not matter.

## `split()` Method
- The `split()` string method is called on a string value and returns a `list` of strings.
  - It uses all white space (space, tab, or newline characters) as a separator by default.
```python
# split() Example
print('My name is Simon'.split())
text = 'goodbye cruel world     '
words = text.split()
print(words)
print (type(words))

# Answer
['My', 'name', 'is', 'Simon']
['goodbye', 'cruel', 'world']
<class 'list'>
```
- The `split()` method can be passed a delimiter string to specify a different string to split.
  - A common use of `split()` is to split a multiline string along the newline characters (`\n`).
```python
# split() Example
multiline_var = '''line 1,
line 2.
line 3
line "4":'''
print(multiline_var.split('\n'))

# Answer
['line 1,', 'line 2.', 'line 3', 'line "4":']
```
- Second argument of the `split()` method is `maxsplit`, that specifies a number of splits. 
- If `maxsplit` is given, at most `maxsplit` splits are done (thus, the list will have at most `maxsplit+1` elements)
```python
# split() Example
text = 'a b c    d'
words = text.split(None, 2)
print(words)

# Answer
['a', 'b', 'c    d']
```
- When there are consequtive separators, the `split()` method interprets them as *separating empty strings*.
```python
# split() Example
text = 'abba'
words = text.split('b')
print(words)

# Answer
['a', '', 'a']
```

## `rsplit()` Method
- The string `rsplit()` method splits the string **from the right side**. First argument is a separator, second is a number of splits.
```python
# rsplit() Example
text = 'aa bb cc'
x = text.rsplit(None, 1)
print(x)

# Answer
['aa bb', 'cc']
```

## `join()` Method
- The `join()` string method joins a list of strings into a single string value.
```python
# join() Example
print(', '.join(['casts','rats','bats']))
print(' '.join(['My', 'name', 'is', 'Simon']))
print('ABC'.join(['My', 'name', 'is', 'Simon']))

# Answer
casts, rats, bats
My name is Simon
MyABCnameABCisABCSimon

# join() Example 2
text = 'abcabcabcabc'
y = ''.join([char for char in text if char != 'a'])
print(y)

# Answer
bcbcbcbc
```

## `format()` Method
- The `fomat()` method will input its method call argument into the string's curly brackets (`{}`).
```python
# format() Example
x = 'hello {}'.format('world')
print(x)

# Answer
hello world
```
- *Double* curly braces are used to scape curly braces.
```python
# format() Example
x = 'hello {{}}'.format('world')
print(x)

# Answer
hello {}

# format() Example 2
x = 'hello {{{}}}'.format('world')
print(x)

# Answer
hello {world}
```
- Use numbers to specify where to put the variables.
- Not all the arguments have to be used
- Arguments can be reused.
```python
# format() Example
s1 = "{0} is better than {1}".format("emacs", "vim")
s2 = "{1} is better than {0}".format("emacs", "vim")
s3 = "{0} is better than {0}".format("emacs", "vim")
s4 = "{1} is better than {1}".format("emacs", "vim")
print(s1)
print(s2)
print(s3)
print(s4)

# Answer
emacs is better than vim
vim is better than emacs
emacs is better than emacs
vim is better than vim
```
- Name arguments can be used to specify where to put the variables.
```python
# format() Example
x = " I {verb} the {object} off the {place} "\
    .format(verb="took", object="cheese", place="table")
print(x)

# Answer
I took the cheese off the table 
```

## `rjust()`, `ljust()`, and `center()` Method
- The `rjust()`, `ljust()`, and `center()` string methods pads a string to a specified length, with spaces by default.
```python
# rjust() Example
strs = ['a', 'an', 'cat', 'door', 'hello']
for i in strs:
    print(i.rjust(4))

# Answer
   a
  an
 cat
door
hello
```
- The second arg speficies the pad character (space by default)
```python
# center() Example
strs = ['a', 'an', 'cat', 'door', 'hello']
for i in strs:
    print(i.center(6, '_'))

# Answer
__a___
__an__
_cat__
_door_
hello_
```
```python
# rjust(), ljust(), and center() Example
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
        
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

# Answer
---PICNIC ITEMS--
sandwiches..    4
apples......   12
cups........    4
cookies..... 8000
-------PICNIC ITEMS-------
sandwiches..........     4
apples..............    12
cups................     4
cookies.............  8000
```