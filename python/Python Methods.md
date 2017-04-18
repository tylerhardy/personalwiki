# Python Methods
- Methods can be stringed together to form **Method Chaining**.
```python
# Method Chaining Example
text = 'Hello world'
x = text.lower()[::-1].title()
print(x)

# Answer
Dlrow Olleh
```
## `print()` Method
- The `print()` method by default ends with a new line.  
- The `print()` method `End [arg]` overrides the implide `\n`.
- The `print()` method `sep` kwarg specifies a separator between arguments.
```python
# print() Example
a = [1, 2]
b = [4, 5, 6]
c = 'hello'

print(a, b, c, sep='\n')

# Answer
[1, 2]
[4, 5, 6]
hello
```