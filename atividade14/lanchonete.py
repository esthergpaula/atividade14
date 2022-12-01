import math
from flask import Flask

app = Flask(__name__)

cardapio = [[1,'Cachorro quente', 12.00],
                [2, 'Sanduíche', 23.89],
                [3, 'Pastel', 3.98],
                [4, 'Refrigerante', 5.72],
                [5, 'Suco', 4.35]]

@app.route('/1/<int:x1>/<int:y1>/<int:x2>/<int:y2>')
def exercicio_1(x1,x2,y1,y2):
    a = x2-x1
    b = y2-y1
    d = math.sqrt(math.pow(a, 2)+ math.pow(b, 2))
    return f'a distância entre P1({x1},{y1}) e P2({x2},{y2}) é {d:.2f}'


@app.route('/2/a')
def menu():
    return f'Cardápio {cardapio}'


@app.route('/2/b/<int:x>')
def item(x):
    if x > 0 and x < len(cardapio)+1:
        return f'Cardápio {cardapio[x-1]}'
    else:
        return f'Item não existe'



@app.route('/2/c/<nome>/<float:valor>')
def inserir(nome, valor):
    cardapio.append([cardapio[-1][0]+1, nome, valor])
    return f'{cardapio}'


@app.route('/2/d/<int:id>/<nome>/<float:valor>')
def updateFull(id, nome, valor):
    cardapio[id-1] = id, nome, valor
    return f'{cardapio}'

@app.route('/2/e/<int:id>/nome/<nome>')
def updateNome(id, nome):
    cardapio[id-1][1] = f'{nome}'
    return f'{cardapio}'

@app.route('/2/e/<int:id>/valor/<float:valor>')
def updateValor(id, valor):
    cardapio[id-1][2] = valor
    return f'{cardapio}'

@app.route('/2/f/<int:id>')
def remove(id):
    cardapio.pop(id-1)
    return f'{cardapio}'


if __name__ == 'main':
    app.run()
