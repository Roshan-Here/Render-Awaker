import requests
import time

def awaker_list():

    text_file_name = '../siteslists.txt'
    store_array = []
    
    with open(text_file_name,'r',encoding='utf-8') as txt:
        store_array = [line.strip() for line in txt.readlines()]
        
    print(store_array)

    # while store_array:
    while True:
        # print(store_array)
        for url in store_array:
            try:            
                req = requests.get(url)
                print(req.status_code)
            except Exception as e:
                print(f'May be Stutdown : {url} {e}')
        print('sleeping for 35 secounds')
        time.sleep(35)
        
        exit()

awaker_list()