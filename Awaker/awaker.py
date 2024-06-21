import requests
import aiohttp
import asyncio
from .sendAleartEmail import sendEmailAsAleart

async def awaker_list(text_file_name):


    store_array = []
    
    with open(text_file_name,'r',encoding='utf-8') as txt:
        store_array = [line.strip() for line in txt.readlines()]
        
    print(store_array)

    # while store_array:
    while store_array:
        # print(store_array)
        for url in store_array:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as response:
                        if not response.status==200:
                            sent = await sendEmailAsAleart(email_text)
                            store_array.remove(url)
                        else:            
                            print(f"Status for {url}: {response.status}")
            except Exception as e:
                email_text = f"Status for {url}: {response.status}"
                sent = await sendEmailAsAleart(email_text)
                print(sent)
                print(f"May be Shutdown: {url} {e}")
        
        print('Sleeping for 35 seconds')
        await asyncio.sleep(35)
        
        # exit()
        
    EXIT_TEXT_EMAIL = f"i'm not working !!!, good bie...."
    sent = await sendEmailAsAleart(EXIT_TEXT_EMAIL,'Aleart !!! Sleeping Bie')
# awaker_list()