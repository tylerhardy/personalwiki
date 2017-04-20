
# Programming Concepts Definitions
## **Low-Level Language**
A programming language that is designed to be easy for a computer to execute; also called **"machine language"** or **"assembly language."**
## **Semantics**
The meaning of a program.
## **Debugging**
The process of finding and removing any of the three kinds of programming errors: *Syntax Errors*, *Logic Errors*, and *Exceptions*.
## **Semantic Error**
An error in a program that makes it do something other than what the programmer intended.
## **Program**
A set of instructions that specifies a computation.
## **Interpret**
To execute a program in a high-level language by translating it one line at a time.
## **Object Code**
The output of the compiler after it translates the program.
## **Natural Language**
Any one of the languages that people speak that evolved naturally.
## **Formal Language**
Any one of the languages that people have designed for specific purposes, such as representing mathematical ideas or computer programs
## **Source Code**
A program in a high-level language before being compiled
## **Token**
One of the basic elements of the syntactic structure of a program, analogous to a word in a natural language.
## **Parse**
To examine a program and analyze the syntactic structure.
## **Prompt**
Characters displayed by the interpreter to indicate that it is ready to take input from the user.
## **Script**
A program stored in a file (usually one that will be interpreted).
## **High-Level Language**
A programming language like Python that is designed to be easy for humans to read and write.
## **Print Statement**
An instruction that causes the Python interpreter to display a value on the screen.
## **Problem Solving**
The process of formulating a problem, finding a solution, and expressing the solution.
## **Executable**
Another name for object code that is ready to be executed.
## **Portability**
A property of a program that can run on more than one kind of computer.
## **Algorithm**
A general process for solving a category of problems.
## **Script Mode**
A way of using the Python interpreter to read and execute statements in a script.
## **Compile**
To translate a program written in a high-level language into a low-level language all at once, in preparation for later execution.
## **Exception**
An error that is detected while the program is running.
## **Syntax**
The structure of a program.
## **Bug**
An error in a program.
## **Interactive Mode**
A way of using the Python interpreter by typing commands and expressions at the prompt.
## **Syntax Error**
An error in a program that makes it impossible to parse (and therefore impossible to interpret).
## **Expression**
A combination of variables, operators, and values that represents a single result value.
```python
n + 25
```
## **Expression**
The most basic kind of programming instruction in the language.  Expressions consist of *values* (such as `2`) and *operators* (such as `+`), and they can always *evaluate* (that is, reduce) down to a single value. Expressions can be used anywhere that you could also use a *value*.  A single value with no operators is also considered an expression.
## **Data Type**
A category for values.  Every value belongs to exactly one data type.
## **Assignment Statement**
An assignment statement consists of a variable name, an equal sign (called the *assignment operator*), and the value to be stored.
## **Assignment**
A statement that assigns a value to a variable
## **State Diagram**
A graphical representation of a set of variables and the values they refer to.
```python
message ---> 'And now for something completely different'
n ---------> 17
pi --------> 3.1415926535897932
```
## **Keyword**
A reserved word that is used by the compiler to parse a program.
```
print()
if
and
or
not
```

