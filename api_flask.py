from flask import Flask, jsonify, request
from banco import app
import matricula, modelo

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE', 'OPTIONS'])
def api_echo():
    return "ECHO: " + request.method

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

@app.route('/users/<userid>', methods = ['GET'])
def api_users(userid):
    users = {'1':'john', '2':'steve', '3':'bill'}

    if userid in users:
        return jsonify({userid:users[userid]})
    else:
        return not_found()

def lista_disciplinas():
    '''Retorna a lista de todas as disciplinas.'''
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

def disciplina_por_id(id_desejado):
    '''Retorna a disciplina cujo ID foi informado, se houver.'''
    disciplina = modelo.Disciplina
    disciplina = disciplina.select()
    disciplina = disciplina.where(modelo.Disciplina.id == id_desejado)
    disciplina = disciplina[0]
    return  {
                "id"        :   disciplina.id,
                "nome"      :   disciplina.nome,
                "sigla"     :   disciplina.sigla,
                "periodo"   :   disciplina.periodo,
                "ativa"     :   disciplina.ativa,
            }

@app.route('/disciplina/<int:id>', methods = ['GET'])
def disciplina_api(id):
    return jsonify({"disciplina" : disciplina_por_id(id)})

@app.route('/disciplinas', methods = ['GET'])
def disciplinas_list_api():
    return jsonify({"disciplinas" : lista_disciplinas()})

@app.route('/grades', methods = ['POST'])
def melhor_grade():
    max_grades = 3
    max_disciplinas = 6
    if request.json:
        grades = matricula.grade_ideal(
                request.json, max_grades, max_disciplinas
            )
        grades_json = []
        for grade in grades:
            grades_json.append([disciplina_por_id(id) for id in grade])
        return jsonify({"grades" : grades_json})
    else:
        return None

if __name__ == '__main__':
    app.debug = True
    app.use_reloader = True
    app.run(host='0.0.0.0')
