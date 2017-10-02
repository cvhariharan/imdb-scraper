import requests,sys
from selenium import webdriver

imdb_url = sys.argv[1]
html_source = requests.get(imdb_url).text

def snippet(start,end,html_source,start_offset):
    snippet_index_start = html_source.find(start)
    snippet_index_end = html_source.find(end,snippet_index_start)
    return html_source[snippet_index_start+start_offset:snippet_index_end]

#Find the poster division and isolate it from the rest of the html source
poster_content = snippet("<div class=\"poster\">","</div>",html_source,0)
print(poster_content)

#Find the url that points to the image
imgurl = snippet("<a href=",">",poster_content,len("<a href=")).replace("\n","").replace("\"","")
imgurl = "http://imdb.com"+imgurl

browser = webdriver.Chrome("D:\chromedriver")
browser.get(imgurl)
new_poster_content = browser.page_source
new_imgurl = snippet("<img class=\"pswp__img\" src=","style",new_poster_content,len("<img class=\"pswp__img\" src=")).replace("\n","").replace("\"","")
print(new_imgurl)
