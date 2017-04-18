# Dictionaries
## Dictionary Basics
- Dictionary uses keywords for indexes.
  - The indexes for dictionaries are called *keys*.
  - The key and its associated value are called a *key-value pair*.
- Dictionaries are designated with the curly brackets (`{}`), and the key-value pair is separated with a colon (`:`).
- Dictionary keywords are **unique**. When you add a keyword more than once, the last value overwrites the previous.
- Dictionaries contents can be removed by using the `del` statement followed by the dictionary name and the key in brackets of the key-value pair that will be deleted.
- Dictionary values are accessed by the notation `dict[keyword]`. When a non-existent keyword is assigned a value, that keyword is created.
  - Integers can serve as dictionary keywords. If no keyword exists, a new one is created.


```python
# Dictionary Basics Example
data = {'a':1, 'a':2, 'c':3}
print(data['a'])

# Answer
2
```
- You can use **dictionary comprehension** to create a dictionary.
```python
# Dictionary Basics Example
data = {x:'abc'[x] for x in range(3)}
print(data)

# Answer
{0: 'a', 1: 'b', 2: 'c'}
```
## Dictionaries Vs. Lists
- Items in dictionaries are unordered, there is no *first* item in a dictionary.
- It does not matter in what order the key-value pairs are typed in a dictionary.
- Due to dictionaries not being ordered they cannot be sliced like lists.
  - Trying to access a key that does exist in a dictionary will result in a `KeyError`.

## The `keys()`, `values()`, and `items()` Methods
- There are three dictionary methods that will return list-like values of the dictionary's keys, values, or both keys and values: `keys()`, `values()`, and `items()`.
- They cannot be modified and do not have an `append()` method.
- These list-like values can be used in `for` loops.
  - A `for` loop can also iterate over the keys, values, or both keys and values (key-value pair).
  - **Note:** that the values in the `dict_items` value returned by the `items()` method are tuples of the key and value.
- If a list is needed from one of these methods, pass its list-like return value to the `list()` function
```python
# Dictionary Methods Example
spam = {'color': 'red', 'age': 42}
print(spam.keys())
print(list(spam.keys()))

# Answer
dict_keys(['color', 'age'])
['color', 'age']
```
- The `for` loop multiple assignment trick can be used to assign the key and value to separate variables.
```python
# Dictionary Methods Example
spam = {'color':'red','age':'42'}
for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))

# Answer
Key: color Value: red
Key: age Value: 42
```
## Checking Whether a KEY or VALUE Exists in a Dictionary
- The `in` and `not in` operators can be used to check whether a value exists in a list.
- The operators can also be used to see whether a certain key or value exists in a dictionary.
```python
# in and not in Operators Example
spam = {'name': 'Tyler', 'age': 31}
print('name' in spam.keys())
print('color' in spam.keys())

# Answer
True
False
```