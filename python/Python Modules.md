# Python Modules
## `copy` List Module
- The statement `c = copy.copy(b)` is equivalent to `c = b[:]` and creates a shallow copy
```python
# copy Example
import copy

a = [1]
b = [0, a]
c = copy.copy(b)

print(c is b)
print(c[1] is b[1] is a)

# Answer
False
True
```
- The statement `c = copy.deepcopy(b)` creates a deep copy of `b`, duplicating any internal references. 
  - The variable `c[1]` no longer points to `a`
```python
# copy Example
import copy

a = [1]
b = [0, a]
c = copy.deepcopy(b)

print(c is b)
print(c[1] is b[1] is a)

a[0] = 'X'
c[1][0] = 'Y'

print(b)
print(c)

# Answer
False
False
[0, ['X']]
[0, ['Y']]
```
## From `itertools` Import `zip_longest`
- `itertools.zip_longest()` function zip lists, padding the missing items with None (by default)
- `itertools.zip_longest` **fillvalue** kwarg specify what to pad the missing values with (default is None).
```python
# itertools Example
from itertools import zip_longest

a = [1, 2]
b = [3, 4, 5]
c = [7]

print(*list(zip_longest(a, b, c)), sep='\n')

# Answer
(1, 3, 7)
(2, 4, None)
(None, 5, None)

# itertools Example 2
from itertools import zip_longest

a = [1, 2]
b = [3, 4, 5]
c = [7]

for i in zip_longest(a, b, c, fillvalue='X'):
    print(i)

# Answer
(1, 3, 7)
(2, 4, 'X')
('X', 5, 'X')
```

## `pyperclip` Module
- The `pyperclip` module has `copy()` and `paste()` functions that can send text to and receive text from the computer's clipboard.
