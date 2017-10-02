import requests,sys

imdb_url = sys.argv[1]
html_source = requests.get(imdb_url).text

#Find the poster division and isolate it from the rest of the html source
poster_index_start = html_source.find("<div class=\"poster\"")
after_poster_content = html_source[poster_index_start:]
poster_index_end = after_poster_content.find("</div>")

#Find the url that points to the image
poster_content = after_poster_content[:poster_index_end]
src_tag_index = poster_content.find("src")
src_tag_end = poster_content.find("itemprop")
imgurl = poster_content[src_tag_index+4:src_tag_end].replace("\n","").replace("\"","")

#Change the image dimensions
imgurl=imgurl.replace("UX182_CR0,0,182,268_AL__QL50","UX400_CR0,0,400,585_AL__QL50")

#Open a BINARY file and write the contents to it
image = open(imdb_url.split("/")[4]+".jpg","wb")
image_data = requests.get(imgurl).content
image.write(image_data)
image.close()
print(imgurl)
