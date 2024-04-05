from cachetools import TTLCache
from flask import Flask, jsonify
import time

cache = TTLCache(maxsize=100, ttl=30)
app = Flask(__name__)

def banco_de_dados_simuladio():
    """Simula um acesso demorado a um banco de dados."""
    time.sleep(2)
    return [
        {"nome": "João Leal", "e-mail": "lealjoao394@gmail.com"},
        {"nome": "Gabriel Gimenez", "e-mail": "gabriel2005gimenez@gmail.com"},
        {"nome": "Vinicius Lima", "e-mail": "vini.spec38@gmail.com"}
    ]

@app.route("/usuarios")
def resgata_usuarios_route():
    tempo_de_inicio_da_requisicao = time.time()
    dados = cache.get("usuarios")

    if dados is None:
        dados = banco_de_dados_simuladio()
        cache["usuarios"] = dados

    tempo_de_resposta = time.time() - tempo_de_inicio_da_requisicao
    return jsonify({"dados": dados, "tempo_de_resposta": tempo_de_resposta})

if __name__ == "__main__":
    app.run(debug=True)
