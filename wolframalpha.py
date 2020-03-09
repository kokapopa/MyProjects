import requests
from bs4 import BeautifulSoup

API = "http://api.wolframalpha.com/v2/query?input={}&appid={}"
APPID = 'HP97VV-LH7WRTPJLJ'


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


print(ask('5 divide by 50'))