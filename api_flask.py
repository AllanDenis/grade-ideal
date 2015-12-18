from flask import Flask, jsonify, request
from banco import app
import matricula, modelo

def lista_disciplinas():
    disciplinas = []
    for d in modelo.Disciplina.select():
        # aulas = matricula.aulas_da_grade(d.id, matricula.horario)
        # aulas = matricula.binario_para_indices(aulas, range(len(aulas)))
        disciplinas.append({
            "id"        :   d.id,
            "nome"      :   d.nome,
            "sigla"     :   d.sigla,
            "periodo"   :   d.periodo,
            "ativa"     :   d.ativa,
            # "horario"   :   aulas,
        })
    return disciplinas

@app.route('/disciplinas', methods = ['GET'])
def disciplinas_list_api():
    return jsonify({"disciplinas" : lista_disciplinas()})

@app.route('/grades', methods = ['POST'])
def melhor_grade():
    max_grades = 3
    max_disciplinas = 6
    if request.json:
        disciplinas_id = matricula.grade_ideal(
                request.json, max_grades, max_disciplinas
            )
        # disciplinas_list = modelo.Disciplina.select().where(id in disciplinas_id).get()
        grades = {"grades" : disciplinas_id}
        return jsonify(grades)
    else:
        return None

if __name__ == '__main__':
    app.debug = True
    app.use_reloader = True
    app.run(host='0.0.0.0')
