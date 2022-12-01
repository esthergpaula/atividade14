from flask import Flask,request

app = Flask(__name__)

@app.route('/1', methods=['POST'])
def exercicio_1():

    x = request.json['x']
    y = request.json['y']
    z = request.json['z']

    if (x+y) > z or (x+z) > y or (y+z) > x:
        return f'{x}, {y} e {z}, podem formar um triângulo'
    else:
        return f'{x}, {y} e {z}, NÃO podem formar um triângulo'

@app.route('/2', methods=['POST'])
def exercicio_2():
    json = request.json['id']
    sapato = 'Sapato R$ 99,99'
    bolsa = 'Bolsa R$ 103,89'
    camisa = 'Camisa R$ 49,98'
    calca = 'Calça R$ 89,72'
    blusa = 'Blusa R$ 97,35'

    if json == 1:
        return f'{sapato}'
    elif json == 2:
        return f'{bolsa}'
    elif json == 3:
        return f'{camisa}'
    elif json == 4:
        return f'{calca}'
    elif json == 5:
        return f'{blusa}'


if __name__ == '__main__':
    app.run()