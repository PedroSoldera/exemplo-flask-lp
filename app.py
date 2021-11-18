from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

filmes = [
    {"nome_filme": "Star Wars - A vingança dos Sith", "nota_publico": 60, "nota_critica": 80},
    {"nome_filme": "Star Wars - A Ameaça Fantasma", "nota_publico": 59, "nota_critica": 52},
    {"nome_filme": "Star Wars - O Ataque dos Clones", "nota_publico": 56, "nota_critica": 65},
]

@app.route('/')
def index():
    return render_template('index.html', lista=filmes)

@app.route('/adicionar')
def adicionar():
    return render_template('adicionar.html')

@app.route('/salvar', methods=['POST'])
def salvar():
    nome_filme = request.form['nome_filme']
    nota_publico = request.form['nota_publico']
    nota_critica = request.form['nota_critica']
    novos_filmes = {'nome_filme': nome_filme, 'nota_publico': nota_publico, 'nota_critica': nota_critica}

    filmes.append(novos_filmes)
    
    return redirect('https://5000-gray-tahr-puynue2p.ws-us18.gitpod.io/')

@app.route('/buscar', methods=['POST'])
def buscar():
    lista_filme = []
    pesquisa = request.form['pesquisa']
    for filme in filmes: 
        if pesquisa.lower() in filme['nome_filme'].lower():
            lista_filme.append(filme)
    return render_template('buscar.html', lista_filme=lista_filme)

@app.route('/deletar', methods=['POST'])
def deletar():
    deletar = request.form['deletar']
    for filme in filmes:
        if deletar in filme['nome_filme'].lower():
            del filmes[filme]
    return redirect('https://5000-gray-tahr-puynue2p.ws-us18.gitpod.io/')

    
app.run(debug=True)