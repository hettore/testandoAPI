from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=["POST"])
def cadastrar():
    cep = request.form.get('cep')
    rua = request.form.get('rua')
    cidade = request.form.get('cidade')
    nome = request.form.get('nome')
    numero = request.form.get('numero')
    return render_template('cadastrado.html', cep=cep, rua=rua, cidade=cidade, nome=nome, numero=numero)


@app.route('/busca_cep', methods=['GET'])
def busca_cep():
    cep = request.args.get('cep')
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        rua = dados['logradouro']
        cidade = dados['localidade']
        return jsonify({'rua': rua, 'cidade': cidade})
    return jsonify({})




app.run(debug=True)