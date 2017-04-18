# Lists

## List Basics

- List indexes begin with 0
- List are mutable
- A *list* is a value that contains multiple values in an ordered sequence.
- The term *list value* refers to the list itself, not the values inside the list value.
- A list begins With an opening square brackets and ends with a closing square bracket, `[]`.
- Values inside the list are also called *items*
  - *Items* are separated with commas.
- The value inside the square brackets that follows the list is called an *index*.
- A slice is typed between square brackets, like an index, but it has two integers separated by a colon (`[3:6]`).
- A list can be concatenated by using the `+` operator.
- Values can be removed from a list by using the `del` statement.
- A common Python technique is to use `range(len(someList))` with a `for` loop to iterate over the indexes of a list. 

```python
# List Example
list = ["E", "D", "C", "B", "A"]
print(list)
print(list[0])

# Answer
["E", "D", "C", "B", "A"]
E

# List Example 2
list = ["E", "D", "C", "B", "A"]
list[0] = "X"
print(list)

# Answer
['X', 'D', 'C', 'B', 'A']
```
- The proper way to **mutate** a string is to use *slice notation* and *concatenation* to build a **new** string.
- String `join()` method uses the string as a **separator** for a list of strings and returns a string.

## List Slice Notation
- List slice notation: `a[start:end]` # items **start** through **end-1**
- Slice notation `x[1:2] = []` can be used to remove elements from a list
- **Note**: Not to be confused with `x[1] = []` which would replace `1` with an empty list.
  - This would return: `[0, [], 2, 3]`
```python
# List Slice Notation Example
x = [0, 1, 2, 3]
x[1:2] = []
print(x)

# Answer
[0, 2, 3]
```
- **Extended slices are not flexible**. 
- When assigning to an extended slice, the list on the right hand side of the statement must contain the same number of items as the slice it is replacing.
```python
# List Slice Notation Example
x = [0, 1, 2, 3]
x[::2] = []
print(x)

# Answer
ValueError: attempt to assign sequence of size 0 to extended slice of size 2
```
- Modifying the expression with `x[::2] = [],[]` will however return the desired results.
```python
# List Slice Notation Example
x = [0, 1, 2, 3]
x[::2] = [],[]
print(x)

# Answer
[[], 1, [], 3]
```

## List Referencing
- When a list (`[1, 2, 3, 4]`) is assigned to a variable, a list *reference* (`ID: 12345678`) is actually being assigned to the variable.
- List variables (`my_list` and `other_list`) don’t actually contain lists—they contain references to lists. 
  - These references will have ID numbers that Python uses internally.
- Variables will contain references to list values rather than list values themselves. 
  - But for strings and integer values, variables simply contain the string or integer value. 
- Python uses references whenever variables must store values of mutable data types, such as lists or dictionaries. 
  - For values of immutable data types such as strings, integers, or tuples, Python variables will store the value itself.
```python
# List Referencing Example
my_list = [1, 2, 3, 4]
other_list = my_list
```

- The expression `b = a` does not create a new list, but reference `b` to `a`. Thus, changing the content of `b` changes `a` as well.
```python
# List Referencing Example
a = [1, 2]
b = a

print(a is b)
b[0] = 'A'
print(a is b)
print(a, b)

# Answer
True
True
['A', 2] ['A', 2]
```
- The expression `b = a[:]` creates a shallow copy of `a`.
```python
# List Referencing Example
a = [1, 2]
b = a[:]
print(a is b)
print(a, b)

# Answer
False
[1, 2] [1, 2]
```

## List `in` And `not` Operation
- You can determine whether a value is or isn’t in a list with the `in` and `not` in operators.
- The `in` operator checks for membership of **upper level** only
```python
# List in and not Operation Example
a = [1]
b = [0, a]
c = [0, b]

print(a in b)
print(a in c)
print(a in c[1])

# Answer
True
False
True
```
## List Multiple Assignment
- The multiple assignment trick is a shortcut that lets you assign multiple variables with the values in a list in one line of code.
- The number of variables and the length of the list must be exactly equal.
```python
# List Multiple Assignement Example
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
print(size)
print(color)
print(disposition)

# Answer
fat
orange
loud
```
## List Sequence Multiplication
- `List` or `tuple` can be initiated by multiplication.
- Sequence multiplication repeats the references, not the values.
```python
# List Sequence Multiplication Example
x =  [[0]]*3
print(x)

x[2][0] = 1

print(x)
print(x[1] is x[2])

# Answer
[[0], [0], [0]]
[[1], [1], [1]]
True
```