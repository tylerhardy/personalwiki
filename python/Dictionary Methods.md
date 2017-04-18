# Dictionary Methods

## `keys()` Method
- The `keys()` method will return list-like values of the dictionary's keys.
- If a list is needed from one of these methods, pass its list-like return value to the `list()` function
- Cannot modify the dictionary.
```python
# keys() Example
var = {'color': 'red', 'age': 42}
print(var.keys())
print(list(var.keys()))

# Answer
dict_keys(['color', 'age'])
['color', 'age']

# keys() Example 2
for k in var.keys():
    print(k)

# Answer
color
age
```

## `values()` Method
- The `values()` method will return list-like values of the dictionary's values.
- If a list is needed from one of these methods, pass its list-like return value to the `list()` function
- Cannot modify the dictionary.
```python
# keys() Example
var = {'color': 'red', 'age': 42}
print(var.values())
print(list(var.values()))

# Answer
dict_values(['red', 42])
['red', 42]

# values() Example 2
var = {'color': 'red', 'age': 42}
for v in var.values():
    print(v)

# Answer
red
42
```

## `items()` Method
- The `items()` method will return list-like values of both the dictionary's keys and values.
- If a list is needed from one of these methods, pass its list-like return value to the `list()` function
- Cannot modify the dictionary.
- **Note:** that the values in the `dict_items` value returned by the `items()` method are tuples of the key and value.
```python
# keys() Example
var = {'color': 'red', 'age': 42}
print(var.items())
print(list(var.items()))

# Answer
dict_items([('color', 'red'), ('age', 42)])
[('color', 'red'), ('age', 42)]

# items() Example 2
for i in var.items():
    print(i)

# Answer
('color', 'red')
('age', 42)
```

## `get()` Method
- The `get()` dictionary method takes *two* arguments: the **key** of the value to retrieve and a **fallback value** to return if that key does not exist.
  - By default the *fallback value* returns **None**.
- The `get()` dictionary method will not throw an error when non-existent keywords are accessed.
```python
# get() Example
picnic_items = {'apples':5,'cups':2}
print('I am bringing ' + str(picnic_items.get('cups',0)) + ' cups.')
print('I am bringing ' + str(picnic_items.get('eggs',0)) + ' eggs.')

# Answer
I am bringing 2 cups.
I am bringing 0 eggs.

# get() Example 2
x = {'a':0, 'b':1}
y, z = x.get('a'), x.get('c')
print(y, z)

# Answer
0 None
```

## `setdefault()` Method
- The `setdefault()` dictionary method will set a value for a certain key **only** if that key does not already have a value.
- The `setdefault()` method takes in *two* arguments, the **first arguments** is the `key` to check for and the **second arguments** is the `value` to set if that *`key` does not exist*.
```python
# setdefault() Example
var = {'name': 'Pooka','age':5}
var.setdefault('color','black')
print(var)

# Answer
{'name': 'Pooka', 'age': 5, 'color': 'black'}

# setdefault() Example 2
var.setdefault('color','white')
print(var)

# Answer
{'name': 'Pooka', 'age': 5, 'color': 'black'}
```

## `update()` Method
- The `update()` methods adds content of one dictionary to another.
```python
# update() Example
x = {'a':1, 'b': 2}
y = {'b':10, 'c': 11}

y.update(x)
print(y)

# Answer
{'b': 2, 'c': 11, 'a': 1}
```