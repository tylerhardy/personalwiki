# Reading and Writing Files
## Files and File Paths
- A file has two key properties:
  - *filename*
  - *Path*
### `os.path.join()` Function
- Retuns a string with the correct path separators
```python
# os.path.join() Example
import os
var = os.path.join('usr','bin','spam')
print(var)

# Answer On Linux
user/bin/spam
# Answer on Windows
usr\bin\spam
```
### `os.getcwd()` Function
- Returns the current working directory
```python
# os.getcwd() Example
os.getcwd()
# Answer
'C:\\Python34'
```
### `os.chdir()` Function
- Changes the working directory to whatever is passed as an argument
```python
# os.chdir Example
os.chdir('C:\\Windows\\System32')
os.getcwd()
# Answer 
'C:\\Windows\\System32'
```
### `os.makedirs()` Function
- Creates a directory in the location passed as an argument
- It will create any necessary intermediate folders in order to ensure that the full path exists
```python
# os.makedirs() Example
import os
os.makedirs('C:\\delicious\\walnut\\waffles')
```

## `os.path` Module
### `os.path.abspath(path)` Function
- Returns a string of the absolute path of the argument
### `os.path.isabs(path)` Function
- Returns `True` if the argument is an absolute path
- Returns `False` if the argument is a relative path
### `os.path.relpath(path, start)` Function
- Returns a string of a relative path from the `start` path to `path`.
- If `start` is not provided the current working directory is used as default
### `os.path.dirnamt(path)` Function
- Returns a string of everything that comes **before** the last slash in the `path` argument.
### `os.path.basename(path)` Function
- Returns a string of everything that comes **after** the last slash in the `path` argument.
### `os.path.split(path)` Function
- Returns a tuple value of the path's dir name and the base name
### Spliting All Folders in a Path
- Use the `split()` string method and split on the string in `os.sep` variable.
```python
# Splitting All Folders Example
import os
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
print(calcFilePath.split(os.path.sep))

# Answer
['C:', 'Windows', 'System32', 'calc.exe']
```
## Finding File Size and Foler Contents
### `os.path.getsize(path)` Function
- Returns the size in bytes of the file in the `path` argument
### `os.listdir(path)` Function
- Returns a list of filename strings for each file in the `path` argument
```python
# os.path.getsize(path) and os.listdir(path) Example
import os
totalSize = 0
folder = 'C:\\Windows\\System32'
for filename in os.listdir(folder):
    fileSize = os.path.getsize(os.path.join(folder, filename))
    totalSize += fileSize
print(totalSize)
# Answer
2456729766
```

## Checking Path Validity
- The `os.path` module provides functions to check whether a given path exists and whether it is a file or folder.
### `os.path.exists(path)` Function
- Returns `True` if file or folder referred to in the argument **exists**
- Returns `False` if file or folder referred to in the argument **does not exists**
### `os.path.isfile(path)` Function
- Returns `True` if the path argument exists and is a file
- Returns `False` if the path argument does not exists and/or is not a file
### `os.path.isdir(path)` Function
- Returns `True` if the path argument exists and is a folder
- Returns `False` if the path argument does not exists and/or is not a folder

## File Reading/Writing Process
- **Plaintext Files** contain only basic text characters and do not include font, size, or color information.
- **Binary Files** are all other file types.
- Three steps to reading or writing files in Python:
  1. Call the `open()` function to return a `File` object.
  2. Call the `read()` or `write()` method on the `File` object.
  3. Close the file by calling the `close()` method on the `File` object.

## Opening Files with the `open()` Function
### `open()` Function
- The `open()` function takes string paths to the file as absolute or relative path.
- The `open()` function returns a `File` object.
- To open a file in reading mode you pass the `'r'` argument as the second paramter in the `open()` function.
- To open a file in writing mode you pass the `'w'` argument as the second paramter in the `open()` function.
  - Write Mode will overwrite the existing file.
- To open a file in appending mode you pass the `'a'` argument as the second paramter in the `open()` function.
  - Append Mode will append at the end of the existing file.
- Both `'w'` and `'a'` will create the file if the file does not already exist.
```python
# open() Example
helloFile = open('C:\\Users\\tylerhardy\\hello.txt')
helloContent = helloFile.read()
print(helloFile)
print(helloContent)

# Answer
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\tylerhardy\\hello.txt'
```
### `read()` Method
- Returns the contents stored in the file as a string.
```python
# read() Example
helloFile = open('C:\\Users\\tylerhardy\\hello.txt', 'r')
helloContent = helloFile.read()
print(helloContent)

# Answer
Hello World!
```
### `readline()` Method
- Returns a list of string values from the file.
```python
# readline() Example
sonnetFile = open('C:\\Users\\tylerhardy\\sonnet29.txt')
sonnetContent = sonnetFile.readlines()
print(sonnetContent)

# Answer
["When, in disgrace with fortune and men's eyes,\n", 'I all alone beweep my outcast state,\n', 'And trouble deaf heaven with my bootless cries,\n', 'And look upon myself and curse my fate,']

```
### `write()` Method
- 
```python
# write() Example
baconFile = open('bacon.txt', 'w')
baconFile.write('Hello world!\n')

baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')

baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)

# Answer
Hello world!
Bacon is not a vegetable.
```

## Saving Variables with the Shelve Module
### `shelve` Module
- Allows you to save variables to binary shelf files.
- Allows you to add *Save* and *Open* features to your program.
- Stores data in a dictionary
- Does not have to be opened in read or write mode--it can do both once opened.
```python
# shelve Example
import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()

shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

# Answer
<class 'shelve.DbfilenameShelf'>
['Zophie', 'Pooka', 'Simon']
['cats']
[['Zophie', 'Pooka', 'Simon']]
```

## Saving Variables with the `pprint.pformat()` Function
### `pprint.pformat()` Function
- The `pprint.pprint()` function will 'pretty print' the contents of a list or dictionary to the screen.
- Returns the the text as a string instead of printing it.
```python
# pprint.pformat() Example
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()
```
