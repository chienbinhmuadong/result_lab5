# ВАРИАНТ 6
import requests 
import json
url_base='http://api.steampowered.com'
url_getnews='/ISteamNews/GetNewsforApp/v0002/'
while True:
    try:
       appid=int(input("ввод AppID игры, который вы хотите вернуть: "))
       try:
           number_news=int(input("ввод количества новостей вы хотите показать: "))
           try:
               max_length=int(input('ввод наибольшей длины у новостей: '))
               break
           except Exception as e:
               print(f'Error!\n{type(e)}')
       except Exception as e:
            print(f'Error!\n{type(e)}')        
    except Exception as e:
        print(f'Error!\n{type(e)}')

params={'appid': appid,
        'count':number_news,
        'maxlength':max_length,
        'format':json}
url=f'{url_base}{url_getnews}'
response=requests.get(url, params=params)
data_output=response.json()
with open("data_structure.json",'w') as file:
    json.dump(data_output, file,indent=4)
#пример: appid=440, number_news=3, max_length=300