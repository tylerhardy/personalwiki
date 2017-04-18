# Tulpes
## Tulpe Basics
- Tuples are immutable
- Tuples can be created without parentheses.
```python
# Tuple Basics Example
a = (1, 2)
a[1] = 3

# Answer
TypeError: 'tuple' object does not support item assignment
```
## Tulpe Unpacking
- Tuples can be used in unpacking.
- Tuple unpacking cannot have more than one `*` when unpacking.
```python
# Tulpe Unpacking Example 1
a, b, *c = [1, 2, 3, 4, 5]
print(a, b, c)

# Answer
1 2 [3, 4, 5]

# Tulpe Unpacking Example 2
*a, b, c = [1, 2, 3, 4, 5]
print(a, b, c)

# Answer
[1, 2, 3] 4 5

# Tulpe Unpacking Example 3
a, *b, c = [1, 2, 3, 4, 5]
print(a, b, c)

# Answer
1 [2, 3, 4] 5
```
- You can unpack into the `print()` statement.
```python
# Tulpe Unpacking Example
x = [4, 5, 6, 7]
print(x)
print(*x)

# Answer
[4, 5, 6, 7]
4 5 6 7
```
- Tuple unpacking creates a list
```python
# Tuple Unpacking Example
x, *y = 1, 2, 3
print(type(x))
print(type(y))

# Answer
<class 'int'>
<class 'list'>
```
