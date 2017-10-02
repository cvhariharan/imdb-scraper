import imdb_scraper,requests

imdb = imdb_scraper.website("lego batman",True)
#imgurl,image_data = imdb.poster()
plot = imdb.plot()
rating = imdb.rating()
title = imdb.title()
imgurl = imdb.poster()
image = open(title+".jpg","wb")
image.write(requests.get(imgurl).content)
image.close()
review = imdb.reviews()
print(title+"\n"+rating+"\n"+plot+"\n"+imgurl+"\n"+review)
