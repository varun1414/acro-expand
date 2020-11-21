import bs4
import requests
import re
extract = bs4.BeautifulSoup(requests.get('https://www.verywellfamily.com/the-secret-language-of-teens-100-social-media-acronyms-2609651').content, 'html.parser')
elems = extract.select('#mntl-sc-block_1-0-9')

unfiltered=elems[0].getText()
unfiltered=re.sub(r'\\x | \xa0 | / | \n','',unfiltered)

un_array=unfiltered.split('-')
print(un_array)