
import requests
from datetime import date

from DB import DB

url = 'http://api.openweathermap.org/data/2.5/weather?q=Chapeco,BR&APPID=e18b3342107602110eebebc63bd441aa&units=metric'

res = requests.get(url)

data = res.json()

temperatura = data['main']['temp']
velocidade_vento = data['wind']['speed']

latitude = data['coord']['lat']
longitude = data['coord']['lon']
pais = data['sys']['country']
cidade = data['name']
umidade = data['main']['humidity']
minima = data['main']['temp_min']
maxima = data['main']['temp_max']

descricao = data['weather'][0]['description']

print('Temperatura : {} graus celsius'.format(temperatura))
print('Velocidade do vento : {} m/s'.format(velocidade_vento))
print('Latitude : {}'.format(latitude))
print('Longitude : {}'.format(longitude))
print('Descricao : {}'.format(descricao))
print('Pais : {}'.format(pais))
print('Cidade : {}'.format(cidade))
print('Umidade : {}'.format(umidade))
print('Minima : {}'.format(minima))
print('Maxima : {}'.format(maxima))

data_atual = date.today()

query = 'INSERT INTO historico_clima (cidade, pais, descricao, data_insercao, temperatura, velocidade_vento, latitude, longitude, umidade, temp_minima, temp_maxima) VALUES (\''+format(cidade)+'\', \''+format(pais)+'\', \''+format(descricao)+'\', \''+format(data_atual)+'\', '+format(temperatura)+', '+format(velocidade_vento)+', '+format(latitude)+', '+format(longitude)+', '+format(umidade)+', '+format(minima)+', '+format(maxima)+')'

conexao = DB()
conexao.executarInsert(query)
