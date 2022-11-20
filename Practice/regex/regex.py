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
bat 
cat mat pat

CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net

https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# pattern = re.compile(r'(Mr|Mrs|Ms)\.?\s[A-Z]\w*') #grabbing Mr Mrs Ms ("name")
# pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)') #grabbing email address
pattern = re.compile(r'https?://(www\.)?(\w+)+(\.\w+)')  # grabbing domain name
match = pattern.finditer(text)
for matched in match:
    print(matched.group(0))

# with open("data.txt", 'r') as f:
#     file = f.read()
#     match = pattern.finditer(file)
#     for matched in match:
#         print(matched)
