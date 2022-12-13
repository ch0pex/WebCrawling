import openpyxl
import time 
import threading
import json


from film import Film

EXCEL_PATH = "MovieGenreIGC_v3.xlsx"
JSON_PATH = "data.json"

NUM_OF_ROWS = 100
NUM_OF_THREADS = 16
START = 0

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
        with open(f"Data/data{i}.json", "a", encoding="utf-8") as f:
            data = f.read()
        with open(JSON_PATH, "a", encoding="utf-8") as f:
            f.write(data)
    

    print(time.time() - start)