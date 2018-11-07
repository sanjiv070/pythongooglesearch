import requests, sys, webbrowser, bs4

res= requests.get('https://www.google.com/search? q='+''.join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
linkElements =soup.select('.r a')
linkToOpen=min(5,len(linkElements))
for i in range(linkToOpen):
    webbrowser.open('https://www.google.com'+linkElemnents[i].get('href'))
     

