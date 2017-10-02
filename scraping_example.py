import imdb_scraper,requests

imdb = imdb_scraper.website("http://www.imdb.com/title/tt0944947/?ref_=india_t_glfull")
#imgurl,image_data = imdb.poster()
plot = imdb.plot()
rating = imdb.rating()
title = imdb.title()
imgurl = imdb.poster()
image = open("image.jpg","wb")
image.write(requests.get(imgurl).content)
image.close()
review = imdb.reviews()
print(title+"\n"+rating+"\n"+plot+"\n"+imgurl+"\n"+review)
