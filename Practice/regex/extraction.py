import re
text = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_url = pattern.sub(r'\2\3', text)
print(subbed_url)
