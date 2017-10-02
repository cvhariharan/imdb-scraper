import requests,sys

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
imgurl = snippet("src","itemprop",poster_content,len("src=")).replace("\n","").replace("\"","")

#Change the image dimensions
imgurl=imgurl.replace("UX182_CR0,0,182,268_AL__QL50","UX400_CR0,0,400,585_AL__QL50") #Replace with @@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg to directly get hd posters

#Open a BINARY file and write the contents to it
image = open(imdb_url.split("/")[4]+".jpg","wb")
image_data = requests.get(imgurl).content
image.write(image_data)
image.close()
print(imgurl)
