# Common Error Messages
## **SyntaxError: EOL while scanning string literal**
Probably forgot the final single quote character at the end of the string.
## **TypeError: must be str, not int**
Check the **Data Type** of the variables.

```py
traceback.format_exc()
```
- Want information from an exception's traceback but also want an `except` stateatment.

# Assertion

```py
podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
```

# loggin
```py
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -%(levelname)s - %(message)s')
logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')
logging.disable(logging.CRITICAL)
logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')
```
```shell
2017-05-08 11:54:42,559 -DEBUG - Some debugging details.
2017-05-08 11:54:42,559 -INFO - The logging module is working.
2017-05-08 11:54:42,559 -WARNING - An error message is about to be logged.
2017-05-08 11:54:42,560 -ERROR - An error has occurred.
2017-05-08 11:54:42,560 -CRITICAL - The program is unable to recover!
```

# Logging to a File
```py
import logging
logging.basicConfig()
```