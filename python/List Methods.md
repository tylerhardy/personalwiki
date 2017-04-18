# List Methods

## `remove()` Method
- The list `remove()` method returns a `ValueError` if the value is not in the list.
```python
# remove() Example
x = [0, 1, 2, 1]
x.remove(4)
print(x)

# Answer
ValueError: list.remove(x): x not in list
```

## `index()` Method
- *List values* have an `index()` method that can be passed a value, and if that value exists in the list, the index of the value is returned.
  - If that value is not in the list then Python produces a `ValueError` error.
- If there are duplicate values in the list the first appearance is returned.

## `count()` Method
- List method `count()` returns the number of occurences
```python
# count() Example
var = ['a', 'b', 'c', 'a']
i = var.count('a')
print(i)

# Answer
2
```

## `pop()` Method
- List method `pop()` removes a single element from list and returns it. 
- By default, pop removes and returns the last element.
```python
# pop() Example
x = [0, 1, 2, 3]
y = x.pop()
print(x)
print(y)

# Answer
[0, 1, 2]
3
```

## `remove()` Method
- List method `remove()` removes the first occurence of a value from a list.
- List method `remove()` returns a ValueError if value is not in a list
  - Modifying the expression with `x.remove(3)` will however return ValueError: `ValueError: list.remove(x): x not in list`
```python
# remove() Example
x = [4, 5, 6, 5]
x.remove(5)
print(x)

# Answer
[4, 6, 5]
```

## `append()` Method
- List method `append()` adds a single element to the end of the list.
```python
# append() Example
x = [0, 1, 2]
x.append(3)
print(x)

# Answer
[0, 1, 2, 3]
```
- List method `append()` always adds a single element to a list.
```python
# append() Example
x = [0, 1, 2]
x.append([3 ,4])
print(x)
print(x[3])

# Answer
[0, 1, 2, [3, 4]]
[3, 4]
```

## `insert()` Method
- The `insert()` method inserts a value at any index in the list.
  - The first argument to `insert()` is the index for the new value.
  - The second argument is the new value to be inserted.
```python
# insert() Example
var = ['a', 'b', 'c', 'a']
var.insert(2, 'z')
print(var)

# Answer
['a', 'b', 'z', 'c', 'a']
```

## `extend()` Method
- List method `extend()` takes an iterable and adds it to a list as **separate** elements.
```python
# extend() Example
x = [0, 1, 2]
x.extend([3, 4])
print(x)

# Answer
[0, 1, 2, 3, 4]
```

## `sort()` Method
- Lists of number values or lists of strings can be sorted with the `sort()` mehtod.
- The `reverse` keyword argument can be included in `sort()` with the condition `True` to sort the values in reverse order.
  - `var.sort(reverse=True)`
- There are three things to keep in mind with the `sort()` method:
  1. The `sort() method sorts the list in place. You cannot capture the return value by assigning it to a new variable.
  2. Lists with both number values and string values cannot be sorted.
  3. The `sort()` method uses "ASCIIbetical order" rather than actual alphabetical order for sorting strings.
    - Uppercase letters come before lowercase letters.
    - If you need to sort the values in regular alphabetical order, pass `str.lower` for the `key` keyword argument in the `sort()` method call.