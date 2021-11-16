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
def save():
    filme = request.form['filme']
    nota_pub = request.form['nota_publico']
    nota_crit = request.form['nota_critica']
    novos_filmes = {'Nome filme:':f'{filme}', 'Nota Público': f'{nota_pub}', 'Nota Critica': f'{nota_crit}'}

    filmes.append(novos_filmes)
    
    return redirect('https://5000-lavender-jay-yx2ss8o4.ws-us18.gitpod.io/')

app.run(debug=True)