import openpyxl
import requests
import time 
import threading
import json

from bs4 import BeautifulSoup
from film import Film

EXCEL_PATH = "MovieGenreIGC_v3.xlsx"
JSON_PATH = "data.json"

def main(start, end, threadid):
     for id, url in enumerate(sheet.iter_rows(min_row=start, max_row = end,values_only=True)):
        film = Film(url[1], id)
        print(film.title)
        index, content = film.to_dict()
        with open(f"Data/data{threadid}.json", "a", encoding="utf-8") as f:
            json.dump(index, f, ensure_ascii=False)
            f.write("\n")
            json.dump(content, f, ensure_ascii=False)
            f.write("\n")   
           
            

            
if __name__ == "__main__":
    start = time.time()
    wb = openpyxl.load_workbook(EXCEL_PATH)
    sheet = wb.active

    
    thread1 = threading.Thread(target=main, args=(2, 20,1))
    thread2 = threading.Thread(target=main, args=(21, 40,2))
    thread3 = threading.Thread(target=main, args=(41, 60,3))
    thread4 = threading.Thread(target=main, args=(61, 80,4))
    thread5 = threading.Thread(target=main, args=(81, 100,5))
    thread6 = threading.Thread(target=main, args=(101, 120,6))
    thread7 = threading.Thread(target=main, args=(121, 140,7))
    thread8 = threading.Thread(target=main, args=(141, 160,8))


    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    

    print(time.time() - start)
