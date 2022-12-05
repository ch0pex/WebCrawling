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
        self.director = self.__get_director()
        self.writers = self.__get_writers()
        self.actors = self.__get_actor()
        self.genres = None
        self.country = None
        self.lenguages = None
        self.runtime = None
        self.summary = None
        self.sinopsis = None 
        self.__get_storyline()
        self.__get_sinopsis()
     
    
     
     
    def __str__(self):
        index = {"index":{"_index":"imdb","_type":"film","_id":self.id}}
        content = {}
        for key, value in self.__dict__.items():
            if value is not None and key != "id" and "__" not in key:
                content[key] = value        
        return str(index) +"\n"+ str(content)  


    def __get_title(self):
        return  self.__reference.select("title")[0].text[:-25].split(" (")[0]

    def __get_year(self):
        return self.__reference.select("title")[0].text[:-25].split(" (")[1]
    
    def __get_director(self): 
        crew = self.__reference.findAll("div", {"class":"titlereference-overview-section"})
        for element in crew: 
            if "Director" in element.text:
                aux_list = element.findAll("a")
                return [z.text for z in aux_list]
        return None

    def __get_writers(self): 
        elements = self.__reference.find("table", {"class" :"simpleTable spFirst writers_list"}).findAll("td", {"class":"name"})
        return [z.text.strip() for z in elements]
    
    def __get_actor(self): 
        elements = self.__reference.find("table", {"class" :"cast_list"}).findAll("span", {"itemprop":"name"})
        return [z.text for z in elements]
        

    def __get_storyline(self): 
        storyline = self.__reference.find_all("td", {"class":"ipl-zebra-list__label"})
        for element in storyline: 
            if element.text == "Genres":
                ahrefs = element.find_next_sibling("td").find_all("a")         
                self.genres = [ahref.text for ahref in ahrefs]       
            
            elif element.text == "Country": 
                self.country = element.find_next_sibling("td").find("a").text
                        
            elif element.text == "Language":
                ahrefs = element.find_next_sibling("td").find_all("a")         
                self.lenguages = [ahref.text for ahref in ahrefs][1:]
            
            elif element.text == "Runtime":
                self.runtime = element.find_next_sibling("td").find("li").text.strip()
    
    def __get_sinopsis(self):
        content = self.__sinopsis.find("ul", {"id":"plot-synopsis-content"})
        if content.find("li").get_attribute_list("id")[0] != "no-synopsis-content":
            self.sinopsis = content.text
        else:
            content = self.__sinopsis.find("ul", {"id":"plot-summaries-content"})
            elems = content.findAll("li")
            self.summary = [z.text.strip() for z in elems]
            # COntemplar crear solo un atributo y listas como texto concatenado

    def __get_rating(self): ...
