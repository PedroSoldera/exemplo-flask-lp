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
    
    return redirect('https://5000-amaranth-moose-j937nk9u.ws-us18.gitpod.io/')

@app.route('/buscar', methods=['POST'])
def buscar():
    lista_filme = []
    busca = request.form['busca']
    for filme in filmes: 
        if busca.lower() in filme['filme'].lower():
            lista_filme.append(filme)
    return render_template('buscar.html', lista_filme=lista_filme)



app.run(debug=True)