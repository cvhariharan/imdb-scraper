import imdb_scraper,requests

imdb = imdb_scraper.website("http://www.imdb.com/title/tt3014284/")
#imgurl,image_data = imdb.poster()
plot = imdb.plot()
rating = imdb.rating()
title = imdb.title()
imgurl = imdb.poster()
image = open("image.jpg","wb")
image.write(requests.get(imgurl).content)
image.close()
print(title+"\n"+rating+"\n"+plot+"\n"+imgurl)
