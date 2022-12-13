from bs4 import BeautifulSoup
import requests


class Film: 
    def __init__(self, url, id): 
        self.__reference = BeautifulSoup(requests.get(url + "/reference").text , "html.parser")
        self.__sinopsis = BeautifulSoup(requests.get(url + "/plotsummary").text , "html.parser")

        self.id = id
        self.title = self.__get_title()
        self.rating = self.__get_rating()
        self.year = self.__get_year()
        self.directors = self.__get_directors()
        self.writers = self.__get_writers()
        self.actors = self.__get_actors()
        self.genres = None
        self.country = None
        self.lenguages = None
        self.runtime = None
        self.summary = self.__get_summary()
        self.poster = self.__get_poster()
        self.__get_storyline()
        
     
     
     
    def to_dict(self):
        index = {"index":{"_index":"imdb","_type":"_doc","_id":self.id}}
        content = {}
    
        for key, value in self.__dict__.items():
            if value is not None and key != "id" and "__" not in key:
                content[key] = value 
             
        return index, content 


    def __get_title(self):
        return  self.__reference.select("title")[0].text[:-25].split(" (")[0]
    
    
    def __get_rating(self):
        rate = self.__reference.find("span", {"class" :"ipl-rating-star__rating"})
        if rate is None:
            return None 
        rate_span = rate.find_next_sibling("span")
        if rate_span is None: 
            return None    
        if rate_span.get_attribute_list("class")[0] == "ipl-rating-star__total-votes":
            try: 
                return float(rate.text)
            except ValueError: 
                return None 
        return None


    def __get_year(self):
        try: 
            return int(self.__reference.select("title")[0].text[-29:-25])
        except ValueError: 
            return None
      

    def __get_directors(self): 
        crew = self.__reference.findAll("div", {"class":"titlereference-overview-section"})
        if crew is None:
            return None
        for element in crew: 
            if "Director" in element.text:
                aux_list = element.findAll("a")
                return [z.text for z in aux_list]
        return None

    def __get_writers(self): 
        table = self.__reference.find("table", {"class" :"simpleTable spFirst writers_list"})
        if table is None: 
            return None 
        writers = table.findAll("td", {"class":"name"})
        if writers is None: 
            return None
        return [z.text.strip() for z in writers]
    
    def __get_actors(self): 
        table = self.__reference.find("table", {"class" :"cast_list"})
        if table is None: 
            return None
        actors = table.findAll("span", {"itemprop":"name"})
        if actors is None: 
            return None 
        return [z.text for z in actors]
        

    def __get_storyline(self): 
        storyline = self.__reference.find_all("td", {"class":"ipl-zebra-list__label"})
        if storyline is None:
            return
        for element in storyline:
            if element.text == "Genres":
                next = element.find_next_sibling("td")
                if next is not None:
                    ahrefs = next.find_all("a") 
                if ahrefs is not None:
                    self.genres = [ahref.text for ahref in ahrefs]
            
            elif element.text == "Country":
                next = element.find_next_sibling("td")
                if next is not None: 
                    country = next.find("a")
                if country is not None: 
                    self.country = country.text
                        
            elif element.text == "Language":
                next = element.find_next_sibling("td")
                if next is not None: 
                    lenguages = next.find_all("a")
                    self.lenguages = [ahref.text for ahref in lenguages]
            
            elif element.text == "Runtime":
                next = element.find_next_sibling("td")
                if next is not None: 
                    runtime = next.find("li")
                if runtime is not None:    
                    try: 
                        self.runtime = int(runtime.text.strip()[:-4])
                    except ValueError: 
                        self.runtime = None 
  
    def __get_summary(self):
        content = self.__sinopsis.find("ul", {"id":"plot-synopsis-content"})
        if content is None:
            return None
        content_list = content.find("li")
        if content_list is None:
            return None
        if content_list.get_attribute_list("id")[0] != "no-synopsis-content":
            return content.text
        else:
            content = self.__sinopsis.find("ul", {"id":"plot-summaries-content"})
            if content is None:
                return None
            elems = content.findAll("li")
            if elems is None:
                return None
            return [z.text.strip() for z in elems]
        
    def __get_poster(self):
        poster = self.__reference.find("img", {"alt" :"Poster"})
        if poster is None:
            return None 
        return poster.get_attribute_list("src")[0]