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

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])
def save():
    filme = request.form['filme']
    filme = request.form['nota_publico']
    filme = request.form['nota_critica']
    novos_filmes = { 'Nome filme:':f'{filme}', 'Nota Público'}

    return redirect('https://5000-brown-lemur-kiu2j61j.ws-us18.gitpod.io/')

app.run(debug=True)