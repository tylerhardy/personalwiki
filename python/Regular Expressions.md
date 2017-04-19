## Review
- The `?` matches zero or one of the preceding group.
- The `*` matches zero or more of the preceding group.
- The `+` matches one or more of the preceding group.
- The `{n}` matches exactly n of the preceding group.
- The `{n,}` matches `n` or more of the preceding group.
- The `{,m}` matches `0` to `m` of the preceding group.
- The `{n,m}` matches at least `n` and at most `m` of the preceding group.
- `{n,m}?` or `*?` or `+?` performs a nongreedy match of the preceding group.
- `^spam` means the string must begin with `spam`.
- `spam$` means the string must end with `spam`.
- The `.` matches any character, except newline characters.
- `\d`, `\w`, and `\s` match a digit, word, or space character, respectively.
- `\D`, `\W`, and `\S` match anything except a digit, word, or space character, respectively.
- `[abc]` matches any character between the brackets (such as a, b, or c).
- `[^abc]` matches any character that isn’t between the brackets.

# Regular Expressions
- The `\d` in regex stands fopr digit character (`0-9`)
- The `{n}` after a pattern multiplies the pattern `n` times..
  - Example: `\d{3}-\d{3}-\d{3}` will match a phone number pattern.
## Creating Regex Objects
- Regex functions are in the the `re` module.
  - `import re`
- Passing a string value representing your regular expression to `re.compile()` retunrs a `regex` pattern object (a `regex` object).
```python
# regex Example
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex)

# Answer
re.compile('\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d')
```
## Matching Regex Objects
- The `Regex` object `search()` method searches the string it is passed for any mathces to the regex.
- The `search()` method will return `None` if the regex pattern is not found in the string.
- The `search()` method will return a `Match` object if the regex pattern is found in the string.
- The `Match` objects have a `group()` method that will return the actual matched text from the searched string.
```python
# regex Example
import re
# The desired pattern is passed to re.compile which stores the resulting Regex object in the variable phonNumRegex.
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d\-\d\d\d\d') 
# The method search() is called on phoneNumRegex and passes the string (string argument ('string')) we want to search for a match
# Theresult of the search gets stored in the variable matchObject
matchObject = phoneNumRegex.search('My number is 415-555-4242.')
# Knowing that matchObject contains a Match object and not the null value None, we can call group() on matchObject to return the match
print('Phone number found: ' + matchObject.group())

# Answer
Phone number found: 415-555-4242
```
## Grouping with Parentheses
- Adding parentheses will create *groups* in regex.
  - `(\d\d\d)-(\d\d\d-\d\d\d\d)`
- The `group()` match object method can be used to grab the matching text from just one group.
```python
# regex Example
import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d\-\d\d\d\d)') 
matchObject = phoneNumRegex.search('My number is 415-555-4242.')
print(matchObject.group(1))
print(matchObject.group(2))
print(matchObject.group(0))
print(matchObject.group())

# Answer
415
555-4242
415-555-4242
415-555-4242
```
- The `groups()` method (not to be confused with the singular `group()` method) can be used to retrieve all the groups at once.
- The `groups()` method returns a tuple of multiple values.
  - The use of the multiple-assignment trick will assign each value to a separate variable.
```python
# regex Example
import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d\-\d\d\d\d)') 
matchObject = phoneNumRegex.search('My number is 415-555-4242.')
print(matchObject.groups())
areaCode, mainNumber = matchObject.groups()
print(areaCode)
print(mainNumber)

# Answer
('415', '555-4242')
415
555-4242
```
- To match a parenthesis in text using regex an escape character is needed.
- The regex escape is the backslash `\`.
  - The `\(` and `\)` escape characters in the raw string passed to `re.compile()` will match actual paranthesis characters.
```python
# regex Example
import re
phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d\-\d\d\d\d)') 
matchObject = phoneNumRegex.search('My number is (415)-555-4242.')
print(matchObject.group(1))
print(matchObject.group(2))

# Answer
(415)
555-4242
```
## Matching Multiple Groups with the Pipe
- The `|` character is called a *pipe*.
- It can be used anywhere you want to match **one** of many **expressions**.
  - When both values are found in the searched string the first occurrence of matching text will be returned as the `Match` object.
```python
# regex Example
import re
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))
batRegex2 = re.compile(r'Bat(wo)?man')
mo2 = batRegex2.search('The Adventures of Batman')
mo3 = batRegex2.search('The Adventures of Batwoman')
print(mo2.group())
print(mo3.group())

