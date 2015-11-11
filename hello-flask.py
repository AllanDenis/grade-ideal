from flask import Flask, jsonify, request
from flask.ext.cors import CORS
import matricula, modelo

app = Flask(__name__)
CORS(app)

@app.route('/disciplinas', methods = ['GET'])
def lista_disciplinas():
    disciplinas = []
    for d in modelo.Disciplina.select():
        disc_tmp = {
            "id"        :   d.id,
            "nome"      :   d.nome,
            "sigla"     :   d.sigla,
            "periodo"   :   d.periodo,
            "ativa"     :   d.ativa,
        }
        disciplinas.append(disc_tmp)
    return jsonify(enumerate(disciplinas))

@app.route('/grade', methods = ['POST'])
def melhor_grade():
    return "JSON Message: " + str(request.data)
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
