# Elements of Flow Control
Flow control statements often start with a part called the *condition*, and all are followed by a block of code called the *clause*.
- All flow control statements end with a colon and are followed by a new block of code (the clause).
## Conditions
- Conditions always evaluate down to a Boolean value, `True` or `False`.
- A flow control statement decides what to do based on whether its condition is `True` or `False`, and almost every flow control statement uses a condition.
## Blockes of Code (The Clause)
- Lines of Python code can be grouped together in blocks
- You can tell when a block begins and ends from the indentation of the lines of code.
- There are three rules for blocks.
  * Blocks begin when the indentation increases.
  * Blocks can contain other blocks.
  * Blocks end when the indentation decreases to zero or to a containing block’s indentation.
## Statements
- Decisions your programs will make.
### IF Statements
```python
name = 'Alice'
if name == 'Alice':
    print('Hi, Alice.')
```
- Most common type of flow control.
  * An `if` statement's clause will execute if the statement's conditon is `True`.
  * Clause is skipped if condition is `False`.
- In python, an `if` statement consists of the following:
  * The `if` keyword
  * A condition (an expression that evaluates to `True` or `False`)
  * A colon `:`
  * Starting on the next line, and indented block of code (called the `if` clause)
### Else Statements
```python
name = 'Bob'
if name == 'Alice':
    print('Hi, Alice.')
else:
    print('Hello, stranger.')
```
- An `if` clause can optionally be followed by an `else` statement.
- The `else` clause is executed only when the `if` statement's condition is `False`.
- An `else` statement doesn't have a condition.
- In python, an `else` statement consists of the following:
  * The `else` keyword
  * A colon `:`
  * Starting on the next line, and indented block of code (called the `else` clause)
### Elif Statements
```python
name = 'Bob'
age = 5
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
```
- The `elif` statement is an "else if" statement that always follows an `if` or another `elif` statement.
- Provides another condition that is checked only if all the previous conditions were `false`.
- In python, an `elif` statement consists of the following:
  * The `elif` keyword
  * A condition (an expression that evaluates to `True` or `False`)
  * A colon `:`
  * Starting on the next line, and indented block of code (called the `elif` clause)
- In `elif` statements order does matter.
### While Loop Statements
```python
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1
```
- The code in a `while` clause will be executed as long as the `while` statement's condition is `True`.
- In python, a `while` statement consists of the following:
  * The `while` keyword
  * A condition (an expression that evaluates to `True` or `False`)
  * A colon `:`
  * Starting on the next line, and indented block of code (called the `while` clause)
- In the `while` loop, the condition is always checked at the start of each *iteration*.
### Break Statements
```python
while True:                         # (1)
    print('Please type your name.')
    name = input()                  # (2)
    if name == 'your name':         # (3)
        break                       # (4)
print('Thank you!')                 # (5)
```
- Used inside loops (while and for)
- Code execution that reaches a `break` statement will immediately exit the `while` loop's clause.
### Continue Statements
```python
while True:
  print('Who are you?')
  name = input()
  if name != 'Joe':       #(1)
    continue              #(2)
  print('Hello, Joe. What is the password? (It is a fish.)') 
  password = input()      #(3)
  if password == 'swordfish':
    break                 #(4)
print('Access granted.')  #(5)
```
- Used inside loops (while and for)
- When the program execution reaches a `continue` statement it immediately jumps back to the start of the loop and reevaluates the loop's condition.
  * This is also what happens when the execution reaches the end of the loop.
## For Loop Statements and the Range() Function
```python
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')
```
- Used to execute a block of code for only a certain number of times.
- Loop statements may have an `else` clause; it is executed when the loop terminates through exhaustion of the list (with `for`) or when the condition becomes false (with `while`), but not when the loop is terminated by a `break` statement.
- In python, a `for` statement consists of the following:
  * The `for` keyword
  * A variable name
  * The `in` keyword
  * A call to the `range()` method with up to three integers passed to it
  * A colon `:`
  * Starting on the next line, and indented block of code (called the `for` clause)
- The variable `i` will go up to, but will not include, the integer passed to `range()`.
- The `range()` method parameters:
  * `range(stop)`
  * `range([start], stop[, step])`
    - `start`: Starting number of the sequence.
    - `stop`: Generate numbers up to, but not including this number.
    - `step`: Difference between each number in the sequence.

## Importing Modules
```python
import random
for i in range(5):
    print(random.randint(1, 10))
```
- Python can call a basic set of functions called *built-in functions*
  - Python also comes with a set of modules called the *standard library*.
- Each module is a Python program that contains a related group of functions.
- In python, an `import` statement consists of the following:
  * The `import` keyword
  * The name of the module
  * Optionally, more module names, as long as they are separated by commas
    - `import random, sys, os, math`
- Once a module is import you have access to all the functions in that module.
### From Import Statements
- An alternative form of the `import` statement.
- It is composed of the `from` keyword, followed by the module name, the `import` keyword, and a star(`*`)
  * `from random import *`
- Using this form of `import` statement, calls to functions in the module will not need the `module` prefix in the  `module.function` method.
## Ending a Program Early with Sys.exit()
```python
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
```
- Terminates the program.
- This will always happen if the program execution reaches the bottom of the instructions.
- You can cause the program to terminate, or exit, by calling the `sys.exit()` function.
  * Since this function is in the `sys` module you will have to import `sys` before you can use it.