# Answer
Batmobile
mobile
Batman
Batwoman
```

## Optional Matching with the Question Mark
- The `?` character flags the group that preceds it as an optional part of the pattern.
  - The `?` is saying "Match zero or one of the group preceding this question mark".

## Matching Zero or More with the Star
- The `*` means 'match zero or more' of the group that precedes it, this can occur any number of times in the text.

## Matching One or More with the Plus
- The `+` means 'match one ore more' of the group that precedes it, this must occur at least once.

## Matching Specific Repetitions with Curly Brackets
- If you have a group that you want to repeat a specific number of times, follow the group in your regex with a number in curly brackets.
- You can specify a range between the curly brackets `{minimum,maximum}`
  - The range min and max can be omitted to indicate unlimited bounds.

## Greedy and Nongreedy Matching
- Python's regular expressions are greedy by default.
  - In ambiguous situations they will match the longest srting possible.
- The non-greedy version, shortest string possible, has the closing curly bracket followed by a question mark `(ha){3,5}?`
- **Note**: the question mark can have two meanings in regular expressions:
  - Declaring a nongreedy match or flagging an optional group. 
  - These meanings are entirely unrelated.

## The Findall() Method
- The `search()` method will return a `Match` object of the first matched text in the searched string.
- The `findall()` method will return the strings of every match in the searched string.
  - The returned `Match` object will be a list of strings as long as there are no groups in the regular expression.
  - If there are groups in the regular expression then `findall()` will return `Match` object as a list of `tuples`.

## Character Classes

| Shorthand Character Class | Represents |
|---------------------------|------------|
| `\d` | Any numeric digit from `0` to `9` |
| `\D` | Any character that is **not** a numeric digit from `0` to `9` |
| `\w` | Any letter, numeric digit, or the underscore character |
| `\W` | Any character that is **not** a letter, numeric digit, or the underscore character |
| `\s` | Any space, tab, or newline character. |
| `\S` | Any character that is **note** a space, tab, or newline |

- The regex (`r'\d+\s\w+'`) will match text that has one or more numeric digits (`\d+`), followed by a whitespace character (`\s`), followed by one or more letter/digit/underscore characters (`\w+`)
  - `[number_chars+|space_chars|string_chars+]` --> `'42 stars'`

## Making Your Own Character Classes
- You can define your own character class using square brackets.
```python
# regex Example
import re
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food. BABY FOOD.'))

# Answer
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
```
- You can include ranges of letters or numbers by using a hyphen (`-`).
  - `[a-zA-Z0-9]` --> will match all lowercase letters, uppercase letters, and numbers.
- Inside the square brackets, the normal regular expression symbols are not interpreted as such.
  - You do not need to escape the `.`, `*`, `?`, or `()` characters with a preceding backslash (`\`).
- The caret character (`^`) when placed after the character's class opening brackets (`[`) allows you to make a *negative character class*.
  - A negative character class will match all the characters that are not in the character class.
  - `[^aeiouAEIOU]` --> will match all characters that isn't a vowel.

## The Caret and Dollar Sign Characters
- The caret symbol (`^`) when placed at the start of a regex will indicate that a match *must* occur at the **beginning** of the searched text.
- The dollar symbol (`$`) when placed at the end of a regex will indicate the string *must* **end** with this regex pattern.
```
^(\d)?[-|\.]?(((\()?\d{3}(\))?)[-|\.]?)?(\d{3}[-|\.]?\d{4})$
^(\d)?(\s|-|\.)?(((\()?\d{3}(\))?)(\s|-|\.)?)?(\d{3}(\s|-|\.)?\d{4})$
^(\d)?(\s|-|\.)?((\(\d{3}\))|(\d{3}))?(\s|-|\.)?(\d{3}(\s|-|\.)?\d{4})$
```

## The Wildcard Character
- The `.` (or *dot*) character in a regular expression is called a *wildcard* and will match any character except for a newline.
- The dot star (`.*`) will match everything and anything except a new line.
- To match in the non-greedy way use `.*?`.

## Matching Newlines with the Dot Character
- The dot-star will match everything except a newline.
- Passing the `re.DOTALL` as the second argument to the `re.compile()` method you can make the dot character match **all characters** including the newline character.
```python
newlineRegex = re.compile('.*', re.DOTALL)
```

## Review
- The `?` matches zero or one of the preceding group.
- The `*` matches zero or more of the preceding group.
- The `+` matches one or more of the preceding group.
- The `{n}` matches exactly n of the preceding group.
- The `{n,}` matches `n` or more of the preceding group.
- The `{,m}` matches `0` to `m` of the preceding group.
- The `{n,m}` matches at least `n` and at most `m` of the preceding group.
- `{n,m}?` or `*?` or `+?` performs a nongreedy match of the preceding group.
- `^spam` means the string must begin with `spam`.
- `spam$` means the string must end with `spam`.
- The `.` matches any character, except newline characters.
- `\d`, `\w`, and `\s` match a digit, word, or space character, respectively.
- `\D`, `\W`, and `\S` match anything except a digit, word, or space character, respectively.
- `[abc]` matches any character between the brackets (such as a, b, or c).
- `[^abc]` matches any character that isn’t between the brackets.

## Case-Insensitive Matching
- To match strings without any upper or lower-case pass the `re.IGNORECASE` or `re.I` as a second argument to `re.compile()`

## Substituting Strings with the `sub()` Method
- The `sub()` method returns a string with substitutions applied.
  - The `sub()` method takes two parameters, the first being the word you wish to substitute, and the second being the string to manipulate.
```python
# regex Example
namesRegex = re.compile(r'Agent \w+')
var = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(var)

# Answer
CENSORED gave the secret documents to CENSORED.
```
- Matched test can be part of the substitution.
- In the first argument to sub(), you can type \1, \2, \3, and so on, to mean "Enter the text of group 1, 2, 3, and so on, in the substitution."
```python
# regex Example
agentNamesRegex = re.compile(r'Agent (\w)\w*')
var = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(var)

# Answer
A**** told C**** that E**** knew B**** was a double agent.
```

## Managing Complex Regexes
- Matching complicated text patterns might require long, convoluted regular expressions.
- You can mitigate this by telling the `re.compile()` function to ignore whitespace and comments inside the regular expression string. 
- This *verbose mode* can be enabled by passing the variable `re.VERBOSE` as the second argument to `re.compile()`.
```python
# regex Example
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
```

## Combining `re.IGNORECASE`, `re.DOTALL`, and `re.VERBOSE`
- The `re.compile()` method only takes a single value as its second argument.
- To get around this restriction you combin the `re.IGNORECASE`, `re.DOTALL`, and `re.VERBOSE` variables using the pipe character (`|`).
  - In this context it is known as the *bitwise or* operator
