import pyperclip, re

phoneReg = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    )''', re.VERBOSE)

emailReg = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @                   
    [a-zA-Z0-9.-]+     
    (\.[a-zA-Z]{2,4})   
    )''', re.VERBOSE)

text = str(pyperclip.paste())
results = []

for result in phoneReg.findall(text):
    num = '-'.join([result[1], result[3], result[5]])
    results.append(num)

for result in emailReg.findall(text):
    results.append(result[0])

if len(results) > 0:
    pyperclip.copy('\n'.join(results))
    print('Copied to clipboard:')
    print('\n'.join(results))
else:
    print('No phone numbers or email addresses found.')
