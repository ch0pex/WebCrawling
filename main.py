import openpyxl
import requests
import time 
import threading

from bs4 import BeautifulSoup
from film import Film

EXCEL_PATH = "MovieGenreIGC_v3.xlsx"
JSON_PATH = "data.json"

def main(start, end):
     for id, url in enumerate(sheet.iter_rows(min_row=start, max_col=end, max_row = 20,values_only=True)):
        film = Film(url[1], id)
        print(film)
        



if __name__ == "__main__":
    start = time.time()
    wb = openpyxl.load_workbook(EXCEL_PATH)
    sheet = wb.active
    thread1 = threading.Thread(target=main, args=(2, 20))
    thread1.start()
    
    #print(time.time() - start)


       
    


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
                            if "Director" in element.text:cle
                                aux_list = element.findAll("a")
                                directors = [z.text for z in aux_list]
                                break,
            "writers" : lista = imdb.find("table", {"class" :"simpleTable spFirst writers_list"}).findAll("td", {"class":"name"})
                        writters = [z.text.strip() for z in lista]
            "actors" : lista = imdb.find("table", {"class" :"cast_list"}).findAll("span", {"itemprop":"name"})
                        actors = [z.text for z in lista]
        }
        
        print(film)
        
        
        
        
        
"""