import bs4
import requests
import re
def sep_upper(arr):
    extract = bs4.BeautifulSoup(requests.get('https://www.verywellfamily.com/the-secret-language-of-teens-100-social-media-acronyms-2609651').content, 'html.parser')
    elems = extract.select('ol')
    elems=str(elems)
    elems=elems.replace('<strong>','@@')
   
    un=re.sub(r'<.*?>',' ',elems)
    un=un.replace(u'\xa0',u' ')
    un=un.strip()
    # print(un)

    un=un.split('@@')
    # print(un)
    # un=un.replace('GAL  – Get a life ','GAL–Get a life')
    # un=un.replace('LMIRL  – Let’s meet in real life ','LMIRL–Let’s meet in real life')

    
    acr=[]
    ext=[]
    temp=[]
    for i in un:
        if i.find('-')> 0:
            temp.append(i)
     
       
        
    # print(temp)
    for i in temp:
        l=i.split('-')
        acr.append(l[0])
        ext.append(l[1])
    
    
    # print(acr)
    for i in un:
        if i.find('-')==-1:
            acr.append(i)
        if i.find('-')==0:
            #i=" "+i[1:]
            ext.append(i)
    # print(acr)
    # for i in ext:
    #     if i.find('-')>0:
    #         k=i.split('-')
    #         ext.append(k[0])
    #         ext.append(k[1])
    
    acr.remove('[ \n ')
    for key,i in enumerate(acr):
        if i.find('  –')!=-1:
            l=i.split('  –')
            # print(l)
            ext.insert(key,l[1])
            acr[key]=l[0]
    for i,value in enumerate(acr):
        try:
            print(value+" "+ext[i])
        except:
            print(value+" "+" no")