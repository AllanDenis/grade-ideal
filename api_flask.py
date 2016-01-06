from flask import Flask, jsonify, request
from banco import app
import matricula, modelo, dados

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE', 'OPTIONS'])
def api_echo():
    return "ECHO: " + request.method

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': request.url + ': ' + error,
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
    for disciplina in modelo.Disciplina.select():
        disciplina_dict = vars(disciplina)['_data']
        horario = dados.horario[disciplina_dict['id']]
        horario = [aula for aula in range(len(horario)) if horario[aula] == 1]
        disciplina_dict["horario"] = horario
        disciplinas.append(disciplina_dict)
    return disciplinas

def disciplina_por_id(id_desejado):
    '''Retorna a disciplina cujo ID foi informado, se houver.'''
    disciplina = modelo.Disciplina
    disciplina = disciplina.select()
    disciplina = disciplina.where(modelo.Disciplina.id == id_desejado)
    disciplina = disciplina[0]
    disciplina = vars(disciplina)['_data']
    # O horário é a lista de aulas em que a disciplina é lecionada.
    # As aulas são serializadas semanalmente; a primeira aula é a aula zero;
    # A última aula é dada por aulas_por_dia * dias_por_semana.
    horario = dados.horario[disciplina["id"]]
    horario = [aula for aula in range(len(horario)) if horario[aula] == 1]
    disciplina["horario"] = horario
    return disciplina

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
    if 'historico' in request.json:
        historico = request.json['historico']
        grades = matricula.grade_ideal(historico, max_grades, max_disciplinas)
        grades_json = []
        for grade in grades:
            grades_json.append([disciplina_por_id(id) for id in grade])
        return jsonify({"grades" : grades_json})
    return not_found("Histórico em formato incorreto ou inexistente.")

if __name__ == '__main__':
    app.debug = True
    app.use_reloader = True
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
    app.run(host='0.0.0.0')
