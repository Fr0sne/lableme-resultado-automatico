import requests
import json
from win10toast import ToastNotifier
from time import sleep
from os import system
from datetime import datetime

 


url = "https://sislu.dasa.com.br/sislu/ws/portal/resultadosPaginadosUsuario"
while True:
    system('cls')
    
    req = requests.post(url, data="dataInicio=&dataFim=&paginaBuscada=0&resultadosPorPagina=20&login=LOGIN&origem=LEME&senha=PASSWORD")
    content = req.content
    requisicoes = json.loads(content.decode('utf-8'))
    for datas in requisicoes['requisicoes']:
        for exames in datas['exames']:
            print("Exame: " + exames['codigo'])
            print("Nome: " + exames['nome'])
            print("Status: " + exames['status'])
            now = datetime.now()
            horario = now.strftime("%d/%m/%Y %H:%M:%S")
            print("Data da atualização: " + horario)
            if(exames['status'] != "ABERTO"):
                n = ToastNotifier()
                n.show_toast("Laboratório LEME", "Resultado disponível", duration = 10)
                exit()
    sleep(1200)
            
