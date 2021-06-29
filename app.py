from flask import Flask

#instancia do flask para executar a minha aplicação
app = Flask(__name__)

#decorator definind a  rota principal
@app.route('/')
def index():
    return 'Hello World'

#verificacao para confirmar se o usuário esta executando através do main e não de um arquivo secundario
if __name__=='__main__':
    app.run()

