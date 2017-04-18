# Python Functions
## `enumerate()`
- The `enumerate()` function returns tuples in a form of **(index, item)**.
```python
# enumerat() Example
x = ['a', 'b', 'c', 'd']
y = list(enumerate(x))
print(y)
print(type(y[1]))

# Answer
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
<class 'tuple'>
```
### `enumerate()` Foor Loop
- The `enumerate()` forloop function iterates over a sequence and returns **an item with an index**.
```python
# enumerate() Example
x = ['a', 'b', 'c', 'd']
for ind, itm in enumerate(x):
    print(ind, itm)

# Answer
0 a
1 b
2 c
3 d
```
- The `enumerate()` forloop function can be used to **enumerate** in list comprehensions.
```python
# enumerate() Example
x = ['a', 'b', 'c', 'd']
y = [i for i in enumerate(x)]
print(y)

# Answer
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
```
- The `enumerate()` for loop function can index from any starting number by specifying the `start` argument.
```python
# enumerat() Example
x = ['a', 'b', 'c', 'd']
y = [i for i in enumerate(x, start=5)]
print(y)

# Answer
[(5, 'a'), (6, 'b'), (7, 'c'), (8, 'd')]
```
- This program creates a string with alternating upper- and lower-case characters. `[i%2 == 0]` selects one of the elements from `[j.lower(), j.upper()]` by using `False==0` and `True==1` equivalency.
```python
# enumerate() Example
line1 = '''\
increased
throttling
capability'''

my_list = [[j.lower(), j.upper()][i%2 == 0] for i, j in enumerate(line1)]
line2 = ''.join(my_list)
print(line2)

# Answer
InCrEaSeD
ThRoTtLiNg
cApAbIlItY
```
## `zip()` Function
- The `zip()` function combines lists into a list of tuples.
```python
# zip() Example
a = [1, 2, 3]
b = [4, 5, 6]

for i in zip(a, b):
    print(i)

# Answer
(1, 4)
(2, 5)
(3, 6)
```
- The `zip()` function returns a list of tuples equal to the length of the shortest list.
```python
# zip() Example
a = [1, 2]
b = [4, 5, 6]

for i in zip(a, b):
    print(i)

# Answer
(1, 4)
(2, 5)
```
- You can `zip()` strings.
```python
# zip() Example
a = 'hello'
b = 'world'

print(*list(zip(a, b)), sep='\n')

# Answer
('h', 'w')
('e', 'o')
('l', 'r')
('l', 'l')
('o', 'd')
```
## `lambda` Function
- The `lambda` function is a way to create short functions.
```python
# lambda Example
func = lambda x : x+1
a = func(1)
print(a)

# Answer
2
```
- The `lambda` function uses variables from the external scope.
```python
# lambda Example
func = lambda: 1 if x else 2

x = True
print(func())
x = False
print(func())

# Answer
1
2
```
- The `print('2')` statement is not a part of `func` definition, it's just in the same line, but separated by `;` The code is identical to:
```python
# lambda Example
func = lambda: print('1'); print('2');

func()

# Answer
2
1

# lambda Example 2
func = lambda: print('1');
print('2');

func()

# Answer
2
1
```
- The `lambda` function can be used for multiple arguments and with default values.
```python
# lambda Example
func = lambda x=1, y=1: x + y

print(func())
print(func(2))
print(func(2, 3))

# Answer
2
3
5
```
## `any()` Function
- The `any()` function returns `True` if at least one of the arguments is `True`.
```python
# any() Example
x = [0, 0, 0, 1]

if any(x):
    print('yes')
else:
    print('no')

# Answer
yes

#any() Example 2
x = [0, '', 0.0, False]

if any(x):
    print('yes')
else:
    print('no')

# Answer
no
```
## `all()` Function
- The `all()` function returns `True` if all the arguments are `True`.
```python
# all() Example
x = [1, 2, 3]

if all(x):
    print('yes')
else:
    print('no')

# Answer
yes
```

## `str()` Function
- The `str()` function converts numbers to strings.
```python
# str() Example
x = 'Hello '
y = 7
print(x + str(y))

# Answer
Hello 7
```
## `list()` Function
- The function `list()` will return list versions of the values passed to it.
```python
# list() Example
print(list((1,2,3)))

# Answer
[1, 2, 3]
```
- The `list()` function turns a `string` into a `list` of characters.
```python
# list() Example
t = 'hel lo'
print(list(t))

# Answer
['h', 'e', 'l', ' ', 'l', 'o']
```

## `tuple()` Function
- The function `tuple()` will return tuple versions of the values passed to it.
  - This is a generator expression. There is no tuple comprehension.
- For tuple comprehension, use the tuple() function.
```python
# tuple() Example
x = (i**2 for i in range(4))
print(x)

print(tuple([1,2,3]))

y = tuple(i**2 for i in range(4))
print(y)
# Answer
<generator object <genexpr> at 0x000001EB156FD410>
(1, 2, 3)
(0, 1, 4, 9)
```