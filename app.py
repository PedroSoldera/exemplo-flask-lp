from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

filmes = [
    {"filme": "Star Wars - A vingança dos Sith", "nota_publico": 60, "nota_critica": 80},
    {"filme": "Star Wars - A Ameaça Fantasma", "nota_publico": 59, "nota_critica": 52},
    {"filme": "Star Wars - O Ataque dos Clones", "nota_publico": 56, "nota_critica": 65},
]

@app.route('/')
def index():
    return render_template('index.html', lista=filmes)

@app.route('/adicionar')
def adicionar():
    return render_template('adicionar.html')

@app.route('/salvar', methods=['POST'])
def salvar():
    filme = request.form['filme']
    nota_publico = request.form['nota_publico']
    nota_critica = request.form['nota_critica']
    novos_filmes = {'Nome filme:':f'{filme}', 'Nota Público': f'{nota_publico}', 'Nota Critica': f'{nota_critica}'}

    filmes.append(novos_filmes)
    
    return redirect('https://5000-coral-mosquito-1pmn8i18.ws-us18.gitpod.io/')

@app.route('/buscar', methods=['POST'])
def buscar():
    lista_filme = []
    busca = request.form['busca']
    for filme in filmes: 
        if busca.lower() in filme['filme'].lower():
            lista_filme.append(filme)
    return render_template('buscar.html', lista_filme=lista_filme)

app.run(debug=True)