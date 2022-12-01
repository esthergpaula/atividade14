import math
from flask import Flask

app = Flask(__name__)


@app.route('/1/<int:x1>/<int:y1>/<int:x2>/<int:y2>')
def exercicio_1(x1,x2,y1,y2):
    a = x2-x1
    b = y2-y1
    d = math.sqrt(math.pow(a, 2)+ math.pow(b, 2))
    return f'a distância entre P1({x1},{y1}) e P2({x2},{y2}) é {d:.2f}'
if __name__ == '__main__':
    app.run()