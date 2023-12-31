import random
import requests
import json
import languages

from langdetect import detect

def translate(lang, text):
    
    ispr = lang in languages.langs

    if ispr:

        if len(text) > 5000:

            print('[ ! ZyTranslate ! ] ошибка. слишком большой текст. введитasddе до 5000 символов')

            return

        url = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl={lang}&dt=t&q={text}'
        response = requests.get(url)
        json_data = response.json()
        translation = json_data[0][0][0]

        return translation.encode('utf-8').decode('utf-8')

    print('[ ! ZyTranslate ! ] ошибка. неверный язык.')

def randomTranslate(text):

    lang = random.choice(languages.langs)
    url = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl={lang}&dt=t&q={text}'
    response = requests.get(url)
    json_data = response.json()
    translation = json_data[0][0][0]

    return translation.encode('utf-8').decode('utf-8')

def detectLang(text):

    lang = detect(text)
    
    return lang.encode('utf-8').decode('utf-8')
