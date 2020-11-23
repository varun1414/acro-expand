import bs4
import requests
import re
import json
from collections import OrderedDict 

def lut(acr,ext):
    arr=dict(zip(acr,ext))
    return arr

def jdump(dictionary):
    with open("main.json", "w") as outfile:  
        json.dump(dictionary, outfile,indent=1) 

def sep_upper(arr):
    extract = bs4.BeautifulSoup(requests.get('https://www.verywellfamily.com/the-secret-language-of-teens-100-social-media-acronyms-2609651').content, 'html.parser')
    elems = extract.select('ol')
    elems=str(elems)
    elems=elems.replace('<strong>','@@')
   
    un=re.sub(r'<.*?>',' ',elems)
    un=un.replace(u'\xa0',u' ')
    un=un.replace('[ \n ','')
    un=un[1:]
    
    un=un.strip()
    

    un=un.split('@@')
    
    
    acr=[]
    ext=[]
    temp=[]
    for i in un:
        if i.find('-')> 0:
            temp.append(i)
     
       
        
    # print(temp)
    for i in temp:
        l=i.split('-')
        acr.append(l[0].lower().strip())
        ext.append(l[1].lower().strip())
    
    
    
    for i in un:
        if i.find('-')==-1:
            acr.append(i.lower().strip())
        if i.find('-')==0:
          
            i=i.replace('-','')
            ext.append(i.lower().strip())

    
  
    for key,i in enumerate(acr):
        if i.find('  –')!=-1:
            l=i.split('  –')
            
            ext.insert(key,l[1])
            acr[key]=l[0]

    lut_arr=lut(acr,ext)
    jdump(OrderedDict(sorted(lut_arr.items())))
