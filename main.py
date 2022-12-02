import openpyxl
import requests
from bs4 import BeautifulSoup


EXCEL_PATH = "MovieGenreIGC_v3.xlsx"
JSON_PATH = "data.json"

def get_storyline(): 
    storyline = imdb.find_all("td", {"class":"ipl-zebra-list__label"})
    for element in storyline: 
        if element.text == "Plot Summary":
            plot_summary = element.find_next_sibling("td").find("p").text.strip()
            
        elif element.text == "Genres":
            ahrefs = element.find_next_sibling("td").find_all("a")         
            genres = [ahref.text for ahref in ahrefs]       
        
        elif element.text == "Country": 
            country = element.find_next_sibling("td").find("a").text
                    
        elif element.text == "Language":
            ahrefs = element.find_next_sibling("td").find_all("a")         
            lenguages = [ahref.text for ahref in ahrefs][1:]
        
        elif element.text == "Runtime":
            runtime = element.find_next_sibling("td").find("li").text.strip()
    
    print(runtime)




if __name__ == "__main__":
    wb = openpyxl.load_workbook(EXCEL_PATH)
    sheet = wb.active


    for row in sheet.iter_rows(min_row=2, max_col=2, max_row = 20,values_only=True):

        imdb = BeautifulSoup(requests.get(row[1] + "/reference").text , "html.parser")
    
        # get_storyline()
    
        

 
        
        
       
    


"""
        film = {
            "Title": imdb.select("title")[0].text[:-25].split(" (")[0],
            "year": imdb.select("title")[0].text[:-25].split(" (")[1],
            ****HAY MAS STAR RATING****"score": imdb.find("span", {"class" :"ipl-rating-star__rating"}).text,
            "genre": get_storyline,
            "sumary": get_storyline,
            "country": get_storyline,
            "runtime": get_storyline,
            "language": get_storyline,         
            "poster": imdb.find("img", {"alt" :"Poster"}).get_attribute_list("src")[0]
            "director": crew = imdb.findAll("div", {"class":"titlereference-overview-section"})
                        for element in crew: 
                            if "Director" in element.text:
                                aux_list = element.findAll("a")
                                directors = [z.text for z in aux_list]
                                break,
            "writers" : lista = imdb.find("table", {"class" :"simpleTable spFirst writers_list"}).findAll("td", {"class":"name"})
                        writters = [z.text.strip() for z in lista]
            "actors" : lista = imdb.find("table", {"class" :"cast_list"}).findAll("span", {"itemprop":"name"})
                        actors = [z.text for z in lista]
        }
        
        print(film)"""