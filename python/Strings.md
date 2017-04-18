# Strings

## Escape Characters
- An *escape character* lets you use characters that are otherwise impossible to put into a string.
- An escape character consists of a backslash (`\`) followed by the character you want to add to the string.

### Table of Exape Characters
| Escape Character | Prints as |
|------------------|-----------|
| \' | Single Quote |
| \" | Double Quote |
| \t | Tab |
| \n | Newline (line break) |
| \\ | Backslash |

## Raw Strings
- You can place an `r` before the beginning quotation mark of a string to make it a raw string.
- A *raw string* completely ignores all escape characters and prints any backslash that appears in the string.

## Multiline Strings with Triple Quotes
- A *Multiline* string in Python begins and ends with either three single quotes or three double quotes.
- An quotes, tabs, or newlines in between the `triple quotes` are considered part of the string.
- Python's indentation rules for blocks do not apply to lines inside a multiline string.

## Indexing and Slicing Strings
- Strings use indexes and slices the same way lists do.
- Slicing a string does not modify the original string.
- Strings are immutable.
```python
# String Basics Example
a = 'hello'
a[1] = 'E'

# Answer
TypeError: 'str' object does not support item assignment
```
- You can capture a slice from one variable in a separate variable.
- Three indices separated by a colon `[start:end:step]`.
- An omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.
- Indices may be negative numbers usually used to start counting from the right. 
- **Note** that `-0` is really the same as `0`, so it does not count from the right. 
- The last character of a string has index `-1`.
```python
# String Slice Notation Example
t = 'AaBbCcDd'
print(t[::2])
print(t[1::2])

# Answer
ABCD
abcd
```

## The in and not in Operators with Strings
- The `in` and `not in` operators can be used with strings just like with list values.
- An expression with two strings joined using `in` or `not in` will evaluate to a Boolean `True` or `False`.

## String Concatenation
- adjacent strings are concatenated, so `'a'` `'b'*2` is similar to `'ab'*2`
```python
# String Basics Example
print('a' 'b'*2)

# Answer
abab
```