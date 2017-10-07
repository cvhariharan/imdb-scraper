import requests,sys
class Scraper:
    def __init__(self,search,toSearch):
        if toSearch:
            self.search_source = requests.get("http://imdb.com/find", params={'q':search}).text
            first_result = self.snippet("<h3 class=\"findSectionHeader\"><a name=\"tt\"></a>Titles</h3>","<img src",self.search_source,len("<h3 class=\"findSectionHeader\"><a name=\"tt\"></a>Titles</h3>"))
            url = self.snippet("<a href=",">",first_result,len("<a href="))
            self.url = "http://imdb.com"+url.replace("\"","") #Remove double-quotes
            print(self.url)
            self.page_source = requests.get(self.url).text
            #print(url)
        else:
            self.url = search
            html_source = requests.get(self.url).text
            self.page_source = html_source

    def title(self):
        #Returns the title of the movie
        title_div = self.snippet("<div class=\"title_wrapper\">","</span>",self.page_source,len("<div class=\"title_wrapper\">"))
        self.title = self.snippet("<h1 itemprop=\"name\" class=\"\">","&nbsp;",title_div,len("<h1 itemprop=\"name\" class=\"\">"))
        return self.title

    def movie_id(self):
        #Returns the imdb id using the url
        self.movie_id = self.url.split("/")[4]
        return self.movie_id

    def poster(self):
        imdb_url = self.url

        #Find the poster division and isolate it from the rest of the html source
        poster_content = self.snippet("<div class=\"poster\">","</div>",self.page_source,0)

        #Find the url that points to the image
        imgurl = self.snippet("src","itemprop",poster_content,len("src=")).replace("\n","").replace("\"","")

        #Change the image dimensions
        self.imgurl=imgurl.replace("@._V1_UX182_CR0,0,182,268_AL__QL50.jpg","@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg") #Replace with @._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg to directly get hd posters

        return self.imgurl #Only returns the image url

    def plot(self):
        #Returns the summarized plot
        plot_div = self.snippet("<div class=\"inline canwrap\" itemprop=\"description\">","</div>",self.page_source,len("<div class=\"inline canwrap\" itemprop=\"description\">"))
        self.plot = self.snippet("<p>","</p>",plot_div,len("<p>"))
        return self.plot

    def rating(self):
        #Returns the imdb rating
        rating_div = self.snippet("<div class=\"ratingValue\">","</div>",self.page_source,len("<div class=\"ratingValue\">"))
        self.rating = self.snippet("<span itemprop=\"ratingValue\">","</span>",rating_div,len("<span itemprop=\"ratingValue\">"))
        return self.rating

    def reviews(self):
        #Returns the first review show on the main page of the movie/series
        self.review = self.snippet("<p itemprop=\"reviewBody\">","</p>",self.page_source,len("<p itemprop=\"reviewBody\">"))
        return self.review

    def snippet(self,start,end,html_source,start_offset):
        snippet_index_start = html_source.find(start)
        snippet_index_end = html_source.find(end,snippet_index_start)
        return html_source[snippet_index_start+start_offset:snippet_index_end]
