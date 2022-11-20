import re

text = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
# match = pattern.finditer(text)
# for matched in match:
#     print(matched)

with open("data.txt", 'r') as f:
    file = f.read()
    match = pattern.finditer(file)
    for matched in match:
        print(matched)