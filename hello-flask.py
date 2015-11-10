from flask import Flask, jsonify
import matricula
import modelo

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/disciplinas')
def lista_disciplinas():
    disc = modelo.disciplinas()
    disc = disc.select().get()
    # print(dir(disc))
    disc = {1:"orge",2:"calc"}
    return jsonify(disc)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
