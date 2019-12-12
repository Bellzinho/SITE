from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

piadas = [
        {
            'id':'1',
            'pergunta':'O que aconteceu com pintinho binário que não tinha 1?',
            'resposta': 'Foi compilar e explodiu!'
        },
        {
            'id':'2',
            'pergunta':'Eu gosto de iOS e Carlos Drummond?',
            'resposta': 'Carlos Drummond de Android'
        },
        {
            'id':'3',
            'pergunta':'O que o C++ disse para o C?',
            'resposta': 'Você não tem classe!'
        },
        {
            'id':'4',
            'pergunta':'Quanto programadores são necessários para trocar uma lâmpada?',
            'resposta': 'Nenhum, é problema de hardware.'
        },
        {
            'id':'5',
            'pergunta':'O que é um terapeuta?',
            'resposta': '1024 gigapeutas.'
        },
        {
            'id':'6',
            'pergunta':'Como o Nerd faz amigo oculto?',
            'resposta': '.amigo{visibility:hiden}'
        },
        {
            'id':'7',
            'pergunta':'Seja \"int x = 10; int y = 10; print(x + y);\". Qual o nome do filme?',
            'resposta': 'O código dá 20.'
        }
    ]


class Piadas(Resource):

    def get(self):
        return {'piadas':piadas}

api.add_resource(Piadas, '/piadasnerd')

if __name__ == '__main__':
    app.run(debug=True)