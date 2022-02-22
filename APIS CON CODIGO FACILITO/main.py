import requests
import json


if __name__ == '__main__':
    url = 'https://httpbin.org/delete'
    payload = {'nombre': 'Jorge', 'Curso': 'Python', 'Nivel': 'Intermedio'}
    headers = {'content-Type': 'Aplication/json', 'acces-token' : '12345'}

    reponse = requests.delete(url, data= json.dumps(payload), headers = headers)

    #JSON post se encarga de serializarlos
    #data entonces nosotros lo serializamos

    print(reponse.url)

    if reponse.status_code == 200:
        #print(reponse.content)
        headers_response = reponse.headers
        server = headers_response['server']
        print(headers_response)
