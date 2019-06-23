from flask import Flask, jsonify, request
from DB import DB

app = Flask(__name__)

@app.route('/clima', methods=['GET'])
def home():
    query = 'SELECT * FROM public.historico_clima'

    conexao = DB()
    result = conexao.executarSelect(query)
    dados = []
    for cidade in result:
        dados.append({'id': cidade[11],
                      'cidade': cidade[0],
                      'pais': cidade[1],
                      'descricao': cidade[2],
                      'temperatura': cidade[3],
                      'velocidade_vento': cidade[4],
                      'latitude': cidade[5],
                      'longitude': cidade[6],
                      'umidade': cidade[7],
                      'temp_minima': cidade[8],
                      'temp_maxima': cidade[9],
                      'data_insercao': cidade[10]})

    return jsonify(dados), 200


@app.route('/clima/<string:cidade>', methods=['GET'])
def clima_por_cidade(cidade):

    query = 'SELECT * FROM public.historico_clima WHERE historico_clima.cidade = \''+cidade+'\''

    conexao = DB()
    result = conexao.executarSelect(query)
    dados = []
    for cidade in result:
        dados.append({'id': cidade[11],
                      'cidade': cidade[0],
                      'pais': cidade[1],
                      'descricao': cidade[2],
                      'temperatura': cidade[3],
                      'velocidade_vento': cidade[4],
                      'latitude': cidade[5],
                      'longitude': cidade[6],
                      'umidade': cidade[7],
                      'temp_minima': cidade[8],
                      'temp_maxima': cidade[9],
                      'data_insercao': cidade[10]})

    return jsonify(dados), 200

if __name__ == '__main__':
    app.run(debug=True)