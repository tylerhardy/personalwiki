# Generators
- Function with a yield is a generator function, and returns a generator.
```python
# Generator Example
def func():
    yield 1
    yield 2
    yield 3

print(type(func))
print(type(func())

# Answer
<class 'function'>
<class 'generator'>
```
- Generator function. genr will return 0 once and then None forever, unless something is sent in.
- Generator function. new = yield output assigned 5 to new when genr.send(5) was called.
```python
# Generator Example
def func():
    output = 0
    while True:
        new = yield output
        output = new

genr = func()
print(next(genr))
print(next(genr))
print(genr.send(5))
print(next(genr))

# Answer
0
None
5
None
```
- Generator function. In this case, genr retains the last thing you send in.
```python
# Generator Example
def func():
    output = 0
    while True:
        new = yield output
        output = new if new != None else output


genr = func()
print(next(genr))
print(next(genr))
print(genr.send(5))
print(next(genr))

# Answer
0
0
5
5
```
- Generator function. Because generator-iterators begin execution at the top of the generator's function body, there is no yield expression to receive a value when the generator has just been created. Therefore, calling send() with a non-None argument is prohibited when the generator iterator has just started, and a TypeError is raised if this occurs (presumably due to a logic error of some kind). Thus, before you can communicate with a coroutine you must first call next() or send(None) to advance its execution to the first yield expression
```python
# Generator Example
def func():
    output = 0
    while True:
        new = yield output
        output = new if new != None else output


genr = func()
print(genr.send(5))
print(next(genr))
print(next(genr))
print(next(genr))

# Answer
TypeError: can't send non-None value to a just-started generator
```