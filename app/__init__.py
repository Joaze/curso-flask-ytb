from flask import Flask

#instancia do flask para executar a minha aplicação
#dentro do init somente a declaração da nossa aplicação
app = Flask(__name__)

from app.controllers import default

