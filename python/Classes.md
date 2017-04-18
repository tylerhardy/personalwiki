# Classes
- Class attributes can be added outside class definition.
```python
# Class Example
class mycls():
    pass

mycls.x = 1
print(mycls.x)

# Answer
1
```
- Class attributes can be removed by del.
```python
# Class Example
class mycls():
    x = 1

print(mycls.x)
del mycls.x
print(mycls.x)

# Answer
1
AttributeError: type object 'mycls' has no attribute 'x'
```
- Multiple inheritance.
```python
# Class Example
class A:
    x = 1

class B:
    y = 2

class C(A, B):
    pass

print(C.x, C.y)

# Answer
1 2
```
- Class attribute x is shared by all instances.
```python
# Class Method
class mycls:
    x = 1

obj1 = mycls()
print(obj1.x)

mycls.x = 2
obj2 = mycls()
print(obj1.x, obj2.x)

# Answer
1
2 2
```