## **Operator**
A special symbol that represents a simple computation like addition, multiplication, or string concatenation.
```python
32 + 8 / 4
# The plus and the divide symbols are the operator
```
## **Operand**
One of the values on which an operator operates.
```python
32 + 8 / 4
# The int variables 32, 8, and 4 are the operands.
```
## **Integer**
A type that represents whole numbers.
```python
x = 32
# 32 is an integer type variable
```
## **Floating-point**
A type that represents numbers with fractional parts.
```python
x = 3.14
# 3.14 is a floating-point type variable
```
## **String**
A type that represents sequences of characters.
```python
var = 'Hello World'
# 'Hello Wolrd' is a string type variable
```
## **Statement**
A section of code that represents a command or action.
```python
n = 17
```
## **Variable**
A name that refers to a value
```python
x = 1
# x is a variable that refers to the value of 1
```
## **Floor Division**
The operation that divides two numbers and leaves off the fraction part (remainder).
## **Evaluate**
To simplify an expression by performing the operations in order to yield a single value.
## **Rules of Precedence**
The set of rules governing the order in which expressions involving multiple operators and operands are evaluated.
```python
 1 + 2**3 - (1+1)**(5-2) 
```
## **Concatenate**
To join two operands end-to-end.
```python
x = 'a' 'b' + str(y) + "c!"
```
## **Comment**
Information in a program that is meant for other programmers (or anyone reading the source code) and has no effect on the execution of the program.
## **Iterables**
An object capable of returning its members one at a time
## **Instance**
A member of a set
## **Loop**
A part of a program that can execute repeatedly.
## **Encapsulation**
The process of transforming a sequence of statements into a function definition.
```python
# Expressions and Statements are encapsulated in a function
def square(t, length):
    t = turtle.Turtle()
    t.speed('fastest')
    print(t)
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()

square('bob', 200)
```
## **Generalization**
The process of replacing something unnecessarily specific (like a number) with something appropriately general (like a variable or parameter).
## **Keyword Argument**
An argument that includes the name of the parameter as a **Keyword**.
## **Interface**
A description of how to use a function, including the name and descriptions of the arguments and return value.
## **Refactoring**
The process of modifying a working program to improve functionn interfaces and other qualities of the code.
## **Development Plan**
A process for writing programs.
## **Docstring**
A string that appears in a function definition to document the function's interface.
## **Precondition**
A requirement that should be satisfied by the caller before a function starts.
## **Postcondition**
A requirement that should be satisfied by the function before it ends.
## **Function**
A named sequence of statements that performs some useful operation.  Functions may or may not take arguments and may or may not produce a result.
```python
''' Function Definition and invocation.'''
def someFunction(string_var):
    some_string = ''
    if string_var:
        some_string = "Hello " + str(string_var) + "!"
        return some_string
    else:
        return 'The string variable string_var is empty'

new_string = ''
new_string = someFunction('World')
print(new_string)

# Answer
Hello World!
```
## **Function Definition**
A statement (`def`) that creates a **new function**, specifying its name, parameters, and the statements it executes.
```python
def someFunction(string_var):
    some_string = ''
    if string_var:
        some_string = "Hello " + str(string_var) + "!"
        return some_string
    else:
        return 'The string variable string_var is empty'
```
## **Function Object**
A value created by a function definition.  The name of the function is a variable that refers to a function object.
```python
# Function Object: someFunction
print(someFunction)
# <function someFunction at 0x0000026B6F983E18>
print(type(someFunction))
# <class 'function'>
```
## **Function Call**
A statement that executes a function.  It consists of the function name followed by an argument list in parentheses.
```python
# Function Name: someFunction
# Argument List: ('World')
someFunction('World')
```
## **Header**
The first line of a function definition.
```python
def someFunction(string_var):
```
## **Body**
The sequence of statements inside a function definition.
```python
    some_string = ''
    if string_var:
        some_string = "Hello " + str(string_var) + "!"
        return some_string
    else:
        return 'The string variable string_var is empty'
```
## **Parameter**
A name used inside a function to refer to the value passed as an argument.
```python
def someFunction(string_var):
# The parameter for the function someFunction(string_var) is string_var
```
## **Argument**
A value provided to a function when the function is called.  This value is assigned to the corresponding parameter in the function.
```python
# The argument is the string value 'World' in the function call (somefunction())
new_string = someFunction('World')
```
## **Local Variable**
A variable defined inside a function.  A *Local Variable* can only be used inside its function.
```python
some_var = 'Hi'
def anotherFunction():
    # The Local Variable
    new_var = 'Hello'

# This will cause an error since it is calling a Local Variable from outside the Local Scope.
print(new_var)
```
## **Return Value**
The result of a function. If a function call is used in an expression, the return value is the value of the expression.
```python
def simpleFunction():
    x = 1 + 1
    return x
# The y variable receives the return value from the function call expression.
y = simpleFunction()
print(y)
# The return value
2
```
## **Fruitful Function**
A function that returns a value.
```python
def fruitFul():
    return "Hello!"
print(fruitFul())
```
## **Void Function**
A function that doesn't return a value.
```python
def fruitFul():
    print("Hello!")
print(fruitFul())
```
## **Module**
A file that contains a collection of related functions and other definitions.

