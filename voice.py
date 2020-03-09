from fuzzywuzzy import fuzz
import time
import datetime
import speech_recognition as sr
import pyttsx3
import requests
from bs4 import BeautifulSoup

API = "http://api.wolframalpha.com/v2/query?input={}&appid={}"
APPID = 'HP97VV-LH7WRTPJLJ'

opts = {
    'alias': ('проблема', 'беда'),
    'tbr': ('скажи', 'расскажи', 'покажи'),
    'cmds': {
        'trans': ('переведи слово', 'переведи предложение'),
        'time': ('время', 'скок время', 'сейчас времени'),
        'stupid1': ('ржаку обоссаку', 'хочу поржать'),
        'tup': ('ты тупая', 'ты молодец'),
        'que': ('вопрос', 'ответ')


    }
}

def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

def callback(recognizer, audio): #slushaet
        try:
            v=[]
            voice=recognizer.recognize_google(audio, language='ru-Ru').lower()
            print('Распознано: '+ voice)
            print(type(voice))
            cmd = voice
            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()  # удаляем имя
                for x in opts['tbr']:
                    cmd = cmd.replace(x, "").strip()  # удаляем скажи расскажи итд
                    # распознаем и выполняем команду
                    cmd = recognize_cmd(cmd)  # вызываем метод для распознавания комнады
                    execute_cmd(cmd['cmds'], v, voice)  # метод для выполнения комнады
        except sr.UnknownValueError:
            print("не распознано")
        except sr.RequestError:
            print("ошибка с вифи")



def recognize_cmd(cmd): #распознает команду
    #ипользуем фуззивуззи для сравниня нечетких команд со всеми существующими
    RC = {'cmds':'', 'percent':0}
    for c,v in opts['cmds'].items():
        for x in v:
            vrt=fuzz.ratio(cmd,x)
            if vrt>RC['percent']:
                RC['cmds']=c
                RC['percent']=vrt
    print(RC)
    return RC

def ask(query):
    print("Asking:", query)
    resp = requests.get(API.format(query, APPID))
    if resp.status_code != 200:
        return None
    dom = BeautifulSoup(resp.text, "lxml")
    result = dom.queryresult.findAll("pod", id="Solution")
    if not result:
        result = dom.queryresult.findAll("pod", id="Result")
    if not result:
        result = dom.queryresult.findAll("pod", id="ChemicalNamesFormulas:ChemicalData")

    subpods = result[0].findAll("subpod")
    return list(pod.plaintext.string for pod in subpods)

import random
import locale
from yandex.Translater import Translater
tr=Translater()

locale.setlocale(locale.LC_ALL, '') #фиксит проблему с библиотекой яндекса

api_key="trnsl.1.1.20200309T060830Z.344d9b14a5d60014.73173e69fc28c824b2288d084ca8e11617d260e1"

def execute_cmd(cmd,v, voice):
    print(cmd)
    if cmd == 'time':
        #cказать время
        now = datetime.datetime.now()
        speak('cейчас ' + str(now.hour) + ':' + str(now.minute))
    elif cmd == 'stupid1':
        #анекдоты ыЫыыы
        l=['хамуда хабиби хамуд', 'запомни лучше посрать и опаздать чем прийти и обосраться', 'споры грибов. о чем они'
                ' спорят?']
        speak(l[random.randint(0, len(l) - 1)])
    elif cmd == 'trans':
        print(voice)
        for x in opts['cmds']['trans']:
            voice = voice.replace(x, "").strip()
        print(voice)
        query = voice
        tr.set_key(api_key)
        tr.set_from_lang('en')
        tr.set_to_lang('ru')
        tr.set_text(query)
        result = tr.translate()
        speak(str(result))
    elif cmd == 'tup':
        speak('я знаю')
    elif cmd == 'que':
        for x in opts['cmds']['que']:
            voice = voice.replace(x, "").strip()
        speak(ask(str(voice)))
    else:
        speak('че')




#ЗАПУСК
r= sr.Recognizer()
m = sr.Microphone(device_index=1)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

speak('приветик')
speak('че надо')

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1)














