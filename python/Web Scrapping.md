# Web Scrapping
## Python Modules for Scrapping
- webbrowser: Comes with Python and opens a browser to a specific page.
- Requests: Downloads files and webpages from the Internet.
- Beautiful Soup: Parses HTML
- Selenium: Launches and controls a web broswer.

## Downloading Files from the Web with Requests Module
The request module is a third party module that will have to be downloaded and installed, `pip install requests`.

The `requests.get()` function takes a string of a URL to download. Using the `requests.get()` function will return a `Response` object.

```py
import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt', verify=False)
print(type(res))
print(res.status_code)
print(res.status_code ==  requests.codes.ok)
print(len(res.text))
print(res.text[:250])
```

### Checking for Errors
```py
import requests
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: {0}'.format(exc))
```

### Saving Files to the HDD
```py
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt', verify=False)
try:
    res.raise_for_status()
    playFile = open('RomeoAndJuliet.txt','wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    playFile.close()
except Exception as exc:
    print('There was a problem: {0}'.format(exc))
```
1. Call `requests.get()` to download the file.
2. Call `open()` with `'wb'` to create a new file in the **write binary** mode.
3. Loop over the `Response` object's `iter_content()` method.
4. Call `write()` on each iteration to write the content to the file.
5. Call `close()` to close the file.

## Beautiful Soup Module
To install beautiful soup use the following pip command: `pip install beautifulsoup4`


| Selector passed to the select() method | Will match... |
|-|-|
| soup.select('div') | All elements named `<div>` |
| soup.select('#author') | The element with an id attribute of author |
| soup.select('.notice') | All elements that use a CSS class attribute named notice |
| soup.select('div span') | All elements named `<span>` that are within an element named `<div>` |
| soup.select('div > span') | All elements named `<span>` that are directly within an element named `<div>`, with no other element in between |
| soup.select('input[name]') | All elements named `<input>` that have a name attribute with any value |
| soup.select('input[type="button"]') | All elements named `<input>` that have an attribute named type with value button |

```py
import bs4,sys, os

print(os.getcwd())
root_dir = os.getcwd()
os.chdir('{0}\\personalwiki\\python\\'.format(root_dir))
print(os.getcwd(), end='\n\n')

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')
print(type(elems))
print(elems)
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)
```