## **Module Object**
A value created by an import statement that provides access to the values defined in a module.
## **Import Statement**
A statement that reads a module file and creates a module object.
## **Dot notation**
The syntax for calling a function in another module by specifying the module name followed by a dot (period) and the function name.
## **Composition**
Using an expression as part of a larger expression, or a statement as part of a larger statement.
## **Flow of Execution**
The order in which statements are executed during a program run.
## **Stack Diagram**
A graphical representation of a stack of functions, their variables, and the values they refer to.
## **Frame**
A box in a stack diagram the represents a funcntion call.  It contains the local variables and parameters of the function.
## **Traceback**
A list of the functions that are executing, printed when an exception occurs.
## **Modulus Operator**
An operator, denoted with a percent sign (%), that works on integers and yields the remainder when one number is divided by another.
## **Boolean Expression**
An expression whose value is either **True** or **False**.
## **Relational Operator**
One of the operators that compares its operands: `==`. `!=`, `>`, `<`. `>=`, and `<=`.
## **Logical Operator**
One of the operators that combines boolean expressions: `and`, `or`, and `not`.
## **Conditional Statement**
A statement that controls the flow of execution depending on some condition.
## **Condition**
The boolean expression in a conditional statement that determines which branch is executed.
## **Compound Statement**
A statement that consists of a header and a body.  The header ends with a colon (`:`). The body is indented relative to the header.
## **Branch**
One of the alternative sequences of statements in a conditional statement.
## **Chained Conditional**
A conditional statement with a series of alternative branches.
## **Nested Conditional**
A conditional statement that appears in one of the branches of another conditional statement.
## **Recursion**
The process of calling the function that is currently executing.
## **Base Case**
A conditional branch in a recursive function that does not make a recursive call.
## **Infinite Recursion**
A recursion that doesn't have a base case, or never reaches it.  Eventually, an **Infinite Recursion** causes a runtime error.
## **Temporary Variable**
A variable used to store an intermediate value in a complex calculation.
## **Dead Code**
Part of a program that can never be executed, often because it appears after a **return** statement.
## **None**
A special value returned by functions that have no return statement or a retrun statement without an argument.
## **Incremental Development**
A program development plan intended to avoid debugging by adding and testing only a small amount of code at a time.
## **Scaffolding**
Code that is used during program development but is not part of the final version.
## **Gaurdian**
A programming pattern that uses a conditional statement to check for and handle circumstances that might cause an error.
## **Multiple Assignment**
Making more than one assignment to the same variable during the execution of a program.
## **Update**
An assignment where the new value of the variable depends on the old.
## **Initialization**
An assignment that gives an initial value to a variable that will be updated.
## **Increment**
An update that increases the value of a variable (often by one).
## **Decrement**
An update that decreases the value of a variable.
## **Iteration**
Repeated execution of a set of statements using either a recursive function call or a loop
## **Infinite Loop**
A loop in which the termincating condition is never satisfied.
## **Object**
Something a variable can refer to.  For now, you can use Object and 'Value' interchangeably.
## **Sequence**
An ordered set; that is, a set of values whee each value is identified by an integer index.
## **Item**
One of the values in a sequence.
## **Index**
An integer value used to select an item in a sequence, such as a character in a string.
## **Slice**
A part of a string specified by a range of indices.
## **Empty String**
A string with no characters and length of 0, represented by two quotation marks.
## **Immutable**
The property of a sequence whose items cannot be assigned.
## **Traverse**
To iterate through the items in a sequence, performing a similar operation on each.
## **Search**
A pattern of traversal that stops when it finds what it is looking for.
## **Counter**
A variable used to count something, usually initialized to zero and then incremented.
## **Method**
A function that is associated with an object and called using dot notation.
