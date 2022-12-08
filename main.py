import openpyxl
import time 
import threading
import json
import os 

from bs4 import BeautifulSoup
from film import Film

EXCEL_PATH = "MovieGenreIGC_v3.xlsx"
JSON_PATH = "data.json"

NUM_OF_ROWS = 30000
NUM_OF_THREADS = 16
START = 10000

counter = 0

def main(start, end, threadid):
    global counter 
    for id, url in enumerate(sheet.iter_rows(min_row=start, max_row = end,values_only=True)):
        counter +=1 
        film = Film(url[1], id + start)
        index, content = film.to_dict()
        with open(f"Data/data{threadid}.json", "a", encoding="utf-8") as f:
            json.dump(index, f, ensure_ascii=False)
            f.write("\n")
            json.dump(content, f, ensure_ascii=False)
            f.write("\n")   
        print(f"{counter} de {NUM_OF_ROWS}")   
        

            
if __name__ == "__main__":
    start = time.time()
    wb = openpyxl.load_workbook(EXCEL_PATH)
    sheet = wb.active

    threads = []
    for i in range (0, NUM_OF_THREADS):
        thread =threads.append(threading.Thread(target=main, args=(int(i*NUM_OF_ROWS/NUM_OF_THREADS + START ), int((i+1)*NUM_OF_ROWS/NUM_OF_THREADS) + START - 1, i)))
        threads[i].start()
       
    for thread in threads:
        thread.join()    

    for i in range (0, NUM_OF_THREADS):
        with open(f"Data/data{i}.json", "r", encoding="utf-8") as f:
            data = f.read()
        with open(JSON_PATH, "a", encoding="utf-8") as f:
            f.write(data)
    

    print(time.time() - start)


       
    


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