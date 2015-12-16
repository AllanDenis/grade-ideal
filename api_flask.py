from flask import Flask, jsonify, request

import matricula, modelo
from banco import app

#app = Flask(__name__)
#CORS(app)
#Compress(app)

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
    return jsonify({"disciplinas" : disciplinas})

@app.route('/grade', methods = ['POST'])
def melhor_grade():
    if request.json:
        grade = jsonify(enumerate(request.json))
        grade = jsonify({"grades" : matricula.grade_ideal(request.json, 1, 6)})
        return grade
    else:
        return None

if __name__ == '__main__':
    app.debug = True
    app.use_reloader = True
    app.run(host='0.0.0.0')
