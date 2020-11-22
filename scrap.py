import bs4
import requests
import re
from filter import sep_upper

extract = bs4.BeautifulSoup(requests.get('https://www.verywellfamily.com/the-secret-language-of-teens-100-social-media-acronyms-2609651').content, 'html.parser')
elems = extract.select('strong')
# print(elems)
unfiltered=[]
for i in elems:
    unfiltered.append(i.getText())
un_string=" ".join(unfiltered)
un_string=un_string.replace(u'\xa0',u' ')
un_string=un_string.strip()
un_array=un_string.split('-')
# print(un_array)

sep_upper(un_array)
