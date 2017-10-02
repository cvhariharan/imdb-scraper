import imdb_scraper,requests
movie_name = input("Name of the Movie or TV Series: ")
imdb = imdb_scraper.website(movie_name,True)
plot = imdb.plot()
rating = imdb.rating()
title = imdb.title()
imgurl = imdb.poster()
#Save the poster
image = open(title+".jpg","wb")
image.write(requests.get(imgurl).content)
image.close()
review = imdb.reviews()
print("Title: "+title+"\n"+"Rating: "+rating+"\n"+"Plot: "+plot+"\n"+"Poster: "+imgurl+"\n"+"Review: "+review)
