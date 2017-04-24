# Organizing Files
## `shutil` Module
- The `shutil` (or shell utilities) module has functions to let you copy, move, rename, and delete files in your Python programs.
- Import: `import shutil`

## Copying Files and Folders
- `shutil` module provides functions for copying files and folders
- `shutil.copy(source, destination)` will copy the file at the path `source` to the folder at the path `destination`.
  - It returns a string of the path of the copied folder.
- `shutil.copytree(source, destination)` will copy the folder at the path `source`, along with all of its files and subfolders to the folder at the path `destination`.
  - It returns a string of the path of the copied folder.

## Moving and Renaming Files and Folders
- `shutil.move(source, destination)` will move the file or folder at the path `source` to the path `destination` and will return a string of the absolute path of the new location.
- The `destination` path can also specify a filename to be renamed.
- The folders in the  `destination` path must exist or else Python will throw an exception.

## Permanently Deleting Files and Folders
- To delete a single file or a single empty folder you use `os` module.
- To delete a folder and all of its contents you use `shutil` module.
- `os.unlink(path)` wll delete the file at `path`.
- `os.rmdir(path)` will delete the folder at `path` as long as it is empty of files and folders.
- `shutil.rmtree(path)` will remove the folder at `path` and all files and folders it contains.

## Safe Deletes with the `send2trash` Module
- The `send2trash` module is a thirdparty module that will send folders and files to your computer's trash or recycle bin.
- Installation: `pip install send2trash`

## Walking a Directory Tree
- The `os.walk()` function takes a single string value (the path of a folder) and returns three values:
  1. A string of the current folder's name.
  2. A list of strings of the folders in the current folder.
  3. A list of strings of the files in the current folder.

```python
# os.walk() Example
import os

for folderName, subfolders, filenames in os.walk('C:\\Users\\tylerhardy\\Downloads\\'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

    print('')
```

## Compressing Files with the `zipfile` Module
### Reading Zip Files
- To read the contents of a ZIP file, you must first create a `ZipFile` object.
- `ZipFile` objects are conceptually simialr to the `File` objects.
- To create a `ZipFile` object call the `zipfile.ZipFile()` function passing a string of the `.zip` file's filename.
- A `ZipFile` object has a `namelist()` method that returns a list of strings for all the files and folders conatined in the ZIP file.
  - These strings can be passed to the `getinfo()` `ZipFile` method to return a `ZipInfo` object about that particular file.
  - `ZipInfo` objects have their own attributes such as `file_size` and `compress_size` in bytes.

### Extracting from ZIP Files
- The `extractall()` method for `ZipFile` objects extracts all the files and folders from a ZIP file into the current working directory.
- A foldername can be passed to `extractall()` to have it extract the files into a folder other than the current working directory.
  - If the folder passed to the `extractall()` method does not exist, it will be created.
- The `extract()` method for `ZipFile` objects will extract a single file from the ZIP file.
  - The string passed to `extract()` must match one of the strings in the list returned by `namelist()`.

### Creating and Adding to ZIP Files
- In order to create ZIP files you must open the `ZipFile` object in write mode by passing 'w' as the second argument.
  - Or 'a' to appened.
- When you pass a path to the `write()` method of a `ZipFile` object Python will compress the file at that path and add it into the ZIP file.
- The `write()` method's first argument is a string of the filename to add.
- The second argument is the compression type parameter (`zipfile.ZIP_DEFLATED`))

