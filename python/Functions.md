# Functions
## Function Basics
```python
def function-name(parameters):
    statements
```
- When functions are defined they will not execute
- Funcionts will only executes when called
- Global effect outside functions while nonlocal effects outer function only one level up
- Functions only effect variables within function unless set globally or to nonlocal
- A string defined at the beginning of a function is the docstring (called by [method].\_\_doc_\_)
- Functions cannot be empty (Syntax error: expected an indented block)
- To make a function do nothing the variable: `pass` must be included in the indented block
  - A function that doesn't return anything, returns `None`
- Functions are objects, you can add attributes to them.
```python
# Function Example
def func():
    pass

func.x = 5
print(func.x)

# Answer
5
```
## Return
- The `return` statment leaves the current function call with `None`, `expression`, or `tuple` as return value.
```python
# Return Value
return
return expression
return tuple
```
- Function can return itself.
```python
# Return Example
def func():
    global x
    x += 1
    return func

x = 0
func()()()
print(x)

# Answer
3
```
## Default Argument Values
```python
def function_name(arg=value):
    pass
```
- Used to specify a default value for one or more arguments. This creates a function that can be called with fewer arguments than it is defined to allow.
- The default values are evaluated at the point of function definition in the defining scope, so that the example below will print `5`.
```python
i = 5
def f(arg=i):
    print arg
i = 6
f()
```
- The default value is evaluated only once. This makes a difference when the default is a mutable object such as a `list`, `dictionary`, or `instances` of most classes.
```python
def f(a, L=[]):
    L.append(a)
    return L

print f(1)
print f(2)
print f(3)
```
```python
[1]
[1, 2]
[1, 2, 3]
```
## Keyword Arguments
- Functions can also be called using keyword arguments of the form `kwarg=value`. 
- Keyword arguments must follow positional arguments. 
- All the keyword arguments passed must match one of the arguments accepted by the function, and their order is not important.

## Function Basics
- In python, a `function` consists of the following:
  - First line in a `def` defines the **function**.
  - The code block (or clause) is the body of the function.
  - The code within the clause is executed when the function is called, not when the function is first defined.
    - This is refered to as **Function Calls**.
- In code a *function call* is just the function's name followed by parentheses.
  * The `print()` statement is an example.
- A major purpose of functions is to group code that gets executed multiple times.
## Def Statements with Parameters
- Values that are passed into functions are called *arguments*.
- A *parameter* is a variable that an *argument* is stored in when a function is called.
- The value stored in a parameter is forgotton (destroyed) when the function returns.
## Return Values and Return Statements
- The value that a function call evaluates to is called the *return value* of the function.
- The return value can be specified with a `return` statement.
- A `return` statement consists of the following:
  - The `return` keyword
  - The value or expression that the function should return.
- When an expression is used with a `return` statement, the *return value* is what this expression evaluates to.
- *Return Values* can be passed in as an argument to another function call.
- A function does nothing after a `return` statement.
## The None Value
- The value `None` represents the absence of a value.
  - `None` is the only value of the `NoneType` data type (`null` in other programming languages).
- Python adds `return None` to the end of any function definition with no `return` statement.
## Keyword Arguments
- Most arguments are identified by their position in the function call.
- *Keyword arguments* are identified by the keyword put before them in a function call.
- *Keyword arguments* arSe often used for optional parameters.
## Local and Global Scope
- Parameters and variables that are assigned in a called function exist in that function's *local scope*.
  - A variable that exists in the *local scope* is called a *local variable*. 
- Variables that are assigned outside all functions exist in the *global scope*.
  - A variable that exists in the *global scope* is called a *global variable*.
- A variable must be a *local variable* or *global variable*, it cannot be both.
- A local scope is created when a function is called.
  - Any variables assigned in this function exist within the local scope.
  - When the function returns, the local scope is destroyed and all the variables in the local scope are forgotton.
- Important notes about scope:
  - Code in the global scope cannot use any local variables.
  - A local scope can access global variables.
  - Code in a function's local scope cannot use variables in any other local scope.
  - The same name can be used for different variables if they are in different scopes.
- It is often considered a bad habbit to rely on global variables in large pograms.
## Global Statement
- The `global` statement is used to modify a global variable from within a function.
- There are four rules to tell whther a variable is in a local scope or global scope:
  1. If a variable is being used in the global scope then it is always a global variable.
  2. If there is a `global` statement for that variable in a function, it is a global variable.
  3. If the variable is used in an assignment statement in the function, it is a local variable.
  4. If the variable is not used in an assignment statement, it is a global variable.
## Error Handling
- Errors in a program can be handled with `try` and `except` statements.
- When code in a `try` clause causes an error, the program execution immediately moves to the code in the `except` clause.
  - After running the `except` clause code, the execution continues as normal.
- Any errors that occur in function calls in a `try` block will also be caught.
## Methods
- A *method* is the same thing as a function, except it is "called on" a value.
- Each data type has its own set of methods.

### Function Default Arguments
```python
def func(x=[]):
    x.append(1)
    return x

for i in range(4):
    print(func())
```
- Mutable default arguments of a function are persistent.
  - The above example would return: 
```
[1]
[1, 1]
[1, 1, 1]
[1, 1, 1, 1]
```
