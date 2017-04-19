import re
phoneNumRegex = re.compile(r'(((\()?\d{3}(\))?)(-|.))?(\d{3}(-|.)\d{4})') 
matchObject = phoneNumRegex.search('My number is (415)-555-4242.')
print(matchObject.group(1))

xmasRegex = re.compile(r'\w+\s\w+')
var = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(var)

"""
8016249401
(801)6249401
801.624.9401
(801).624.9401
801-624-9401
(801)-624-9401
18016249401
1(801)6249401
1801.624.9401
1(801).624.9401
1801-624-9401
1(801)-624-9401
1.8016249401
1.801.624.9401
1.(801).624.9401
1-801-624-9401
1-(801)-624-9401
624-9401
624.9401
6249401
918016249401
18016249401
12345678910111213
"""
agentNamesRegex = re.compile(r'Agent (\w)\w*')
var = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(var)

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

print(phoneRegex)