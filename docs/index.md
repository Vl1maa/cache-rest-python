## Implementando CACHE com PYTHON e cachetools

### Etapa 1: Configuração do Ambiente

1. **Crie um novo repositório no GitHub** para o seu projeto.
2. **Clone o repositório** para a sua máquina local.
3. **Instale as dependências** necessárias:
   ```bash
   pip install -r requirements.txt
   ```

### Etapa 2: Implementação da Aplicação

1. **Crie um arquivo** chamado `app.py` e adicione o seguinte código para implementar uma aplicação Flask com cache:

   ```python
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

   ```

2. **Execute a aplicação** com o comando `python app.py` e teste o endpoint `/usuarios` com método `GET` para verificar o funcionamento do cache.

<br/>

Obs: note que colocamos um sleep na chamada ao banco de dados para representar o delay que seria precisar ir até o banco de dados para sempre resgatar a mesma informação.

### Contribuições

João Leal = Cuidou da documentação e auxiliou na lógica do código.
<br/>
Gabriel Gimenez = Implementou a API REST com o cache.
<br/>
Vinicius Lima = Criou o repositório, auxiliou na implementação da API REST com cache e na documentação.