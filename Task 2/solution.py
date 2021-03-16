import requests


URL = "https://ru.wikipedia.org/w/api.php"
PARAMS = {
    "action": "query",
    "cmtitle": "Категория:Животные_по_алфавиту",
    "cmlimit": "max",
    "list": "categorymembers",
    "format": "json",
    "cmcontinue": '',
}

def main():
    flag = True
    animals_count = {}  

    while flag:

        # while the flag is true, make a request 
        response = requests.get(url=URL, params=PARAMS)
        data = response.json()
        pages = data['query']['categorymembers']
        # an each iteration change 'cmcontinue' parametr to get next pages 
        PARAMS['cmcontinue'] = data['continue']['cmcontinue']

        for page in pages:
            title = page['title']
            # so as not to capture the English names
            if title[0] == "A":
                flag = False
                break
            # if do not do it,  "Helobdella nununununojensis" appears from somewhere in the result xD... 
            if title[0] == 'H':
                continue
            if title[0] not in animals_count.keys():
                animals_count[title[0]] = 0
            animals_count[title[0]] += 1

    return animals_count


if __name__ == "__main__":
    print(main())